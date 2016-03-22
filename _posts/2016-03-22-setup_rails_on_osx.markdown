---
layout: post
title: Mac OS X에서 rails 개발 환경 구축하기
author: 김재우
brief: 맥에서 rails 개발을 하기 위한 기본적인 환경 구축에 대해 설명한다.
date: 2016-03-22
---


Box and Whisker는 신규 서비스의 개발 플랫폼으로 ruby on rails를 선택했다. rails를 선택한 이유에 대해선 나중에 따로 풀어보기로 하고, 이번 포스팅에선 OSX에서 rails를 개발하기 위한 환경 구축에 대해 다루기로 한다.

## Homebrew

[Homebrew](http://brew.sh/)는 Linux의 apt나 yum 같은 software package manager로 OSX에서 다양한 프로그램의 설치와 업데이트, 삭제를 간단한 명령(command line)으로 할 수 있게 해 준다. Homebrew의 설치는 쉘(bash or zsh)에서 아래의 명령을 실행하면 된다. 혹시 Xcode가 설치되어 있지 않으면, 소스 컴파일에 필요한 Command Line Tools가 함께 설치된다.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Homebrew는 /usr/local 디레토리 아래에 설치되는데, 이 디렉토리의 소유자를 homebrew를 설치한 사용자의 계정으로 하기 때문에 sudo 명령 없이도 패키지를 관리 할 수 있다. 

## ruby

OSX에는 ruby가 설치되어 있기는 하나, 오래된 버전(2.0.0)이 설치되어 있어 최신 버전의 ruby를 설치할 필요가 있다. brew를 통해 바로 설치할 수도 있긴 하지만, rbenv + ruby-build를 이용해 루비를 설치하고, 설치된 버전을 관리하는 것이 좋다. 간혹 오래 묵은 프로젝트를 열어봐야 할 때처럼 옛날 버전의 ruby가 필요할 때가 있는데, rbenv를 이용하면 프로젝트별로 다른 버전의 ruby를 사용할 수 있다.

일단 brew로 rbenv와 ruby-build를 설치한다.

``` shell
$ brew install rbenv ruby-build 

```

설치 후 rbenv 사용에 필요한 환경 변수를 세팅한다.

``` shell
$ eval "$(rbenv init -)"
$ echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

```

rbenv 설치가 완료되었으면, 설치할 수 있는 최신 버전의 루비를 확인하고, 해당 버전을 설치한다. 

``` shell
$ rbenv install -l | egrep '^\s+[2-9]' | tail -4
$ rbenv install -k 2.3.0 
$ rbenv global 2.3.0
```

install 명령을 실행할 때 -k 옵션을 주는데, ruby gem을 설치할 때 가끔 ruby 소스가 있어야 하는 것들이 있으므로 컴파일 후 소스를 삭제하지 않고 남겨주도록 하는 옵션이다. 시스템에서 어떤 버전의 루비를 사용할지 정하는 명령은 `rbenv global`인데, 혹시 프로젝트 별로 다른 버전을 사용하게 될 땐 해당 프로젝트 디렉토리에서 `rbenv local`명령으로 사용할 버전을 지정하면 된다.

## rails 

ruby로 만든 library는 보통 gem 형태로 제공되고, `gem install` 명령으로 설치할 수 있다. rails의 설치는 아래의 명령을 실행하면 된다. rails와 함께 설치하는 bundler는 프로젝트별 gem의 의존성을 관리하고 설치해주는 툴이다. 실행파일이 포함된 gem은 설치 후 `rbenv rehash` 명령을 실행해줘야 한다.

``` shell
$ gem install rails bundler
$ rbenv rehash
```

rails를 설치했으면 간단한 프로젝트를 하나 만들어보자. 

``` shell
$ rails new rule_the_world
$ cd rule_the_world
$ rails s
```

이제 브라우저로 [localhost:3000](http://localhost:3000)에 접속해보자. 이렇게 rails까지 설치하면 rails로 웹 개발을 할 수 있는 환경을 다 갖췄다고 볼 수 있다. 하지만 매번 `rails s`명령으로 웹 서버를 실행하는 것도 번거롭고, 혹은 동시에 2개 이상의 프로젝트를 띄워야 할 때 포트를 바꾸는 것도 헷갈린다. 개발 환경에서도 실 서비스 환경과 동일하게 https 프로토콜을 사용하고 싶다면 rails의 기본 웹 서버만으론 부족하다. 

## Pow

[Pow](http://pow.cx/)를 사용하면 위에서 이야기한 몇 가지 불편이 해결된다. 

``` shell
$ brew install pow
$ mkdir -p ~/Library/Application\ Support/Pow/Hosts
$ ln -s ~/Library/Application\ Support/Pow/Hosts ~/.pow
$ sudo pow --install-system
$ pow --install-local
$ sudo launchctl load -w /Library/LaunchDaemons/cx.pow.firewall.plist
$ launchctl load -w ~/Library/LaunchAgents/cx.pow.powd.plist
$ ln -s ~/projects_dir/rule_the_world ~/.pow/
$ open http://rule_the_world.dev/
```

위의 명령을 실행하면 root 권한으로 80 포트에 웹 proxy 서버가 실행되고, node로 만든 rack web server가 20599 포트로 뜬다. 20560 포트로는 *.dev 도메인을 127.0.0.1로 찾아주는 DNS 서버가 실행된다. ``/etc/resolver/dev`` 파일에는 *.dev 도메인에 대해서는 127.0.0.1:20560에 떠 있는 DNS 서버에서 조회하란 내용이 설정된다.

브라우저로 `http://rule_the_world.dev` 페이지를 열면, `rule_the_world.dev` 도메인이 `127.0.0.1`로 resolve되고, 브라우저는 localhost의 80 포트에 접속한다. 80포트에 떠 있는 proxy 서버는 이 요청을 20599 포트로 넘기고, 20599 포트의 웹 서버가 `~/.pow` 디렉토리에 링크된 rails 프로젝트를 서비스 해 준다. 새 프로젝트가 추가되어도 `~/.pow` 디렉토리에 링크 걸기만 하면 된다. `/etc/hosts` 파일을 고칠 필요 없이 `프로젝트이름.dev` 도메인에 접속하기만 하면 된다. 매번 호스트 파일 설정을 하고, 사용할 포트를 정하고, 터미널 열어서 웹 서버를 띄울 필요가 없다. 그리고, pow가 실행한 rails(rack) 어플리케이션은 사용하지 않으면 자동으로 내려가고 필요할 때 다시 실행된다. 개발 중인 모든 rails 프로젝트가 다 떠 있으면 리소스를 많이 먹지 않을까? 걱정할 필요 없다.

## https

아쉽게도 Pow는 https 프로토콜까지 지원하진 않아, https를 사용하기 위해선 Apache나 nginx등의 웹 서버를 써야 한다. root 계정으로 실행되는 80 포트의 proxy 서버만 nginx로 교체하면 20599 포트의 pow 서버는 그대로 두고 로컬에서 https까지 사용할 수 있다. 

일단 pow가 설치한 proxy 서버를 제거하고,

``` shell
$ sudo launchctl unload -w /Library/LaunchDaemons/cx.pow.firewall.plist
$ sudo rm /Library/LaunchDaemons/cx.pow.firewall.plist
```

nginx 설치 후 필요한 설정파일을 다운로드 받고, nginx를 root계정으로 실행한다. OSX에 기본으로 깔린 git은 버전이 낮으므로 nginx 컴파일을 위해선 brew를 통해 git을 따로 설치해야 한다.

``` shell
$ brew install git
$ brew install --devel nginx
$ curl https://dl.dropboxusercontent.com/u/124346/nginx_config.tgz | tar xvzf - -C /usr/local/etc/nginx/ 
$ sudo curl https://dl.dropboxusercontent.com/u/124346/homebrew.mxcl.nginx.plist -o /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
$ sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
```

homebrew.mxcl.nginx.plist 파일은 nginx 설치 시 생성되는 /usr/local/opt/nginx/homebrew.mxcl.nginx.plist 파일에 nginx를 띄우는 사용자를 `root`로 하라는 내용만 추가한 것이다. 

공유한 nginx virtual host 설정 파일은 아래와 같다.

``` nginx
# pow.conf 

server {
    server_name ~^(?<app>.+)+\.(?<ext>dev|ngrok\.io)$;
    listen 80;
    listen 443 ssl http2;

    ssl_certificate     /usr/local/etc/nginx/ssl/dev.cert;
    ssl_certificate_key     /usr/local/etc/nginx/ssl/dev.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS';
    ssl_prefer_server_ciphers on;


    location / {
        #proxy_set_header Host $host;
        proxy_set_header Host $app.$ext;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_redirect off;
        proxy_pass http://localhost:20559; # The real pow port
    }
}
```

80, 443(https) 포트로 들어오는 `*.dev` 요청에 대해 20559 포트로 proxing 해준다. nginx의 virtual host 설정은 위와 같이 regular expression을 사용할 수 있어서, 프로젝트별로 따로 proxy 설정을 할 필요가 없다. `*.dev` 도메인에 대한 SSL 인증서는 self-signed 된 것으로 브라우저에 경고가 떠서 조금 불편하긴 하지만 개발용으로 쓰기엔 크게 문제가 없다. 혹시 인증서가 만료되었으면 [여기](https://gist.github.com/gerald-kim/3d8fcc60c10b08b8ef02)에서 스크립트를 다운로드 받아 인증서를 생성하면 된다.

## 마무리

지금까지 Box and Whisker의 rails 개발 환경에 대해 살펴보았다. 설치하고 설정할 내용이 많아 번거롭긴 하지만 딱 한 번만 제대로 설정해두면 hosts 파일을 손대지 않아도, rails 서버를 수동으로 실행하지 않아도, SSL을 적용할 때마다 nginx 설정파일을 새로 만들지 않아도 된다. 프로젝트를 checkout 받고 `~/.pow/` 디렉토리에 링크 걸어주기만 하면 된다. 

OSX에서 rails를 개발할 때에만 적용되는 내용이라 아쉽다면, 아래의 툴을 이용해서 linux 환경에서도 다른 언어/프레임웍을 사용할 때도 비슷한 환경을 구축할 수 있다.

* [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html)를 이용하면 [OSX](http://asciithoughts.com/posts/2014/02/23/setting-up-a-wildcard-dns-domain-on-mac-os-x/)뿐 아니라 [linux](https://www.computersnyou.com/3786/how-to-setup-dnsmasq-local-dns/)에서도 개발용 wildcard domain을 설정할 수 있다.
* [bam](https://github.com/jweslley/bam/) go 언어로 작성한 reverse proxy 서버로 rails(rack) 어플리케이션 뿐 아니라 [Procfile로 띄울 수 있는 모든 어플리케이션](https://devcenter.heroku.com/articles/procfile) (java, node, python, ...)을 지원한다.
* [prax](https://github.com/ysbaddaden/prax) 같은 linux에서 사용할 수 있는 pow의 대안도 있다. 
