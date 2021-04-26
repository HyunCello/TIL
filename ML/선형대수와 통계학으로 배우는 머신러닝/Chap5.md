# 5.1 컨벡스 셋

## 5.1.1 직선과 선분

### 직선

시작과 끝이 존재하지 않음

### 선분

시작과 끝 존재

### $y = wx_1 + (1-w)x_2$

위 식에서 $w = 0$이면 $y=x_2$, $w = 1$이면 $y=x_1$

if) $0≤w≤1$ → $x_1,x_2$간의 선분

     $w \in \R$        → 직선 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca9ccc1c-f9f5-403f-bfd1-ab258c3fc207/_2021-04-03__11.33.38.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca9ccc1c-f9f5-403f-bfd1-ab258c3fc207/_2021-04-03__11.33.38.png)

$w$는 가중치라고 생각할 수 있음

직선에는 $w$값의 제한이 없기 때문에 

0 보다 작은 음수 값을 가질 수도 있고, 1보다 큰 값을 가질 수도 있다

## 5.1.2 아핀 셋

### 아핀 셋(affine set)

집합 C 내부의 두 점을 잇는 직선이 있다고 했을 때,

$wx_1 + (1-w)x_2 \in C$ 를 만족하면

집합 C : 아핀 셋(affine set)

⇒ 두 점을 잇는 직선은 집합 C에 포함되어야 한다는 뜻

⇒ w값의 제한 이 없다 = 직선

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d2cebb9-e63a-421d-bbae-0b875038e474/_2021-04-03__11.40.38.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d2cebb9-e63a-421d-bbae-0b875038e474/_2021-04-03__11.40.38.png)

그림 5-2 아핀 셋

회색 영역 : 아핀 셋

시작과 끝 범위 제한이 없는 직선을 포함

⇒ 아핀 셋 또한 범위 제한이 없음

### 아핀 조합(affine combination)

n차원으로 확장하면

$w_1x_1 + ... + w_nx_n$ 으로 쓸 수 있고

이 때 $w_1+...+w_n = 1$을 만족

⇒ 포인트 $x_1...x_n$에 대한 아핀 조합

아핀 조합은 곧 집합 C에 속하는 점들의 선형 결합과 같음

그리고 선형 결합 계수 w들의 합은 1을 만족

## 5.1.3 아핀 함수 vs 선형 함수

함수 $f : \R^n \rarr \R^m$ 이 존재한다고 할 때, f함수는 n차원에서 m차원으로 변환하는 함수

### $f : \R^n \rarr \R^m$

함수 $f$ 의 정의역(domain)을 $dom \ f$

함수 $f$ 의 의미 : n차원 공간 $\R^n$에 속하는 벡터를 m차원 공간 $\R^m$에 속하는 벡터로 변환한다는 뜻

함수 $f$ 가 선형 변환이라면 $n \times m$행렬로 나타낼 수 있으며, 이 행렬을 $W$라고 표현

### 선형 함수

$linear function : \ \ \ \ \ f(x) = Wx$

### 아핀 함수

$affine function: \ \ \  f(x) = Wx \ + \ b$

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cfde2f7-5986-4643-ab32-20beec433fd5/_2021-04-03__6.14.37.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cfde2f7-5986-4643-ab32-20beec433fd5/_2021-04-03__6.14.37.png)

그림 5-3 선형 vs 아핀

선형 변환은 원점을 지나가는 것을 볼 수 있음

아핀 부분의 경우 상수 b에 의해 y 절편이 존재하는 것을 볼 수 있음

## 5.1.4 컨벡스 셋

### 컨벡스 셋

집합 C 내부의 두 점 사이의 선분이 집합 C에 속한다면 집합 C는 컨벡스(convex) 한다

⇒ 두 점 $x_1, x_2 \in C$ 에 대해 $0≤ w ≤ 1$을 만족하는 $w$에 대해 아래 조건을 만족하면 집합 C를 컨벡스 셋 이라고 함

