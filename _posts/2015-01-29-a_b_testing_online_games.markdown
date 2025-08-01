---
layout: post
title: "온라인 게임에서의 A/B 테스팅"
author: 강규영
brief: "온라인 게임에서 A/B 테스팅을 하는 방법을 살펴본다"
date: 2015-01-29
---
온라인 게임에서 A/B 테스팅을 하는 방법, 주의할 점, 점진적으로 테스팅을 도입하는 전략, A/B 테이스팅의 단점들에 대해 생각하는 바를 정리해보았다. A/B 테스팅
개념에 대한 설명은 [A/B 테스팅이란](/2015/01/29/a_b_testing.html)을 참고하기 바란다.


# 게임에서의 A/B 테스팅

전통적으로 A/B 테스팅이라고 하면 주로 아래와 같은 것들을 떠올린다:

*   가입이나 구매 버튼의 위치, 색상, 문구 등을 바꿔보기
*   이메일 메시지나 푸시 메시지의 제목/본문을 바꿔보기
*   회원 가입 양식, 주문 양식 등에서 각종 필드의 순서나 필수여부 등 바꿔보기
*   사이트 네비게이션 UI 구성이나 레이블 바꿔보기
*   상품 배치나 종류 바꿔보기

게임에서도 위에 나열된 범주에서 A/B 테스팅을 수행할 수 있겠지만 이런 것들은 게임의 핵심적인 요소라고 보기 어렵다. 물론 UI 디자인, 마케팅, 아이템 판매 등도
중요하겠지만 게임이라고 한다면 핵심은 "재미"가 아닐까. **무엇이 더 재미있는가**에 대한 A/B 테스팅을 할 수 있어야 게임에서의 A/B 테스팅이라고 말할 수 있을
것이다.

이를테면 다음과 같은 것들을 생각해볼 수 있겠다:

*   아이템 드랍률이 적절한가
*   스테이지별 난이도가 적절하게 증가하는가
*   특정 인던의 난이도가 지나치게 쉬운가
*   레벨 디자인의 특정 요소가 플레이어로 하여금 기대한 행동을 하도록 잘 유도하는가
*   몹이 리스폰되는 장소나 간격이 적절한가
*   몬스터 AI가 지나치게 똑똑한가
*   플레이어 실력 평가 및 매치매이킹 알고리즘이 적절한가
*   새로 기획한 유료 아이템의 성능이 지나치게 좋지는 않은가

이 중에서 "스테이지별 난이도가 적절하게 증가하는가"라는 문제를 좀 더 구체적으로 생각해보자.

총 10개의 스테이지가 있다. 스테이지 1에서 시작해서 순차적으로 진행하여 스테이지 10을 클리어하면 게임이 끝난다고 치자.각 스테이지 n에 대하여 \( n ^ 2 \)
시간만큼이 소요되게 하는 것이 디자이너의 의도였다. 즉 스테이지 1에서는 1시간, 스테이지 2에서는 2시간, 스테이지 3에서는 4시간, ... 스테이지 10에서는
1024시간이 걸려야 한다.

로그를 분석해보니 나머지 스테이지는 의도대로 구현이 되었는데, 스테이지 3에 플레이어들의 평균 체류 시간이 예상했단 4시간 보다 33분 높은 4시간 33분이었다고
치자.

스테이지 3의 난이도를 낮추는 패치를 적용하고 이에 대한 A/B 테스트를 아래와 같이 수행할 수 있을 것이다.

*   이미 스테이지 3에 머물고 있던 플레이어들에게는 패치를 적용하지 않는다.
*   패치가 적용된 후 스테이지 3에 진입한 플레이어 중 90%는 A 집단, 나머지 10%는 B 집단으로 배정한다.
*   A 집단에는 패치를 적용하지 않는다.
*   B 집단에는 패치를 적용한다.

A 집단에 비해 B 집단의 평균 체류 시간이 낮아졌다면 패치의 방향이 적절했다고 볼 수 있다. 원하는 결과를 얻었으면 패치를 전체 집단에게 적용하면 된다.

이때 몇 가지 주의할 점이 있다.

우선, 모든 패치는 잘못될 가능성이 있다. 이를테면 체류 시간이 2시간으로 줄어버린다거나 하는 식으로 난이도가 지나치게 하향되거나, 예상치 못했던 이유로 인해
오히려 난이도가 상향될 수 있을 것이다. 따라서 실험군과 대조군을 1:1 비율로 나누기 보다는 1:9와 같이 편향되게 나누는 것이 안전하다.

