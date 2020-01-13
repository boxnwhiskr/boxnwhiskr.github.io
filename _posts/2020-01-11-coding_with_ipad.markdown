---
layout: post
title: 아이패드로 코딩하기
author: 박장시
brief: 5개월 동안 아이패드로 코딩한 경험을 공유합니다.
date: 2020-01-11
---

개발 서버를 따로 만들면, 어떤 기기에서든 연결하여 코딩이 가능하다. 서버를 세팅하고 아이패드를 연결해 개발한 경험을 공유한다.

![ipad.jpg](/img/posts/2020-01-11-coding_with_ipad/ipad.jpg)

# 발단

코딩용으로 사용하던 맥북이 갑자기 고장났다. 2주간 작업 도구가 필요하던 차에 아이패드로 코딩할 수 있지 않을까 생각이 들어 검색하니, 역시나 아이패드로 코딩하는 사람들이 있다. 꼭 아이패드가 아니어도 상관없다. 터미널을 이용해서 [SSH](https://en.wikipedia.org/wiki/Secure_Shell) 연결로 서버에 접속하는 방식이므로 모든 컴퓨터에서 가능하다. 심지어 핸드폰에서도 가능하다.

## 준비물

크게 5가지가 필요하다.

### 아이패드

아이패드는 터미널로만 활용한다. 아이패드 대신 [command-line interface(CLI)](https://en.wikipedia.org/wiki/Command-line_interface)를 쓸 수 있는 어떤 기기든 상관없다. 굳이 아이패드를 쓰는 이유는 이뻐서다. 코딩을 하면 결국 화면 위의 글씨를 한참 쳐다보기 마련인데, 선명한 디스플레이가 주는 장점이 크다.

아이패드가 아니어도 상관없다. 아래에서 이야기할 터미널 에뮬레이터 앱만 있다면 핸드폰에서 코딩하는 것도 가능하다. 일반적으로 [CLI shell](https://en.wikipedia.org/wiki/Shell_(computing)#Text_(CLI)_shells)을 쓸 수 있는 기기라면 아무 문제가 없다.

### 터미널 앱

아이패드에는 터미널이 없다. 따라서 터미널 앱(더 정확하게는 에뮬레이터)이 필요하다. 터미널 앱의 주요 용도는 [SSH](https://en.wikipedia.org/wiki/Secure_Shell) 연결이다. 여기에 [mosh](https://mosh.org)를 사용할 수 있으면 더 편하다. [mosh](https://mosh.org)를 사용하면 터미널 앱을 닫았다가 다시 열어도 서버와 연결된 세션이 끊어지지 않는다. 한참 후에 다시 열어도 전에 작업하던 화면에서 바로 다시 코딩이 가능하다.

터미널 앱은 여러가지가 있는데 [Blink Shell](https://www.blink.sh)을 추천한다. 군더더기 없는 설정에 [mosh](https://mosh.org)를 기본적으로 지원하고 키보드 키 맵핑도 가능하다. `capslock` 키를 `ctrl` 키나 `esc` 키로 변경해서 사용할 수 있다. 다수의 서버 연결도 쉽게 관리할 수 있고, [SSH key](https://en.wikipedia.org/wiki/Ssh-keygen) 설정도 편하다. 필요한 기능만 잘 모아놓아서 매력적이다.

![blinkshell_settings.png](/img/posts/2020-01-11-coding_with_ipad/blinkshell_settings.png)

### 개발 서버

아이패드는 터미널로만 쓰기 때문에 실제 코딩은 개발 서버에서 이루어진다. 연결할 서버가 필요한데, 활용할 서버가 없다면 빌려서 쓸 수 있다. 시중에 많은 클라우드 서비스가 있는데 그 중에서도 [DigitalOcean](https://www.digitalocean.com)에서 제공하는 [Droplets](https://www.digitalocean.com/products/droplets/)를 추천한다. 가장 작은 사이즈가 한 달에 $5인데, 개발 용도로는 큰 부족함이 없다. 일단 가장 작은 사이즈로 시작하고, 필요하면 사용하던 시스템 그대로 업그레이드 한다. 개발 외의 더 무거운 작업을 하기 위해서는 성능이 뛰어난 서버를 잠깐 빌리는 것이 효율적이다. [DigitalOcean](https://www.digitalocean.com) 외에도 비슷한 가격대에 비슷한 성능의 서버를 빌려서 사용할 수 있다.

![droplets_create_settings.png](/img/posts/2020-01-11-coding_with_ipad/droplets_create_settings.png)

### 인터넷

참 당연한 얘기지만, 터미널로 개발 서버에 연결해 작업을 하려면 인터넷 연결이 필수적이다. 로컬 환경에서 작업을 할 수 없다. 따라서 상시 인터넷 연결이 필요하다. 기왕이면 셀룰러 연결이 가능한 태블릿이 편하다. 와이파이 있는지 없는지 확인하고 연결했다가 속도 안 나오면 다른 장소로 옮기는 번거로움을 피할 수 있다. 로컬 작업을 할 수 없다는 점이 어떤 환경에서는 상당한 부담이다. 비행 중인 기내에서나 외딴 섬, 혹은 아프리카 오지 같은 곳에서는 작업할 수 없다. 수시로 인터넷 연결이 끊어지는 환경이라면 그냥 랩탑이 낫다.

![africa.png](/img/posts/2020-01-11-coding_with_ipad/africa.png)

### 외장 키보드와 텍스트 기반 에디터에 익숙한 손가락
아이패드로 본격적인 코딩을 한다면 외장 키보드가 필수적이다. 없어도 할 수는 있지만, 매우 비효율적이다. 되나 안 되나 시험해 볼 목적이 아니라면 외장 키보드가 꼭 필요하다.

아울러 텍스트 기반 에디터에 익숙해져야 한다. [Vim](https://www.vim.org)이나 [Emacs](https://www.gnu.org/software/emacs/) 등을 주로 쓰는데, 처음에는 상당히 생소하다. 이는 기능에 가깝기 때문에 손가락에 익숙해질 때까지 부단히 연습하는 수 밖에 없다. [Vim](https://www.vim.org) 등을 연마하는 것이 부담스럽다면 처음에는 [Nano](https://www.nano-editor.org)를 사용하는 것도 방법이다.

![screen_keyboard.png](/img/posts/2020-01-11-coding_with_ipad/screen_keyboard.png)

# 환경 설정

개발 서버를 세팅하고 아이패드와 연결하는 과정을 설명한다. 크게 어려운 부분은 없으나, 처음에 직접 겪었던 시행착오 위주로 소개한다.

## 개발 서버 생성

[Droplets](https://www.digitalocean.com/products/droplets/)의 가장 작은 인스턴스로 개발 서버를 세팅한다. 우선 서버 위치를 결정해야 하는데, 한국에서는 싱가폴 리전이 가장 빠르다. 보통 지리적으로 가까운 곳에 있는 서버를 쓰는 것이 유리하다. 그러나 대륙을 건너서 사용해야 하는 경우에는 물리적 거리와 무관할 수 있으므로 [스피드테스트](http://speedtest-sgp1.digitalocean.com)를 통해 결정한다.

![digitalocean_sgp_speedtest](/img/posts/2020-01-11-coding_with_ipad/digitalocean_sgp_speedtest.png)

인스턴스 생성 자체는 매우 쉽다. 다만, [SSH key](https://en.wikipedia.org/wiki/Ssh-keygen)를 인스턴스 생성 전에 설정 단계에서 입력하는 것이 편하다. 이를 위해서 우선 [Blink Shell](https://www.blink.sh) 앱의 설정에서 키를 생성한다. 이미 생성되어 있는 디폴트 키를 사용하여도 좋고 새로 만들어도 좋다.

![make_new_ssh_key.png](/img/posts/2020-01-11-coding_with_ipad/make_new_ssh_key.png)

생성된 키를 선택하면 공개키(public key)를 복사할 수 있다.

![made_ssh_key.png](/img/posts/2020-01-11-coding_with_ipad/made_ssh_key.png)

이 때 비밀키(private key)를 복사하지 않도록 주의한다. 공개키가 자물쇠라면 비밀키는 열쇠에 해당한다. 자물쇠를 복사해서 다른 서버에 쓰라고 나눠주는 것은 괜찮지만, 열쇠를 복사해서 쓰라고 나눠주면 보안 취약점을 만들 수 있다. 되도록 비밀키는 생성한 기기 밖으로 나가지 않는 것이 좋다. 꼭 필요한 경우가 아니라면 비밀키는 복사하지 말자.

![copy_public_key](/img/posts/2020-01-11-coding_with_ipad/copy_public_key.png)

복사한 공개키를 인스턴스 생성 시점에 입력하면, 공개키가 생성될 인스턴스에 미리 저장된다. 물론 처음에 패스워드를 이용해서 서버에 접속하고, 이후에 공개키를 직접 복사할 수도 있지만 귀찮기 때문에 추천하지 않는다.

![add_new_ssh_key.png](/img/posts/2020-01-11-coding_with_ipad/add_new_ssh_key.png)

인스턴스 생성 후에 방화벽 설정은 아래 룰을 따른다. [SSH](https://en.wikipedia.org/wiki/Secure_Shell)와 [mosh](https://mosh.org)를 사용하기 위해서 필수적으로 inbound TCP 22, UDP 60000-61000 포트를 열어야 한다. 추후에 필요한 룰은 추가한다. 랩탑에서 작업할 때는 로컬 서버로 열어서 확인하던 작업들이 있는데, 개발 서버를 사용하면 이를 부득이하게 외부로 서빙해서 확인해야 한다. 주로 이 때 필요한 포트들을 룰에 포함시킨다.

예를 들어, 랩탑에서 jekyll로 블로깅을 하면 수시로 로컬 서버에서 배포 상태를 확인해 본다. 개발 서버를 사용하면 로컬 서버에서 배포 상태를 미리 볼 수 없으므로, 임시로 외부 ip에 서빙해서 배포 전에 렌더링 상태를 확인해본다. jupyter 노트북을 사용할 때도 랩탑에서는 주로 로컬 서버를 띄우고 여기에 브라우저로 접근하여 작업한다. 개발 서버를 이용하면 jupyter 서버를 외부 주소로 띄워서 접근한다.

- 참고: [Running a notebook server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

![firewalls_inbound_rules.png](/img/posts/2020-01-11-coding_with_ipad/firewalls_inbound_rules.png)

## 아이패드에서 처음으로 서버에 접속하기

방화벽 설정은 서버에 연결하기 전에 이미 완료되어 있어야 한다. 서버가 제대로 생성되었고 방화벽 설정을 마쳤다면 서버에 처음으로 접속할 수 있다. 처음으로 연결할 때는 `root` 유저를 사용한다. [Blink Shell](https://www.blink.sh)의 host 설정에서 `root` 유저를 입력하고 저장한다. [SSH key](https://en.wikipedia.org/wiki/Ssh-keygen) 설정을 해야 하는데, 위에서 서버 생성할 때 만들어 두었던 바로 그 키를 지정한다. HostName은 생성한 서버의 ip 주소다.

![first_ssh_connection.png](/img/posts/2020-01-11-coding_with_ipad/first_ssh_connection.png)

이제 [Blink Shell](https://www.blink.sh)에서 서버로 접속할 수 있다. [Blink Shell](https://www.blink.sh)에서 다음 명령어를 실행시키면 서버로 연결된다.

{% highlight console %}
blink> ssh test-server
{% endhighlight %}

위에서 `test-server`는 host 설정할 때 지정한 host의 별명이다.

![success_ssh_connetion.png](/img/posts/2020-01-11-coding_with_ipad/success_ssh_connetion.png)

## 새 유저 만들기

리눅스에서 `root` 유저로 접속하여 작업하는 경우는 거의 없다. 현재 접속 중인 세션은 초기 설정을 위해서 `root` 유저로 접속한 상태다. `root` 유저는 모든 권한을 가지고 있기 때문에 위험하다. 평소 작업을 할 때는 일반 유저를 만들어서 사용한다. `tester`라는 일반 유저를 만들자.

{% highlight console %}
# adduser tester
{% endhighlight %}

생성 중에 여러가지 질문이 나오는데 넘어가도 상관없다. 패스워드 설정은 중요하므로 잘 기억해둔다.

새로 만든 계정에 관리자 권한을 부여한다. `root` 유저는 모든 명령이 관리자 권한으로 실행되지만, 일반 유저에 관리자 권한을 부여하면 `sudo` 명령으로만 관리자 권한을 사용할 수 있다. 

{% highlight console %}
# usermod -aG sudo tester
{% endhighlight %}

이제 `tester` 유저는 `sudo` 명령으로 관리자 권한을 사용할 수 있다.

새로 만든 `tester` 유저로 외부에서 접속을 하려면, 필요한 [SSH key](https://en.wikipedia.org/wiki/Ssh-keygen)를 복사해주어야 한다. 처음에 서버를 설정하면서 입력한 공유키는 이미 `root` 유저에게 있는데 이를 복사해서 사용한다.

{% highlight console %}
# rsync --archive --chown=tester:tester ~/.ssh /home/tester
{% endhighlight %}

이제 새로운 유저로 접속할 준비가 되었다. `exit` 명령어로 접속을 끊고 다시 [Blink Shell](https://www.blink.sh)로 돌아온다.

{% highlight console %}
# exit
{% endhighlight %}

## 새 유저로 접속하기

[Blink Shell](https://www.blink.sh)에서 `root` 유저가 아니라 새로 만든 일반 유저 `tester`로 접속하려면 host 설정에서 user를 기존의 `root`에서 `tester`로 바꿔준다. 다른 설정은 그대로 사용한다.

![change_user.png](/img/posts/2020-01-11-coding_with_ipad/change_user.png)

이제 다시 서버에 접속하면 `root` 유저가 아니라 `tester` 유저로 접속하게 된다.

{% highlight console %}
blink> ssh tester
{% endhighlight %}

아무 문제 없이 접속 되었다면 접속 유저를 확인해보자.

{% highlight console %}
> whoami

tester
{% endhighlight %}

이제부터 개발 서버에 접속할 때는 `tester` 유저로 접속한다.

## mosh 사용하기

[mosh](https://mosh.org)를 사용하지 않는다면 아이패드를 새로 열어서 작업을 할 때마다 새로운 터미널 접속 세션을 만들어야한다. [Blink Shell](https://www.blink.sh)은 이미 [mosh](https://mosh.org)를 지원하기 때문에 서버에만 [mosh](https://mosh.org)를 설치하면 된다. 일단 서버에 [SSH](https://en.wikipedia.org/wiki/Secure_Shell) 접속을 하고 시스템 업데이트를 한다.

{% highlight console %}
blink> ssh test-server

...

> sudo apt update
> sudo apt upgrade
{% endhighlight %}

`sudo` 명령어는 관리자 권한으로 다음 명령어를 실행하겠다는 의미다. 패스워드를 요구하면 새 유저를 만들며 설정한 패스워드를 입력한다. 업데이트가 제대로 이루어지지 않는다면 서버의 outbound 방화벽 설정을 살펴본다.

![firewall_outbound_rules.png](/img/posts/2020-01-11-coding_with_ipad/firewall_outbound_rules.png)

업데이트와 업그레이드가 제대로 이루어진다면 무언가 잔뜩 다운로드 받고 설치하느라 서버가 한참 바쁘다. 설치가 모두 끝나면 서버를 리부팅시켜준다.

{% highlight console %}
> sudo reboot
{% endhighlight %}

접속이 바로 끊기고 [Blink Shell](https://www.blink.sh)로 돌아온다. 잠깐 기다렸다가 다시 [SSH](https://en.wikipedia.org/wiki/Secure_Shell) 연결로 서버에 접속한다. 이제 [mosh](https://mosh.org)를 설치하자.

{% highlight console %}
blink> ssh test-server

...

> sudo apt install mosh
{% endhighlight %}

설치가 무사히 끝났다면 다시 접속을 끊고 [Blink Shell](https://www.blink.sh)로 돌아왔다가 [mosh](https://mosh.org)로 접속한다. 그동안 서버에 접속하면서 사용한 `ssh` 명령어가 아니라 `mosh` 명령어로 서버에 접속한다.

{% highlight console %}
> exit

...

blink> mosh test-server
{% endhighlight %}

무사히 서버에 접속했다면 이제 기본적인 서버 세팅은 모두 끝났다. 이제부터 일부러 접속을 끊지 않는 한 아이패드에서 [Blink Shell](https://www.blink.sh)을 열면 기존에 작업하던 개발 서버가 항상 터미널로 연결되어 있다. 특별한 이유가 없다면 서버에 접속할 때는 되도록 [mosh](https://mosh.org)를 사용한다.

# 개발 환경 설정

이제 터미널과 서버가 생겼으니 이를 통해 직접 개발을 할 차례다. 무엇을 만드느냐에 따라서 환경 설정이 매우 다른데, 개발 환경과 관련해서는 매우 간략하게 소개만 한다. 구체적인 세팅을 모두 소개하면 글이 매우 길어질 것 같은데, 이에 대해서는 추후에 따로 정리하려고 한다. 일단 리눅스 환경에서 터미널로 작업할 때의 환경 설정을 검색하면 당장 참고할 수 있는 자료가 많다. 주제별로 참고한 글의 링크를 아래에 함께 정리한다.

## Vim

[Vim](https://www.vim.org)은 사용할 수 있는 애드인이 매우 많다. 사실상 핵심적인 [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)의 기능은 애드인으로 [Vim](https://www.vim.org)에서 사용할 수 있다. 처음에 [CLI](https://en.m.wikipedia.org/wiki/Command-line_interface) 환경에서 [Vim](https://www.vim.org)으로 개발을 시작하면 그 빈약한 기능 때문에 다시 화려한 [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)로 돌아가고 싶다. 어떤 애드인으로 무슨 기능을 사용할 수 있는지 몰라서 이런 경우가 생기는데, 자신이 개발하는 언어를 기반으로 검색을 해보면 [Vim](https://www.vim.org)에서 쓸 수 있는 다양한 애드인을 찾을 수 있다. 정말 안 되는 게 없다.

- [VIM and Python – A Match Made in Heaven](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
- [Vim](https://www.fullstackpython.com/vim.html)
- [Use Vim as a Python IDE](https://spacevim.org/use-vim-as-a-python-ide/)

## tmux

[tmux](https://tmux.github.io)는 터미널 환경을 멀티 분할 스크린으로 사용할 수 있게 해준다. 여러 개의 창으로 나눠서 작업을 할 수 있고, 개별 세션을 관리할 수 있다. [tmux](https://tmux.github.io)에 여러 개의 프로젝트 별로 다른 세션을 만들어서 작업 환경을 지정해두면 편리하게 프로젝트를 불러와서 작업할 수 있다. 프로젝트를 건너 다닐 때마다 매번 번거롭게 스크린 설정을 다시 하거나 유틸리티를 실행시킬 필요가 없다. 직전 작업 상태 그대로 유지해 둔 세션을 불러오기만 하면 된다.

- [A Quick and Easy Guide to tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)
- [Tactical tmux: The 10 Most Important Commands](https://danielmiessler.com/study/tmux/)

[tmux](https://tmux.github.io)를 쓰면 같은 세션에 두 개 이상의 원격 터미널이 접속할 수 있다. 하나의 화면을 여러 명이 공유해서 볼 수 있어서 이를 통해 원격으로 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)이 가능하다. 보통 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)은 하나의 모니터와 하나의 키보드 앞에 두 명이 같이 앉아서 번갈아 가며 키보드를 사용한다. 물리적으로 떨어져 있으면 짝으로 작업하기 어렵다. 그런데 [tmux](https://tmux.github.io)로 물리적 한계를 극복할 수 있다. 두 사람이 원거리에서 같은 화면을 함께 보며 하나의 커서로 번갈아 코딩한다.

함께 일하는 동료([@alankang](https://twitter.com/alankang))와 원격으로 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)을 할 때 이 방법을 사용한다. 같은 개발 서버에 붙어서 음성 통화로 이야기하며 작업하면 꽤 만족스럽다. 원격으로 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)을 하기 위해서 여러가지 시도를 해왔는데, 지금은 [tmux](https://tmux.github.io) 사용으로 정착하고 있다.

- [Remote Pair Programming Made Easy with SSH and tmux](https://www.hamvocke.com/blog/remote-pair-programming-with-tmux/)

## 테마 설정

테마라 하면 터미널 스크린의 색깔과 글씨 크기, 폰트 등 거의 모든 시각적 설정을 말한다. 크게 네 가지 부분에서 설정할 수 있는데, [Blink Shell](https://www.blink.sh), [Bash](https://www.gnu.org/software/bash), [Vim](https://www.vim.org), [tmux](https://tmux.github.io)가 각각의 테마를 제공한다. 터미널에 연결해서 텍스트 기반 에디터를 켜면 처음에는 그 볼품 없는 모양 때문에 흥미가 떨어지는데, 상상하는 거의 모든 곳을 마음대로 고칠 수 있다. [Bash](https://www.gnu.org/software/bash) 대신에 [Z shell](https://www.zsh.org)을 쓴다면 할 수 있는 건 더 많아진다. 개발하면서 테마가 무슨 소용이 있을까 생각할 수 있지만, 보기 싫은 작업 환경에서는 일하기도 싫어진다. 게다가 적절한 정보를 보기 쉽게 표시해주는 것만으로도 작업 효율이 올라간다.

- [What are the best VIM color-schemes?](https://www.slant.co/topics/480/~best-vim-color-schemes)

## 랩탑 환경과 비교

가장 큰 차이는 마우스를 쓸 수 없다는 점이다. 텍스트 환경의 볼품없는 에디터는 테마로 얼마든지 멋지게 고칠 수 있다. [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)에서 요긴하게 써먹던 기능들도 [Vim](https://www.vim.org) 애드인을 통해 거의 동일하게 사용할 수 있다. 극복할 수 없는 차이는 마우스로 화면 위에 커서를 움직일 수 없다는 점이다. 처음에 아이패드로 개발을 하면서 가장 답답한 점이 이 부분인데, [Vim](https://www.vim.org)을 열심히 연습하면서 극복하는 방법 밖에는 없다. 그리고 익숙해지면, 절대로 그 이전 상태로 돌아갈 수 없다.

사용하던 랩탑이 얼마나 대단한 스펙의 기기인지 깨달았다. 가장 작은 서버 인스턴스는 CPU가 1개에 1GB의 램을 가지고 있는데, 개발하면서 거의 불편함을 느낄 수 없다. 가끔 램이 모자란 경우에 2GB로 확장하면 한 달에 $10의 비용이 들어가는데 이 정도만 해도 상당히 쾌적하다. 심지어 터미널로 사용하는 아이패드의 성능이 압도적으로 좋은 역설적인 상황이다. 기존에 쓰던 랩탑에 비해 초라한 수준의 서버에서도 쾌적하게 코딩이 가능한 것이 신기하다. 그동안 항상 최고 성능의 기기만 고집했던 것이 부질 없었다는 생각이 든다. [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)가 얼마나 자원을 많이 사용하는지 생각해 볼 기회가 되었다.

개발 서버가 가장 답답할 때는 딥 러닝 모델을 학습시킬 때였다. 이런 경우 최소 사양의 개발 서버에서 작업을 완수할 수 없다. 다만 컴퓨팅 파워가 필요한 시점은 코딩을 시작한 후에도 한참 후이기 때문에, 필요한 시점에 GPU cloud를 사용하는 게 효율적이다. 필요한 시간 동안에만 적절한 자원을 사용할 수 있다. 시중에 관련 서비스가 편리하게 많이 나와 있어서 최소한의 비용으로 작업할 수 있다. 개발 서버에서는 코딩만 하고 복잡한 계산은 더 비싼 서버가 잠깐 수행하는 구조다.

# 좋은 점

아이패드로 [CLI](https://en.m.wikipedia.org/wiki/Command-line_interface) 환경에서 작업을 하면 좋은 점이 무척 많다.

## 아이패드

우선 가볍다. 어디든 기기를 들고 다니면서 일을 하기 때문에, 전에는 무거운 가방을 당연하게 받아들였다. 오히려 더 좋은 가방을 사서 무거운 물건을 효율적으로 휴대하기 위해 노력했다. 아이패드로 코딩하면서 가방이 매우 가볍고 작아졌다. 함께 일하는 동료([@alankang](https://twitter.com/alankang))는 아이패드 11인치를 쓰는데, 어느 날부터 시장 바구니 같은 걸 손에 들고 다닌다. 장보러 온 사람 같다. 정든 백팩과 이별하게 되었다.

배터리 걱정에서 해방된다. 아직까지 일하면서 한 번도 아이패드가 방전된 경우가 없다. 카페에서 전원을 찾을 필요도 없고, 보조 배터리와 충전기를 들고 다니지 않아도 된다. 대부분의 연산이 개발 서버에서 이루어지기 때문에 다른 짓(?)을 하지 않는다면 아이패드의 전력 소모는 매우 적다. 배터리가 더 오래 가는 이유다.

애플 펜슬로 스케치를 더 많이 한다. 개발하다 보면 생각해서 정리하고 그림 그리거나 스케치를 하는 시간이 많다. 키보드를 두드리는 시간은 생각보다 적다. 그래서 항상 가방에 하얀 종이와 펜을 가지고 다녔는데, 애플 펜슬을 쓰면서 훨씬 부담 없이 낙서를 한다. 낙서하는 시간이 많아질수록 코딩에 필요한 시간은 줄어든다. 게다가 원격으로 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)을 할 때 스케치를 공유할 수 있다. 말로만 설명할 수 없을 때 요긴하다. 스케치 공유는 [Whiteoboard](https://products.office.com/en-us/microsoft-whiteboard/digital-whiteboard-app)로 한다.

종이 같은 필기감을 주는 필름을 붙이면 애플 펜슬로 글쓰기가 훨씬 쾌적해진다. 다만, 펜 촉이 빨리 닳는데 교체 가능하다. 노트를 자주 쓰는 사람이라면 고려할 만하다.

조약한 품질의 랩탑 키보드에서 해방된다. 그동안 맥북의 소위 ‘나비’식 키보드를 억지로 참고 썼다. 저렴한 외장 블루투스 키보드만으로도 타이핑이 훨씬 즐거워진다. 부작용으로 놀라운 기계식 키보드의 세계를 알게 되었다.

![keyboards.jpg](/img/posts/2020-01-11-coding_with_ipad/keyboards.jpg)

## CLI

[Vim](https://www.vim.org)에 익숙해진다. [Vim](https://www.vim.org)은 처음에 배우기가 참 어렵지만, 일단 익숙해지면 매우 효율적으로 코딩할 수 있다. 그래도 일부러 공부하는 것이 참 괴로운데, 이것 말고 방법이 없게 되면 익힐 수 밖에 없다. 제약을 강화하면 다른 면에서 효율이 올라간다. [Practical Vim](https://pragprog.com/book/dnvim2/practical-vim-second-edition)을 읽고, 배운 것을 평소에 써먹으려고 노력하는 것이 중요하다. 외국어 습득 과정과 유사하게, 계속 머리 속에서 인출하는 연습이 필요하다. 기본 기능만 꾸준하게 사용하면 능률이 안 오르고, 항상 ‘[hjkl](https://catonmat.net/why-vim-uses-hjkl-as-arrow-keys)’만 누르게 된다. 감을 유지하기 위해서 가끔씩 [Vim golf](https://www.vimgolf.com)를 치는 것도 좋다. 효율적인 키 스트로크를 떠올리기 위해서 타이핑을 멈추고 잠시 생각하는 시간을 아까워하지 않아야 한다.

원격 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)이 원활하다. 꼭 [CLI](https://en.m.wikipedia.org/wiki/Command-line_interface)에서 [tmux](https://tmux.github.io)를 쓰지 않아도 원격 [짝 프로그래밍](https://en.wikipedia.org/wiki/Pair_programming)은 가능하다. 대안으로 [AWS Cloud9](https://aws.amazon.com/cloud9/)이나 [Visual Studio Code](https://code.visualstudio.com)가 있다. 다만 [tmux](https://tmux.github.io)를 쓰는 방법이 가장 쉽고 간편하다.

리눅스에 익숙해진다. 정확하게 말하면 리눅스의 [CLI](https://en.m.wikipedia.org/wiki/Command-line_interface)와 친해진다. 대안이 없다. 뭔가를 하려면 무조건 텍스트로 명령어를 치는 수 밖에 없으니 자주 쓰게 되고, 편해진다. 개발을 시작한 이래로 이 검은 화면이 편해지는 날은 오지 않을 거라고 생각했는데, 이제 무섭지는 않다. [The Linux Command Line](http://linuxcommand.org/tlcl.php)을 읽어보면 많은 도움이 된다. 역시나 배운 걸 실제로 써먹어 보려는 시도를 지속하는 것이 중요하다.

눈에 띈다. 빛나는 사과 마크보다 아이패드 검은 화면 위에서 코딩하는 게 더 멋지다. CLI is the new black!

# 결론

처음에는 잠깐만 아이패드를 개발용으로 쓸 생각이었다. 그런데 몇 주 쓰다보니 딱히 불편한 점이 없었고, 사소한 문제들은 항상 해결책이 있었다. 오히려 그런 제약들을 해결하느라 새로운 걸 배우고, 더 효율적으로 작업할 수 있게 되었다. 지금은 자주 고장나던 맥북을 처분하고, 아이패드로만 개발한다. 굳이 잘 쓰고 있는 랩탑을 없애고 태블릿 환경으로 옮길 필요는 없겠지만, 이렇게도 코딩할 수 있다.

# 참고

위의 글은 아래 링크들을 참고하였다.

- [Initial Server Setup with Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)
- [Blink Shell for iOS](https://jblevins.org/log/blink-shell)
- [Using the iPad Pro as my development machine](https://arslan.io/2019/01/07/using-the-ipad-pro-as-my-development-machine/)