## $wx_1 + (1-w)x_2 \in C$

아핀 셋과 컨벡스 셋의 차이

두 점을 잇는 직선을 포함하는 아핀 셋과는 달리

컨벡스 셋은  두 점 사이의 선분을 포함한다는 것

컨벡스 셋은 볼록 집합이라고 번역됨

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59a20f16-d0b4-4f12-874e-0666b984b21c/_2021-04-03__8.53.15.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59a20f16-d0b4-4f12-874e-0666b984b21c/_2021-04-03__8.53.15.png)

그림 5-4 컨벡스 셋의 게념

왼쪽 그림은 컨벡스 셋, 오른쪽 그림은 컨벡스 셋 X

왼쪽 그림에서는 두 점 사이의 선분이 모두 원 내부에 속하지만, 오른족 그림은 두 점 사이의 선분 내부의 점이 모두 도형에 속하지는 X

### 아핀 셋이면 컨벡스 셋이다

why? 아핀 셋은 두 지점 사이의 모든 선을 포함하므로 자연스럽게 두 점 사이의 모든 선분 또한 포함

### 컨벡스 조합

아핀 조합과 비슷한 개념으로 컨벡스 조합(convex combination)이라는 개념도 존재

데이터 포인트 $w_1x_1 + ... + w_nx_n$이 존재할 때, 이를 $x_1...x_n$의 컨벡스 조합(convex combination)이라고 함

이 때, $w_1 + ... + w_n = 1$이며, $w_1,...,w_n > 0$을 만족해야 함

### 컨벡스 헐(convex hull)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/654e85b4-2347-4c97-b2a0-379b7eeff6f7/_2021-04-03__8.58.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/654e85b4-2347-4c97-b2a0-379b7eeff6f7/_2021-04-03__8.58.46.png)

컨벡스 셋이 집합 내부의 두 점 사이의 선분을 통해 컨벡스 여부를 알아보았다면,

반대로 컨벡스 헐은 주어진 점들을 포함하는 컨벡스 셋을 의미함

## 5.1.5 초평면과 반공간

### 초평면 (hyperplane)

## {${x|w^tx = b}$}

초평면이란.. $w^Tx = b$ 를 만족하는 데이터 포인트 x의 집합을 의미

이 때, w는 n차원 가중치 벡터, 즉 w $\in \R^n$이고, w ≠ 0이며, b는 1차원 스칼라값, 즉 b $\in \R$

이 떄, $w^T = b$ 는 벡터 w와 벡터 x를 내적한 값이 b라는 것을 의미함

여기서 내적값이 b가 아니라 0이라면 계산하기 편하다

## {${x|w^T(x-x_0) = 0}$}

이때, $x_0$은 초평면 내의 어떤 점도 가능하다

그림으로 그리면..

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8de36f48-e659-4943-ad73-0c52238796cc/_2021-04-04__2.01.42.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8de36f48-e659-4943-ad73-0c52238796cc/_2021-04-04__2.01.42.png)

그림 5.6

벡터 w는 벡터 ${\mathrm x}-{\mathrm x_0}$ 과 수직이므로 두 벡터를 내적했을 때 0이라는 것을 알 수 있음

## 반공간

전체 공간은 초평면(hyperplane)에 의해 반공간(halfspace)로 나뉨

초평면이 두 공간을 나누는 경계라고 생각하면, 반공간은 초평면으로 나뉜 공간의 일부분을 나타낸다고 볼 수 있음

### { $\mathrm {w^Tx} \le b$ }

반공간을 그림으로 표현하면?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82d483d1-7ae3-4fa2-91a9-b538147aafdd/_2021-04-04__2.24.26.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82d483d1-7ae3-4fa2-91a9-b538147aafdd/_2021-04-04__2.24.26.png)

그림 5-7

반공간 : 컨벡스 셋 O, 아핀 셋 X