두번째 고려할 점은 난이도 조절 방식이다. 예를 들어 스테이지 3 보스의 HP를 10% 낮추어 난이도 하향을 했다고 치자. 하지만 보스의 HP는 UI 상에 표시되는
요소이기 때문에 플레이어들이 이를 쉽게 인식할 수 있다. 게다가 각종 커뮤니티를 통해 캡쳐화면을 올리며 "아무개는 보스 HP가 10% 낮더라"는 사실을 공유할 수도
있다. 플레이어들이 실험에 대해 인지하고 자신이 어떤 집단에 속해 있는지 생각하기 시작하면 욕을 먹는 것은 물론이거니와, 실험에도 편향이 발생하게 된다.
블라인드 테스트(blind test)를 해야하는 이유이다. 이를테면 대놓고 HP를 수정하는 것 보다는 보스 AI를 조정하는 식으로 접근하는 것이 좋다.

(실험자가 피험자에게 영향을 미칠 소지가 있다면 이중맹검법(double-blind test)을 적용하는 것이 맞지만 온라인 테스트의 경우 고려하지 않아도 된다.)


# 테스트 서버

잠깐, 만약 테스트 서버가 있는 상황이라면 온갖 극단적인 실험들을 테스트 서버에서 비교적 안전하게 할 수 있지 않나? 뭐하러 저렇게 해야하나?

테스트 서버에서 플레이하는 플레이어들과 일반 서버에서 플레이하는 플레이어들은 균일한 집단이 아닐 가능성이 매우 높다. 이와 비슷하게 "실험적 패치가 있습니다.
미리 체험해보시겠습니까?"라는 식으로 물어보는 방식도 실험 설계라는 관점에서는 적절하지 못한데, 도전을 즐기는 성향의 플레이어들만 편향적으로 실험에 참가하게
되기 때문이다.

즉, 임의적 추출(random selection)이 이루어지지 않을 가능성이 높기 때문에 이 방식으로 테스트를 할 경우 테스팅의 결과를 일반화하기 어렵다.


# Verification, Validation

A/B 테스팅을 통해 안전하게 그리고 확신을 갖고 패치를 적용할 수 있게 되었다. 그럼 이제 이 방식을 계속 반복하면 되는건가? 생각해야할 문제가 몇 가지 더 있다.

