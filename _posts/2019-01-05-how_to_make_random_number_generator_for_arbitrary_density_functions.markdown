---
layout: post
title: 임의의 확률 분포를 따르는 난수 생성기 만들기
author: 박장시
brief: 임의의 분포를 따르는 난수 생성기를 만드는 방법에 대해 설명합니다
date: 2019-01-05
---

‘[특정 확률 분포를 따르는 난수 생성기 만들기](/2017/04/13/how_to_make_random_number_generator_for_any_probability_distribution.html)‘에서는
누적 분포 함수([cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) 이하 ‘CDF’)가
알려진 확률 분포에서 난수를 추출하는 방법에 대해서 설명하였다.
이 글에서는 [CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function)의
역함수를 알 필요 없이, 임의로 만든 분포 함수에 대해서 난수를 생성하는 방법에 대해서 설명한다.

# 테스트를 위한 모방
잘 만든 코드를 테스트하기 위해서 현실을 모방할 때가 많다.
예를 들어, 어떤 서비스를 방문하는 고객 로그를 분석하는 프로그램을 만들었다면 테스트를 위해 실제 로그가 필요하다.
실제 로그를 충분히 사용할 수 없거나, 실제 로그만으로는 테스트가 부족할 때는 있을 법한 로그를 생성한다.

이미 잘 정의된 확률 분포를 사용하면 가상의 데이터를 만드는 일은 수월하다.
대부분의 프로그래밍 언어는 [잘 알려진 확률 분포]((https://en.wikipedia.org/wiki/Probability_distribution#Common_probability_distributions))의
난수 생성기를 [제공](https://docs.scipy.org/doc/scipy/reference/stats.html)한다.
혹시 원하는 확률 분포의 난수 생성기가 없다면 [CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function)의
역함수를 이용해 만들 수 있다(참고: ‘[특정 확률 분포를 따르는 난수 생성기 만들기](/2017/04/13/how_to_make_random_number_generator_for_any_probability_distribution.html)’).

문제는 어떤 확률 분포를 사용해야 하는지 잘 모를 때다.
사용할 확률 분포를 결정하더라도, 적절한 모수를 정하기 어렵다.
개발 하기도 바쁜데 테스트에 사용할 확률 분포를 고르고 그럴듯한 모수를 정해야 한다.
이렇게 복잡한 과정을 거치기 보다, 경험적으로 잘 아는 분포 모양을 대충 그려서 데이터를 발생시키고 싶다.

# 임의의 확률 분포
아주 단순한 예시로 웹 사이트 방문 로그의 시간 간격을 만들어보자.
이런 경우 지수 분포를 사용하지만, 이를 잘 모르거나 모수를 정하기 어렵다면 경험적으로 알고 있는 함수를 분포로 쓸 수 있다.

경험적으로 어떤 웹 사이트의 방문 주기는 1분 내에 `20`, 2분 내에 `15`, 3분 내에 `8`, 4분 내에 `3`, 1분 내에 `1`의 비율로 발생한다고 하자.
여기서 `20`, `15`, `8`, `3`, `1`의 숫자 자체는 중요하지 않다.
다만, 1분과 5분의 차이가 20배라는 비율 차이가 중요하다.
이 숫자들에 모두 100을 곱해서 `2000`, `1500`, `800`, `300`, `100`으로 표현해도 같다.
상대적인 크기가 중요하다.

![non-normalized distribution function]()

이를 그래프로 표현하면 위와 같다. 확률 분포 함수는 모든 확률을 더해서 꼭 1이 되어야 하지만, 난수 생성을 위해서 이 성질은 필요없다.

```python
def target_func(x):
    func_dict = {1: 20, 2: 15, 3: 8, 4: 3, 5: 1}
    try:
        y = func_dict[x]
    except KeyError:
        print('x have to be integer between 1 and 5')
        raise
    return y
```

난수를 발생시키고 싶은 확률 분포 함수를 ‘목표 함수’라고 표현한다.


# 참고

1. 일반적인 [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling)에서는
‘target density’ 외에 ‘candidate function’을 명시한다.
위의 예에서는 이를 균등 분포로 정하여 단순하게 구현하였다.
이 아이디어는 ‘[An introduction to rejection sampling](https://youtu.be/kYWHfgkRc9s)’ 강의에서 얻었다.

2. 이 글은 아래의 자료를 참고하여 작성하였다.
    * [Advanced Statistical Computing / Ch6.3 Rejection Sampling](https://bookdown.org/rdpeng/advstatcomp/rejection-sampling.html)
    * [An introduction to rejection sampling](https://youtu.be/kYWHfgkRc9s)
    * [Rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling)
    * [Pseudo-random number sampling](https://en.wikipedia.org/wiki/Pseudo-random_number_sampling)