아핀 셋이 되려면 공간의 제한이 없어야 하는데.. 반공간에는 경계가 존재한다

앞서 살펴본 초평면과 반공간은 서로 연관되어 있으며 머신러닝에서 분류, 회귀 문제를 풀 때 핵심적인 개념

여기서의 머신러닝의 목적은 전체 공간을 효과적으로 나눌 수 있는 초평면을 찾는 문제라고 할 수 있음

# 5.2 컨벡스 함수

## 5.2.1 컨벡스 함수의 개념

### 컨벡스 함수

함수 $f$의 정의역이 컨벡스 셋(convex set)이고, 모든 데이터 포인트 $x_1,x_2, 0≤ w ≤ 1$에 대해

$f(wx_1 + (1 - w)x_2 ≤ wf(x_1) + (1-w)f(x_2)$

를 만족하는 함수 $f : \R^n → R^m$을 컨벡스 하다고 함

위 부등식의 의미 : 

두 점 ($x_1,f(x_1)$), ($x_2,f(x_2)$) 사이의 선분이 함수 $f$의 그래프보다 위에 있어야 한다는 뜻

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e6eb8e2-7bd8-4d31-9ed8-46d6e448e5df/_2021-04-04__6.02.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e6eb8e2-7bd8-4d31-9ed8-46d6e448e5df/_2021-04-04__6.02.46.png)

만약 위 부등호에서 아래 식과 같이 등호가 없고 $0≤w≤1$이면 strictly 컨벡스 하다고 말한다

strictly convex를 해석하면 '순볼록'이라고도 함

$f(wx_1 + (1 - w)x_2 ≤ wf(x_1) + (1-w)f(x_2)$

### 컨벡스 & 콘케이브

어렸을 때 배웠던 2차 함수에서 볼록함수,오목함수를 생각하면 이해하기 쉬움

if) $-f$가 컨벡스하다면

$f$는 콘케이브 하다

if) $-f$가 strictly concave 하다

$f$는 strictly convex 하다 하고 말함

아핀 함수 : 컨벡스 조건 부등식을 만족하므로..

컨벡스 임과 동시에 콘케이브 함

⇒ 어떤 함수가 컨벡스하면서 콘케이브하다 ⇒ 아핀 함수

## 5.2.2 컨벡스 함수의 예

- 지수 함수
- 절댓값 함수
- 멱함수
- 멱함수
- 로그 함수
- Lp-Norm
- 지시 함수
- 최대 함수

## 5.2.3 1차, 2차 미분 조건

### 그래디언트(gradient)

1차 미분 조건(first-order condition)은 최적값을 찾는 데 중요한 역할을 함

함수 f가 미분 가능하다는 말은 함수 $f$의 정의역 내 모든 점에 대해,

해당 점의 미분값 즉, 그래디언트(gradient) $\nabla f$ 가 존재한다는 뜻

$f(x_2) ≥ f(x_1) + \nabla f(x_1)^T(x_2-x_1)$

f가 미분 가능하다고 할 때,

함수 f가 번벡스하다는 말은 곧 함수 $f$의 정의역이 컨벡스하며

위와 같은 부등식이 모든 점 $x_1,x_2$에 대해 만족하는 말과 같다

1차 미분 조건을 그림으로 표현하면 그림 5-9와 같음

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e66c4c0d-57b2-4f40-b604-5f0fcc1e494c/_2021-04-04__6.24.59.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e66c4c0d-57b2-4f40-b604-5f0fcc1e494c/_2021-04-04__6.24.59.png)

그림 5-9 1차 미분 조건

위 부등식이 의미하는 것은

컨벡스 함수에 대해 지역 정보(local information)를 유도할 수 있고

⇒ 이로부터 전역 정보(global information)를 유도할 수 있다

$\nabla f(x) = 0$