좀 전의 A/B 테스팅은 "(패치가) 디자이너의 의도대로 되었는가?"라는 질문에 대한 답을 주었다. 하지만 또다른 중요한 질문이 남아있다. "디자이너의 의도가
올바른가?"라는 질문을 던져야한다. 소프트웨어 공학에서 말하는
[Verification and Validation](http://en.wikipedia.org/wiki/Verification_and_validation_(software)) 문제이다. Barry Boehm의
표현을 빌자면 다음 두 질문으로 요약할 수 있다:

*   Verification: Are we building the product right? (우리가 제품을 맞게 만들었는가?)
*   Validation: Are we building the right product? (우리가 맞는 제품을 만들었는가?)

조금 전의 난이도 패치 사례에 맞게 고쳐보면 아래와 가다:

*   Verification: 패치로 인해서 스테이지 3의 체류시간이 4시간에 맞춰졌는가?
*   Validation: 스테이지 3의 체류시간이 4시간이어야 게임이 가장 재미있어지는가?

예를들어 스테이지 10을 생각해보자. 디자이너의 의도에 의하면 스테이지 10을 클리어하기 위해서는 1024시간 동안 플레이를 해야한다. 주말도 쉬지 않고 하루
8시간씩 약 네 달을 달려야만 클리어가 가능하다. 개막장 하드코어 인생 퇴갤 게임을 만들고 싶은게 아니라면 분명 문제가 있다. 의도대로
구현되었는가(verification)보다 의도 자체가 올바른가(validation)가 훨씬 중요해보인다.

스테이지 10의 체류시간이 어느 정도여야 게임이 가장 재미있을까?

재미라는 것은 직접 측정하기 쉽지 않으니 재미와 관련이 있을 것으로 보이는 지표 중 측정이 가능한 후보들을 찾아야 한다. 이를테면 각 스테이지별
포기율(abandonment rate)도 괜찮은 후보 중 하나일 것이다. 해당 스테이지에 진입한 플레이어 수를 해당 스테이지를 클리어하지 못한 플레이어 수로 나눈
값을 포기율로 정의할 수 있을 것이다. 예를 들어 스테이지 1에 진입한 100명 중 10명이 스테이지 1을 클리어하지 못하고 게임을 중단했다면 스테이지 1의 포기율은
0.1, 즉 10%이다. "중단" 혹은 "이탈"을 무엇으로 정의할지도 고민을 해야하는데 이에 대해서는 다음 글들을 참고하자:

*   [이탈 기준 정하기](/2014/09/15/make_a_criterion_for_churn.html)
*   [개별 사용자를 고려한 이탈 측정하기](/2014/11/11/measure_churn_for_individual_users.html)

이제 포기율을 측정할 수 있게 되었다. 포기율이 높으면 해당 스테이지가 지나치게 어려워서 재미가 덜할 것이라고 가정하자.

그 다음 단계는 패치 예시와 동일하다. A/B 테스트를 진행하며 포기율이 낮아지는 방향으로 점진적으로 패치를 하는 것이다.

물론 이 예시에는 문제가 있다. 위와 같은 방식으로 포기율을 정하고 이걸 "재미"에 대한 간접 지표로 사용한다면 각 스테이지가 1초만에 클리어되는 게임이 가장
재밌는 게임이다. 사실 플레이어 혹은 사용자가 얼마나 긍정적으로 참여하고 있는가 - positive engagement - 를 측정하는 것은 쉽지 않은 문제이다. 예를들어
"오토"를 켜놓고 꾸벅꾸벅 졸며 플레이하는 모습을 흔히 볼 수 있는데, 이게 정말 재미있는 것인지, 올바른 것인지에 대한 고민을 하기 시작하면 끝이 없다. 하지만
게임 업계 종사자라면 고민하지 않을 수 없는 문제이기도 하다. 이에 대해서는 별도의 글이 필요할 것 같다.

다시 현실로 돌아와서 이 섹션(validation 문제)에 대해 소결론을 내리자면, 단순한 포기율 측정과 "진정한 재미"를 측정하는 것 사이에는 수많은 점진적 단계들이
있다는 것이다. 진정한 재미를 측정할 수 없으니 포기율이나 보고 말아야지 혹은 진정한 재미를 측정할 수 없으니 다 의미없구나 등등은 별로 생산적이지 못한 생각이다.
"진정한 재미"는 아니지만 포기율보다는 똑똑한 지표를 각 게임의 상황에 맞게 얼마든지 찾아낼 수 있다.


# 기존 플레이어와 신규 플레이어

또 다른 문제에 대해 생각해보자.

더 효율적인 HUD UI에 대한 아이디어가 떠올랐다고 치자. 이 HUD UI를 도입하면 등 뒤에 있는 적들의 위치를 더 빠르게 파악할 수 있을 것으로 기대한다. A/B
테스팅을 해보면 좋을텐데, 위와 동일한 방식으로 하면 될까? (후방에 있는 적에 의해 HP가 소모된 양을 측정하면 평가 지표로 쓸 수 있을 것 같다)

의식적이건 무의식적이건 새로운 UI에는 학습 비용이 있다는 점을 고려해야 한다. 기존 HUD에 익숙한 플레이어들은 일시적으로 퍼포먼스가 떨어질 수 있다.

UI 자체는 개선된 것이 맞지만 학습 비용 때문에 일시적으로 퍼포먼스가 떨어진 것인지, UI 자체가 문제인지 알아내려면 테스트 결과를 평가할때 기존 플레이어와 신규
플레이어를 나누고 신규 플레이어 중에서 A 집단과 B 집단의 차이를 비교하면 UI 자체가 개선되었는지 여부를 알 수 있을 것이다.


# 게임 디자인에 통합하기

앞에서 살펴본 바와 같이, 플레이어가 인지하기 어려운 범주 내에서만 테스팅을 하려고 하면 제약이 크다. 이 문제를 완화할 수 있는 좋은 방법 중 하나는 디자인
단계에서부터 테스트를 고려하는 것이다.

이브 온라인(EVE online)은 2009년 Apocrypha 패치에서 "웜홀"이라는 개념을 도입했다. 웜홀에는 여러 종류가 있는데 몇몇 종류는 이미 알려진 두
공간(k-spaces) 사이를 이어주는 역할을 하고, 몇몇 종류는 알려지지 않은 공간(w-spaces)으로 진입하는 통로 역할을 한다. 그리고 웜홀은 구조적으로 불안정하기
때문에 일정 시간이 지나거나, 웜홀을 통해 지나치게 많은 물질(mass)이 통과하면 닫혀버린다.

이브 온라인의 디자이너가 어떤 의도를 가지고 이런 시스템을 설계했는지 알 수 없으나, 마음놓고 여러가지 실험을 할 수 있는 대단히 좋은 장치이다. 일단 지나치게
많은 물질이 통과할 수 없다는 제약으로 인해 게임 내 경제에 미치는 영향을 안전하게 제한할 수 있고, 시간이 지나면 닫힌다는 제약으로 인해 일시적인 아이디어나
새로운 밸런스 등을 자주 테스트해볼 수 있다.

MMORPG가 아니더라도 여러 아이디어를 생각해볼 수 있다. MORPG(방게임)에서 랜덤맵을 골랐을 때 공식적으로 선택할 수는 없는 실험적인 맵이 낮은 빈도로
나온다거나(레벨 디자인 테스트), 영화 헝거 게임에서 스폰서가 보내주는 아이템 상자(!)처럼 일회성으로 사용할 수 있는 새로운 실험적 아이템 같은 것이 하늘에서
간혹 떨어진다거나 하는 식으로 게임 디자인 자체에 실험을 용이하게 해주는 개념들을 녹여 넣으면 좋을 것이다.


# 점진적 도입 전략

그럴듯한 이야기들인데 막상 적용하려고 하면 항상 시간과 비용이 문제다. 다음 방법들을 추천한다.

첫째, 테스팅을 하려면 측정이 선행되어야 하는데 직접 수집 기능을 구현하기 보다는 구글 애널리틱스를 사용할 것을 추천한다. 월 1천만 건의 데이터가 넘지 않는다면
무료로 쓸 수 있다. 1천만 건을 넘는다면 데이터를 샘플링하여 보내는 방식으로 여전히 무료로 쓸 수 있다. 구글 애널리틱스에서 제공하는 SDK(analytics.js,
iOS SDK, Android SDK 등)를 쓴다면 해당 SDK에서 샘플링을 할 수 있다. Measurement Protocol을 직접 구현하는 경우라면
[해시 기반 샘플링](/2014/12/13/Hash-based_sampling.html)을 참고하여 구현하면 된다.

구글 애널리틱스로 게임 데이터를 분석하는 방법에 대해서는 다음 글을 참고하기 바란다:

*   [구글 애널리틱스로 게임 분석하기 1](/2014/09/15/analyze_game_using_ga_1.html)
*   [구글 애널리틱스로 게임 분석하기 2](/2014/11/08/analyze_game_using_ga_2.html)

둘째, 그래픽 에셋이나 UI를 건드리는 테스트보다는 각종 수치(확률 테이블, 능력치 테이블 등) 혹은 알고리즘을 건드리는 테스트와 같이 글자 몇 개만 바꾸면 빠르게
해볼 수 있는 테스트를 먼저 시도하는 식으로 낮은 과일을 먼저 따먹고(성과를 내고), 점진적으로 확장하는 방식으로 접근하면 좋을 것이다.

셋째, 실제 테스트를 진행하려면? 역시나 구글 애널리틱스를 추천한다. Measurement Protocol, Content Experiments API 등을 활용하면 간단하게
테스트를 수행하고 결과를 평가해볼 수 있다.

넷째, 서버측이 아니라 클라이언트측에서 테스트에 따른 변화를 처리해야한다면? 테스트를 할 때마다 앱스토어에 다시 승인을 받으려면 답이 없다. Google Tag
Manager SDK를 활용하면 재승인 없이 테스트와 관련된 각종 설정 데이터를 클라이언트로 재배포할 수 있다. 특히 구글 애널리틱스와 연동이 잘 되기 떄문에
더욱 좋다.

이런 시도들로 작고 빠르게 성공 사례를 만들고 경험을 쌓은 후에 자체적인 테스트 플랫폼을 구축하거나 좀 더 고도화하는 방식이 안전할 것이다.
