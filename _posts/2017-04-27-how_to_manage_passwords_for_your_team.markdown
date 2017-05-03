---
layout: post
title: 팀 공용 계정 비밀번호 관리하기
author: 박장시
brief: "'pass'를 이용하여 팀 공용 계정의 비밀번호를 관리합니다"
date: 2017-04-27
---

팀 프로젝트가 늘어나면 프로젝트 내부에서 사용한 부가 서비스의 계정들이 쌓이기 시작한다.
이러한 공용 계정을 쉽고 안전하게 공유할 수 있는 방법에 대해서 소개한다.

# 수 많은 공용 계정과 비밀번호

개발 프로젝트를 수행하다 보면, 많은 외부 서비스를 모듈로 사용한다.
AWS 계정 정보나 각 서버의 접속 키 파일(AWS의 .pem 등)부터 테스트 이메일 계정, 배포 서비스 계정, 모니터링 서비스 계정 등 열거하면 수 없이 많다.
서비스 계정 정보가 아니더라도 법인 신용카드 정보같이 조직원이 함께 알아야 하지만 게시판 아무 곳에나 적어두기에는 꺼림칙한 정보들이 있다.

구성원이 적거나, 진행 중인 프로젝트가 몇 개 없다면 구성원 각자가 알아서 계정을 잘 기억해둘 수 있다.
그러나 프로젝트가 커지거나, 다수의 프로젝트를 한꺼번에 관리하려면 개인들의 기억력에만 의존할 수는 없다.
보안과 밀접하므로 팀 게시판을 활용할 수도 없다.
더 안전하고 쉬우면서 공짜인 방법이 필요하다.

# pass 시작하기