예를 들어, 위와 같이 그래디언트 값이 0일 때, 모든 $x_2 \in dom \ f$에 대해 $f(x_2) ≥ f(x_1)$이라면,

$x_1$은 함수 $f$에 대한 전역 최솟값(global minimizer)이다

why? 모든 지역에서 $f(x_2)$는 $f(x_1)$보다 크거나 같기 때문

### 헤시안 행렬(hessian matrix)

2차 미분 조건에 대해서 알아보자

만약 함수 $f$ 가 두 번 미분 가능해서 $\nabla^2 f$가 존재할 때,

함수 $f$의 정의역에 존재하는 모든 x에 대해

$\nabla^2 f(x) \ge0$ 이면 함수 $f$는 컨벡스하다

이는 $\nabla^2 f$의 헤시안 행렬이 준양정치행렬(positive semidefinite)

헤시안 행렬(hessian matrix)이란 아래와 같이 함수 $f$의 2차 미분계수를 이용해 만든 행렬을 의미

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ece24169-7d57-4953-b0ce-3cf0749ae0e9/_2021-04-04__10.23.59.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ece24169-7d57-4953-b0ce-3cf0749ae0e9/_2021-04-04__10.23.59.png)

## $\nabla^2 f(x)_{ij} = {{\partial f(\mathrm x)} \over {\partial x_i \partial x_j}}$

## 5.2.4 얀센의 부등식

### 얀센의 부등식

앞서 배웠던 부등식 = 얀센의 부등식(Jansen's inequality)

$f(wx_1 + (1 - w)x_2 ≤ wf(x_1) + (1-w)f(x_2)$

일반화를 시켜보자

$f(w_1\mathrm x_1 + ... + w_k\mathrm x_k ) ≤ w_1 f(\mathrm x_1) + ... + w_k f(\mathrm x_k)$

이 때, $\mathrm x_1, ... ,\mathrm  x_k \in dom \ f$ 이며, $w_1, ... , w_k ≥ 0$이고 $w_1 + ... + w_k = 1$ 이다

얀센의 부등식을 응용해 사용되는 부등식 중 하나는 아래와 같음

아래 부등식에서 E는 기댓값(expection)을 의미

$f(E(x)) ≤ E(f(x))$

또한 얀센의 부등식을 응용하면 다음과 같은 간단한 부등식도 쓸 수 있음

$f({{x_1 + x_2} \over 2}) ≤ {{f(x_2) + f(x_2)} \over {2}}$

## 5.2.5 컨벡스 성질 보존 조건

컨벡스 성질이 보존되는 경우

1. 비음수 가중합(nonnegative weighted sums)을 적용할 때 컨벡스 성질이 보존됨

    ex) $f$가 컨벡스 함수, $\alpha ≥ 0$이면 ⇒ $\alpha f$는 컨벡스하다

    ex) $f_1, f_2$가 모두 컨벡스일 때, 두 함수의 합 $f_1 + f_2$또한 컨벡스하다.

    이를 정리하면 아래 조건을 만족하는 함수 $f$는 컨벡스하다

    $f = w_1f_1 + ... + w_mf_m$

2. 아핀 변환을 했을 경우에도 컨벡스 성질이 보존됨

    ex) 함수 f가 컨벡스하다면 아래 조건을 만족하는 $g$ 또한 컨벡스

    $g(\mathrm x) = f(W\mathrm x +b)$

3. 여러 컨벡스 함수의 최댓값을 구하는 함수가 존재할 때, 최댓값 함수 또한 컨벡스 함수이다

    ex) $f_1$과 $f_2$ 모두 컨벡스 함수이고 두 함수의 최댓값 함수를 $f$라고 했을 때,

    $f$ 역시 컨벡스 함수

    일반화

    $f = max\{f_1(x),...,f_m(x)\}$

4. $f$ 가 컨벡스 함수일 때, $f$의 합성 함수 또한 컨벡스 함수이다
    - $f$가 컨벡스 함수, exp($f$) 또한 컨벡스 함수
    - $f$가 항상 양수, 콘케이브하다면 $\log f$ 또한 콘케이브하다
    - $f$가 항상 양수, 콘케이브하다면 1 / $f$ 은 컨벡스하다
    - $f$가 비음수이고 컨벡스하다면, $p≥1$일 때, $f^p$ 또한 컨벡스하다

# 5.3 라그랑주 프리멀 함수

## 5.3.1 일반적인 최적화 문제

### 라그랑주 승수법(Lagrange Multiplier Method)

제약식(constraint)이 있는 최적화 문제를 푸는 방법

최적화를 하려는 값에 라그랑주 승수(Lagrange Multiplier)항을 더해 제약이 있는 문제로 바꿈으로써 해결가능

최적화를 한다는 말은 극값을 구한다는 뜻, 극값을 구한다는 말은 최댓값이나 최솟값을 구하는 것을 의미함

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fbb0b8a-ec34-43f9-a799-63ef169a5142/_2021-04-05__12.58.45.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fbb0b8a-ec34-43f9-a799-63ef169a5142/_2021-04-05__12.58.45.png)

위 식은 최적화 문제를 표준화 된 형태로 나타낸 것

이때, 최적화시키려는 **목적 함수(objective function)**은 $f(x)$.

자주 사용되는 목적 함수에는 MSE(Mean Squared Error)와 같은 함수 존재

이때, x는 최적화 변수, n차원 실수 공간에 속함 ⇒ $\mathrm x \in \R^n$으로 나타낼 수 있음

구하려는 최적값을 $p^*$라고 함

### 부등식 제약(inequality constraint function)

위 식에서 $g_i(\mathrm x), h_i(\mathrm x)$는 제약식을 나타냄

$g_i(\mathrm x)$ ≤ 0은 부등호를 포함함 ⇒ 부등식 제약 함수

### 등식 제약 함수(equality constraint function)

$h_i(x) = 0$과 같이 등호를 포함하는 제약 함수는 등식 제약 함수라고 함

- 질문

    질문이 있습니다...!
    제약함수라는게 이제 f(x)에서 범위를 제한한다라는거 까지는 이해를 했는데 직관적으로? 실제적으로 어떤건지가 궁금합니다..

## 5.3.2 컨벡스 최적화 문제

일반적인 최적화 형태와 컨벡스 최적화는 어떤 점이 다를까

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5497945a-9f99-4b7d-97b4-5635ace872fe/_2021-04-05__12.57.37.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5497945a-9f99-4b7d-97b4-5635ace872fe/_2021-04-05__12.57.37.png)

컨벡스 최적화 문제에서는 몇가지 조건이 추가

우선 $f(\mathrm x), g_i(\mathrm x)$는 모두 컨벡스 함수여야 한다는 조건이 붙음

즉, 목적 함수와 부등식 제약 함수 모두 컨벡스 함수여야 한다는 뜻

등식 제약 조건 함수 $h_i(\mathrm x) = \mathrm w^T_i - b_i$는 아핀 함수여야 함

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5054d4cc-c802-4381-b564-21803ed5817c/_2021-04-05__12.59.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5054d4cc-c802-4381-b564-21803ed5817c/_2021-04-05__12.59.10.png)

그림 5-10 제약 조건의 부호에 따른 컨벡스 여부

최적화 문제에서 주목해야 하는 부분은 부등식 $g_i(\mathrm x) ≤ 0$의 부호

왜 함수  $g_i(\mathrm x)$는 0보다 작아야 하는가??

because  $g_i(\mathrm x) ≤ 0$를 만족해야 컨벡스하기 떄문

if) $g_i(\mathrm x) > 0$ ⇒ 컨벡스하지 않음

if) $f(x) = x^2 - 1$, 제약조건 $f(x) ≤ 0$