이를 위해서 [pass](https://www.passwordstore.org/)가 있다.
'pass'는 [gpg](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) 기반의 패스워드 관리 툴이다.
cli 기반이므로 쓰기도 아주 쉽다.
게다가 공짜다.
안 쓸 이유가 없다.

![pass](/img/posts/2017-04-27-how_to_manage_passwords_for_your_team/pass-example.png)

## pass 설치

Mac 기준으로 설명한다.
우선 'brew'로 'pass'를 설치하고 자동 완성 세팅을 한다.

    $ brew install pass
    $ echo "source /usr/local/etc/bash_completion.d/password-store" >> ~/.bash_profile

## gpg key 생성

gpg key를 만든다.
gpg는 비대칭키 방식의 암호화를 사용할 수 있는 오픈 소스 툴이다.
혹시 이미 생성한 gpg key가 있다면 기존 키를 그대로 사용해도 무방하다.

    $ gpg2 --gen-key

gpg를 이용해서 키를 생성하면 공개 키(public key)와 비밀 키(prviate key)가 함께 생성되고, '~/.gnupg/' 디렉토리에 저장된다.
종종 키 생성에 시간이 오래 걸릴 때가 있는데, 키 생성에 필요한 엔트로피가 부족하기 때문이다.
이런 경우 다음 글을 참조한다.

*   [Is GPG Hanging When Generating a Key?](https://delightlylinux.wordpress.com/2015/07/01/is-gpg-hanging-when-generating-a-key/)

생성한 gpg key를 확인하면 아래와 같이 방금 전에 만든 키를 확인할 수 있다.

    $ gpg2 --list-keys

    /home/jngsp/.gnupg/pubring.kbx
    -------------------------------
    pub   rsa2048/BD699A08 2017-04-27 [SC]
    uid         [ultimate] jngsp <jngsp@test.com>
    sub   rsa2048/E716C901 2017-04-27 [E]

여기서 'BD699A08'를 gpg-id라고 부른다.
생성한 key pair의 ID다.

## pass 활성화

gpg-id를 이용해서 pass를 활성화시킨다.

    $ pass init BD699A08

gpg-id로 pass를 시작하면 pass는 앞으로 해당 gpg-id의 공개 키를 이용해서 모든 비밀번호를 암호화한다.
'~/.password-store/' 디렉토리가 생성되었으며 이곳에 암호화된 비밀번호를 '.gpg' 파일로 저장한다.
이제 pass를 이용해서 비밀번호를 관리할 수 있다.

# pass 사용하기

## 비밀번호 저장

jngsp@test.com 메일의 비밀번호를 저장하고 싶다면 아래와 같이 `insert` 명령을 사용한다.

    $ pass insert email/jngsp@test.com

    mkdir: created directory '/home/jngsp/.password-store/email'
    Enter password for email/jngsp@test.com:myemailpassword
    Retype password for email/jngsp@test.com:myemailpassword

    $ pass

    Password Store
    └── email
        └── jngsp@test.com

email 디렉토리 밑에 jngsp@test.com 계정의 비밀번호가 저장되었다.
pass 명령으로 해당 계정을 호출하면 비밀번호가 출력된다.
탭 키를 이용해서 자동 생성이 가능하므로 편리하다.

    $ pass email/jngsp@test.com
    myemailpassword

비밀번호가 화면에 노출되는 것도 꺼려진다면 `-c` 옵션을 사용할 수 있다.
비밀번호를 화면에 출력하는 대신에 클립보드로 복사해준다.
클립보드에 복사된 비밀번호는 45초 동안 유효하며, 시간이 지나면 클립보드에서 사라진다.

    $ pass -c email/jngsp@test.com

    Copied cadb to clipboard. Will clear in 45 seconds.

## 비밀번호 생성

애초에 새 계정을 만들 때부터 pass를 이용해서 비밀번호를 생성할 수도 있다.
`generate` 명령을 사용하면 원하는 길이의 강력한 암호를 만들어주고, 자동으로 저장한다.

    $ pass generate heroku-for-microsite 16

    The generated password for heroku-for-microsite is:
    NhZypm~N&'3#X`p4

    $ pass

    Password Store
    ├── email
    │   └── jngsp@test.com
    └── heroku-for-microsite

'NhZypm~N&'3#X`p4'라는 16자리 암호를 생성하고 바로 저장하였다.
생성할 때도 화면에 출력하지 않고 클립보드로 바로 복사가 가능하다.

    $ pass generate -c ci-tool 16

    Copied ci-tool to clipboard. Will clear in 45 seconds.

    $ pass

    Password Store
    ├── ci-tool
    ├── email
    │   └── jngsp@test.com
    └── heroku-for-microsite

## 비밀번호 외의 정보

pass에 비밀번호만 저장해야 하는 것은 아니다.
`-m` 옵션을 사용하면 여러 줄의 텍스트를 저장할 수 있다.

    $ pass insert -m corporate-credit-card

    Enter contents of corporate-credit-card and press Ctrl+D when finished:

    0898
    name: TEST CO.LTD
    number: 4876-9872-2938-1024
    cvv: 287

이렇게 여러 줄을 입력한 경우에는 `-c` 옵션으로 호출했을 때, 첫번째 줄만 클립보드로 복사하므로 비밀번호를 가장 위에 적는 것이 편하다.
나머지 정보에 대해서는 조직 내에서 합의된 규칙을 만들어도 좋다.
사용하는 외부 서비스가 많다면 서비스 계정 이름이나 사용 규칙 등을 상세하게 적어서 관리할 수도 있다.

# git으로 pass 관리하기

pass는 [git](https://git-scm.com/)을 지원한다.
물론 '~/.password-store/' 디렉토리를 git으로 관리하는 비교적 쉬운 일이지만, pass 자체 명령어를 사용하면 더 간단하게 git을 사용할 수 있다.

    $ pass git init
    Initialized empty Git repository in /home/jngsp/.password-store/.git/

remote repository와 연동하면 팀원들과 pass 계정 정보를 공유할 수 있다.

    $ pass git remote add origin git@github.com:testcom/pass-store.git
    $ pass git push -u origin master

일단 git과 연결되면, pass의 정보가 바뀔 때마다 커밋이 자동으로 이루어진다.
pass git push, pass git pull 등을 사용해서 업데이트 한다.

## 팀원과 공유하기

pass는 여러 개의 gpg-id를 지원한다.
하나의 비밀번호를 여러 개의 공개 키로 동시에 암호화시킬 수 있다.
따라서 팀원 중 누군가가 새로운 비밀번호를 저장하면 pass는 팀원 전체의 공개 키들로 비밀번호를 암호화한다.
예를 들어 팀원이 10명이라면, 10개의 공개 키를 동시에 사용하여 새로 저장된 비밀번호를 암호화시킨다.
유의할 점은 서로 다른 공개 키로 암호화된 파일 10개가 따로 생기는 것이 아니라 10개의 공개 키를 한꺼번에 사용하여 암호화된 파일을 하나만 생성한다는 점이다.
저장한 비밀번호가 1개라면 팀원 수와는 상관없이 1개의 암호화된 파일만 생성된다.
이 암호화된 파일이 pass 디렉토리에 저장되며 git repository로 공유된다.

암호화시킬 때 사용했던 공개 키와 짝을 이루는 비밀 키 중에서 하나만 있으면 비밀번호는 복호화 가능하다.
gpg 키를 생성할 때 저장된 비밀 키는 오직 키를 생성한 주인만 가질 수 있다.
따라서 10명의 팀원 각각은 팀원 모두의 공개 키(10개)와 자기 자신의 비밀 키(1개)를 가지고 있어야 한다.
팀원 모두의 공개 키로 비밀번호를 암호화시키고, 비밀번호를 복호화할 때는 자신의 비밀 키를 사용한다.

pass는 비밀번호를 암호화시키거나 복호화시킬 때 사용할 gpg-id를 '~/.password-store/.gpg-id' 파일에 저장해둔다.
이 곳에 자신의 gpg-id가 없다면 그 팀원은 git repository를 복사할 수 있어도 비밀번호를 복호화시킬 수 없다.
즉, git repository가 해킹 당해도 gpg-id의 비밀 키를 모르면 저장된 비밀번호를 볼 수 없다.

따라서 팀 전체가 사용하는 pass 계정은 팀원 모두의 gpg-id를 알고 있어야 한다.
또한 모든 팀원은 각 gpg-id의 공개 키를 '~/.gnupg/'에 저장하고 있어야 한다.
단순히 git repository를 복사해서 공유하는 것만으로는 비밀번호를 암호화하거나 다시 복호화시킬 수 없다.

![public key cryptography](/img/posts/2017-04-27-how_to_manage_passwords_for_your_team/800px-Orange_blue_public_key_cryptography_en.svg.png)

(그림 출처: [wikimedia](https://commons.wikimedia.org/wiki/File:Orange_blue_public_key_cryptography_en.svg))

## 공개 키 공유하기

공개 키를 공유하는 방법에는 여러가지가 있지만, 키 서버를 사용하는 것이 가장 편하다.
키 서버란 모든 사람들의 공개 키를 저장해둔 서버다.
공개 키를 키 서버에 저장해두면, 특정 개인에게 암호화된 메세지를 보내고 싶을 때 서버에 저장된 키를 사용할 수 있도록 도와준다.
팀원 전체가 각자의 공개 키를 키 서버에 저장해두면 팀원 전체가 공유하기 쉽다.

키 서버에 공유하기 전에 공유할 키의 gpg-id를 확인한다.
`--list-secret-keys` 옵션을 사용하면 현재 저장되어 있는 비밀 키를 볼 수 있다.

    $ gpg2 --list-secret-keys

    /home/jngsp/.gnupg/pubring.kbx
    -------------------------------
    sec   rsa2048/BD699A08 2017-04-27 [SC]
    uid         [ultimate] jngsp <jngsp@test.com>
    ssb   rsa2048/E716C901 2017-04-27 [E]

비밀 키를 가지고 있는 gpg-id('BD699A08')를 찾아서 짝을 이루는 공개 키를 공유해야 한다.
키 서버는 몇 개가 있는데 [MIT PGP Public Key Server](https://pgp.mit.edu/)를 주로 사용한다.
아래와 같이 'pgp.mit.edu'에 공개 키를 공유한다.

    $ gpg2 --keyserver pgp.mit.edu --send-key BD699A08

    gpg: sending key BD699A08 to hkp://pgp.mit.edu

모든 팀원은 자신의 gpg-id로 키를 키 서버에 공유해야 한다.
그리고 자신 외의 모든 팀원들의 키를 키 서버에서 공유받아야 한다.

## 공개 키 가져오기

아래와 같이 동료의 키를 키 서버에서 공유 받는다.

    $ gpg --keyserver pgp.mit.edu --recv-key D83EB3C5

    gpg: key D83EB3C5: public key "Box Whisker <bw@boxnwhis.kr>" imported
    gpg: Total number processed: 1
    gpg:               imported: 1

저장된 공개 키 리스트를 보면 동료의 키가 추가된 것을 알 수 있다.

    $ gpg2 --list-keys

    /home/jngsp/.gnupg/pubring.kbx
    -------------------------------
    pub   rsa2048/BD699A08 2017-04-27 [SC]
    uid         [ultimate] jngsp <jngsp@test.com>
    sub   rsa2048/E716C901 2017-04-27 [E]

    pub   rsa2048/D83EB3C5 2017-04-27 [SC]
    uid         [ unknown] Box Whisker <bw@boxnwhis.kr>
    sub   rsa2048/A9CD6AD3 2017-04-27 [E]

가져온 키는 바로 쓸 수 없고, 신뢰 수준을 조정해야 한다.

    $ gpg2 --edit-key D83EB3C5

    gpg> trust
    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y

    gpg> q

## 새로운 동료와 공유하기

새로운 팀원의 입장에서는 기존 팀원 중 누군가가 자신을 pass에 포함시켜 주기를 기다리는 것 말고 할 일이 없다.
새로운 동료를 포함시키기 위해서는 새로운 동료의 gpg-id를 pass에 추가해야 한다.

    $ pass init BD699A08 D83EB3C5

    Password store initialized for BD699A08, D83EB3C5

    [master 0f2f059] Set GPG id to BD699A08, D83EB3C5.
     1 file changed, 1 insertion(+)

    ci-tool: reencrypting to C7505C45A9CD6AD3 D4F57D4EE716C901
    email/jngsp@test.com: reencrypting to C7505C45A9CD6AD3 D4F57D4EE716C901
    heroku-for-microsite: reencrypting to C7505C45A9CD6AD3 D4F57D4EE716C901
    corporate-credit-card: reencrypting to C7505C45A9CD6AD3 D4F57D4EE716C901

    [master 40f16d2] Reencrypt password store using new GPG id BD699A08, D83EB3C5.
     4 files changed, 0 insertions(+), 0 deletions(-)
     rewrite ci-tool.gpg (100%)
     rewrite corporate-credit-card.gpg (100%)
     rewrite email/jngsp@test.com.gpg (100%)
     rewrite heroku-for-microsite.gpg (100%)

새로운 gpg-id를 추가하려면 기존에 포함되어 있는 gpg-id도 포함하여 pass를 다시 설정해준다.
위의 결과를 보면 기존에 저장되어 있던 비밀번호들이 새로운 공개 키를 이용해 다시 암호화된 것을 알 수 있다.
변경된 내용은 git repository를 업데이트하여 공유한다.

    $ pass git push

    Counting objects: 14, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (10/10), done.
    Writing objects: 100% (14/14), 3.61 KiB | 0 bytes/s, done.
    Total 14 (delta 2), reused 0 (delta 0)
    remote: Resolving deltas: 100% (2/2), completed with 1 local object.
    To https://github.com/Jangsea/pass-store.git
       5138d82..40f16d2  master -> master

이제 새 동료는 git repository를 복사하여 비밀번호에 접근할 수 있다.
새 동료 역시 다른 동료들의 공개 키를 키 서버에서 공유 받아야 새로운 비밀번호를 pass에 추가할 수 있다.

## 서로 다른 보안 수준 반영하기

팀이 커지다 보면, 특정 비밀번호는 몇몇의 팀원들만 공유해야 할 필요가 생긴다.
예를 들어, RED와 BLUE로 구분된 보안 수준이 있다면 각 보안 수준에 따라 다른 구성원들만 포함시키고 싶다.
이럴 때는 pass에 하위 디렉토리를 만들고, 각 하위 디렉토리마다 서로 다른 gpg-id를 지정할 수 있다.

    $ pass init -p RED BD699A08

    mkdir: created directory '/home/jngsp/.password-store/RED'
    Password store initialized for BD699A08
    [master e17fd10] Set GPG id to BD699A08.
     1 file changed, 1 insertion(+)
     create mode 100644 RED/.gpg-id

이제 '/home/jngsp/.password-store/RED' 디렉토리가 생성되었고, 'RED/.gpg-id' 파일에는 gpg-id, 'BD699A08'만 저장되어 있다.
즉, RED 디렉토리에 저장되는 모든 비밀번호는 gpg-id, 'BD699A08'만 복호화 가능하다.

## 개인 비밀번호 관리하기

pass에 개인용 비밀번호를 저장하면 git을 통해 전체 팀원에게 공유된다.
물론 팀원들이 이를 복호화할 수는 없지만, 바람직한 상황은 아니다.
이런 경우에는 .gitignore 파일에 '/private' 등을 추가하고 전체 팀 규칙으로 설정하면, 팀원 각자가 개인용 비밀번호를 따로 관리할 수 있다.
[1password](https://1password.com/) 등의 서비스를 굳이 사용할 필요가 없다.
특히 pass는 cli 기반이라 아주 편하다.

# .pem 파일 관리

AWS를 자주 사용하다 보면, .pem 파일이 쌓이는데 이 역시 pass로 관리 가능하다.
결국 .pem 파일도 텍스트이므로 `-m` 옵션으로 .pem 내용을 통째로 암호화하여 저장할 수 있다.

    $ pass insert -m pem/test.pem < test.pem

    Enter contents of pem/ga-climber-test.pem and press Ctrl+D when finished:

    [master 726f816] Add given password for pem/test.pem to store.
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 pem/test.pem.gpg

저장된 .pem 파일은 암호화되어 git repository로 공유된다.
필요할 때 꺼내 쓰기 편하다.

    $ pass pem/test.pem > another-test.pem
    $ diff test.pem another-test.pem  # there is nothing different

# 정리

pass를 이용하면 비밀번호 관리를 편리하게 할 수 있다.
git remote repository를 이용하면 팀원과 공유도 쉽다.
gpg-id와 비대칭키 암호화를 이해할 필요가 있다.
공개 키와 비밀 키가 하나의 짝을 이루고, 이 짝을 gpg-id로 부른다.
암호화시킬 때는 공개 키를 사용하고, 암호를 풀 때는 비밀 키를 사용한다.
개별 팀원은 모든 팀원의 공개 키를 모두 알아야 한다.

텍스트 형태의 정보는 무엇이든 저장할 수 있으므로 응용할 방법이 무척 많다.
더 자세한 사용 예시는 아래 글을 참고한다.

*   [SIMPLE EXAMPLES](https://git.zx2c4.com/password-store/about/#SIMPLE EXAMPLES)