- $x^2 ≤0$ 이면 만족하는 변수 x의 해는 -1 ≤ x ≤ 1
    - 그림 5-10 왼쪽을 보면 -1 ≤ x ≤ 1 영역에 있는 변수 x는 연속 ⇒ 제약조건 $x^2 -1≤0$은 컨벡스 함

elif)  $f(x) ≥ 0$일 때

- $x^2 -1 ≥ 0$을 만족하는 해는 x ≥ 1 or x ≤ -1
    - 변수 x는 불연속적 ⇒ 제약조건 $x^2 -1 ≥ 0$은 컨벡스하지 않음

## 5.3.3 라그랑주 프리멀 함수

### 라그랑지안(Lagrangian)

최적화 문제를 아래처럼 표현한 것을 라그랑지안(Lagrangian)이라고 하며, 다른 말로는 라그랑주 프리멀 함수라고 함

라그랑주 프리멀 함수 $L_p$는 아래와 같음

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15a65b51-f6e0-4d1d-b760-d97676a3a756/_2021-04-05__1.27.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15a65b51-f6e0-4d1d-b760-d97676a3a756/_2021-04-05__1.27.46.png)

기호 설명

$\lambda_i$ : 제약식 $g_i(\mathrm x) ≤ 0$에 대한 라그랑주 승수(Lagrange multiplier)

$v_i$ : 제약식 $h_i(\mathrm x) = 0$에 대한 라그랑주 승수

$\boldsymbol \lambda = ( \lambda_1,\lambda_2,...,\lambda_m),\mathrm v = ( \mathrm v_1,\mathrm v_2,...,\mathrm v_p)$ : 듀얼 변수(dual variable) or 라그랑주 승수 벡터 (Lagrange multipler vector)

ex) 최적화하고 싶은 목적 함수 : $f(x_1,x_2) = x_1^2+x_2^2$

등식 제약 조건 : $h(x,y) = x_1 + x_2$

극값을 구하기 위한 라그랑주 프리멀 함수

$L_p(x_1,x_2,\lambda) = f(x_1,x_2) + \lambda h(x_1,x_2) 
= x^2_1 + x^2_2 + \lambda  (2-x_1-x_2)$

함수 $L(x_1,x_2)$를 $x_1,x_2,\lambda$에 대해 편미분 결과가 0이 되는 지점을 찾는다

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76181ba1-9240-415f-a392-9923f6723f68/_2021-04-05__1.39.29.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76181ba1-9240-415f-a392-9923f6723f68/_2021-04-05__1.39.29.png)

위 식을 정리해 찾은 극값은

$\therefore x_1 = 1, x_2 = 1, \lambda = 2$

## 5.4 라그랑주 듀얼 함수

### 라그랑주 듀얼 함수(Lagrange dual function) $L_p$

라그랑주 프리멀 함수의 하한(lower bound)를 나타냄

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7f46905-91b8-498c-9c70-22c9bce29233/_2021-04-05__1.43.06.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7f46905-91b8-498c-9c70-22c9bce29233/_2021-04-05__1.43.06.png)

if) 라그랑주 프리멀 함수의 하한(lower bound)이 없는 경우

⇒ 라그랑주 듀얼 함수는 마이너스 무한대의 값을 가짐

라그랑주 듀얼 함수는 $\lambda ≥ 0$에 대해 최적값 $p^*$의 하한(lower bound)을 나타냄

⇒ $L_D(\lambda, \mathrm v) ≤ p^*$

만약 라그랑주 듀얼 함수의 최적값을 $d^*$라고 하면 아래와 같은 부등식 성립

즉, 프리멀 문제의 최적값을 구하는 것은 듀얼 함수를 최대화 하는 것과 동일

⇒ $d^* ≤ p^*$

위와 같은 성질을 weak duality라고 함

즉, 라그랑주 듀얼 함수의 최적값 $d^*$는 라그랑주 프리멀 함수의 최적값 $p^*$보다 작거나 같다