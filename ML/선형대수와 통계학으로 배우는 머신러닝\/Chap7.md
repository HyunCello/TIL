# 7.1 오버피팅과 언더피팅

머신러닝 모형을 만들었을 때 모형의 성능은 어떻게 평가?

## 오버피팅 & 언더피팅

오버피팅 : 특정 데이터셋에 과도하게 적합된 것

얼핏 정확도가 높아 보이지만 특정 데이터셋에만 적합되어 알려지지 않은 데이터에 대한 예측력은 낮아지게 됨

언더피팅 : 데이터 셋에 적합이 잘 되지 않은, 즉 과소 적합된 것

머신러닝을 통해 모형을 학습하는 이유는 데이터의 종류와 상관없이 일반화할 수 있는 모형을 생성하는 것

주어진 데이터 셋에 대해 오버피팅이나 언더피팅이 발생한다면 새로운 데이터에 적용할 수 있는 좋은 모형 X

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e336ba39-a7d4-489e-990e-bc7ebe1e64d1/_2021-04-13__4.42.17.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e336ba39-a7d4-489e-990e-bc7ebe1e64d1/_2021-04-13__4.42.17.png)

그림 7-1

위 그림 왼쪽 데이터가 존재할 때, 오른쪽이 이상적인 머신러닝 모형

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad41cb0b-7710-43f8-b0b8-6a81d1ccbe37/_2021-04-13__4.44.48.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad41cb0b-7710-43f8-b0b8-6a81d1ccbe37/_2021-04-13__4.44.48.png)

왼쪽은 오버피팅, 오른쪽은 언더피팅

오버피팅된 경우, 주어진 데이터셋에 대해서는 오차가 없으므로 높은 성능을 보이는 것처럼 착각할 수 있음

but 새로운 데이터 셋에 적용하면 학습 데이터 셋과는 달리 큰 오차를 보임

언더피팅의 경우 데이터의 특성을 잘 나타내지 못함

이 경우, 트레이닝 데이터 셋과 테스트 데이터 셋 모두 큰 오차를 보임

오버피팅과 언더피팅의 개념을 수식을 통해 알아보자

실제 모형이 n차원식이라고 했을 때,

- 추정한 모형이 n보다 큰 차원의 식으로 표현이 된다 ⇒ 오버피팅
- n보다 작은 차원의 식으로 적합되었다 ⇒ 언더피팅

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df4c9f34-2de1-4998-a11c-e9f2ec370ccb/_2021-04-14__1.53.51.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df4c9f34-2de1-4998-a11c-e9f2ec370ccb/_2021-04-14__1.53.51.png)

위와 같이 실제 모형이 n차원식이라고 해보자

if) 오버피팅

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65df2700-3b03-4fbd-8a13-d5c16db9281a/_2021-04-14__1.56.47.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65df2700-3b03-4fbd-8a13-d5c16db9281a/_2021-04-14__1.56.47.png)

if) 언더피팅

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fe31933-bcbe-48c3-8b5e-8db394b3e679/_2021-04-14__1.57.14.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fe31933-bcbe-48c3-8b5e-8db394b3e679/_2021-04-14__1.57.14.png)

관련된 개념 중 하나

### 편향-분산 트레이드오프(bias-variance tradeoff)

이상적으로 연구자는 편향과 분산 모두 작은 것을 원하지만..보통은 그렇지 않음

편향-분산 트레이드오프

- 편향이 낮을수롣 분산은 커지고, 반대로 편향이 높을수록 분산이 작아지는 경향

분산이 높은 현상 ⇒ 주로 복잡한 모형에서 나타남

모형이 복잡하다 ⇒ 오버피팅이 발생할 가능성이 높다

편향이 큰 현상 ⇒ 주로 간단한 모형에서 나타남

모형이 간단하다 ⇒ 언더피팅이 발생할 가능성이 높다 ⇒ 편향이 커질 수 있다

# 7.2 크로스-밸리데이션

오버피팅과 언더피팅을 방지하고 적합한 모형을 추정하기 위해서는 어떻게 해야 하나?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc2ef6c2-d902-4856-bde1-78e5b35ef407/_2021-04-14__2.06.00.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc2ef6c2-d902-4856-bde1-78e5b35ef407/_2021-04-14__2.06.00.png)

그림 7-3 전체 데이터

위와 같은 데이터 셋이 주어졌다고 가정

전체 데이터셋을 모형 생성을 위한 학습에 사용하면 문제가 발생

why? 모형을 생성한 후 실제 데이터에 적용해 보고 성능을 평가해야 하지만

데이터 전체를 학습하는 데 사용하면 새롭게 적용할 데이터가 없기 때문

이러한 문제를 해결하기 위해 전체 데이터를 트레이닝 데이터와 테스트 데이터로 분할해서 사용

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/911df3ee-6463-4bbb-9b07-ee96a3c52474/_2021-04-14__2.10.03.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/911df3ee-6463-4bbb-9b07-ee96a3c52474/_2021-04-14__2.10.03.png)

전체 데이터 셋을 트레이닝(Training)과 테스트(Test) 데이터로 나눈 것

트레이닝 데이터는 학습하는 데 사용, 테스트 데이터는 학습 시에는 사용하지 않고, 모형의 성능을 평가할 때 사용

but 이 경우에도 문제 발생

머신러닝을 적용할 때 다양한 하이퍼파라미터에 대해 여러가지 모형 후보군을 생성하고 평가한 후 최종 모형을 선택하게 됨

이때, 파라미터(parameter)는 모형 내부에서 데이터에 의해 추정되는 값이고, 하이퍼파라미터(hyperparameter)는 모형 생성에 쓰이는 데이터로부터 나온 값이 아니고, 사용자가 직접 정하는 값

ex) k-최근접 이웃 알고리즘

k값을 직접 정하는데, 이때 k가 하이퍼파라미터 값

하이퍼파라미터를 결정하는 과정에서 트레이닝 데이터와 테스트 데ㅣㅇ터만 존재한다면, 테스트 데이터에 의해 최종 모형의 하이퍼파라미터가 결정된다

즉, 모형의 하이퍼파라미터가 테스트 데이터에 의존

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f94b9171-177b-40ee-a853-3ade9341a501/_2021-04-14__2.20.03.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f94b9171-177b-40ee-a853-3ade9341a501/_2021-04-14__2.20.03.png)

이 문제를 해결하기 위해 위 그림처럼 트레이닝 데이터의 일부르 밸리데이션 데이터로 사용

밸리데이션 데이터는 하이퍼파라미터 설정을 위해 사용.

즉, 트레이닝 데이터는 파라미터를 구하는 데 사용하고, 밸리데이션 데이터는 하이퍼파라미터를 정하는 데 사용

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75cea82c-a5a7-4c01-b67c-e36d60b11ade/_2021-04-14__2.24.37.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75cea82c-a5a7-4c01-b67c-e36d60b11ade/_2021-04-14__2.24.37.png)

위 그림과 같이 주어진 데이터 셋에 대해서 트레이닝 데이터, 밸리데이션 데이터, 테스트 데이터로 분할할 수 있는 다양한 조합 방법 존재

이처럼 다양한 조합을 통해 모형의 성능을 검증하는 것을 크로스-밸리데이션(cross-validation, 교차 검증)이라고 함

위 그림은 전체 데이터를 k개로 분할한 후 트레이닝, 밸리데이션 데이터 조합을 바꾸는 방법이며 이를 k-fold cross-validation이라고 부름

위 그림은 데이터 조합을 5개로 설정했으므로 5-fold cross-validation이라고 부름

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41f52806-a22e-4081-a943-823373a62abf/_2021-04-14__2.30.07.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41f52806-a22e-4081-a943-823373a62abf/_2021-04-14__2.30.07.png)

머신러닝 전체 과정을 요약하면 위 그림처럼 나타낼 수 있음

전체 과정을 보면 위처럼 됨

전체 데이터 셋을 크게 트레이닝 데이터와 테스트 데이터로 분할함

테스트 데이터는 최종 모형을 테스트하는 데만 사용

그리고 트레이닝 데이터의 읠부를 밸리데이션 데이터로 분할한 후 트레이닝 데이터를 통해 학습시켜 만든 모형을 밸리데이션 데이터를 이용해 하이퍼하라미터 결정

끝으로 하이퍼파라미터까지 설정한 모형을 테스트 데이터를 이용해 성능을 평가

# 7-3 파이프라인

파이썬을 활용한 머신러닝 실습 과정에서 파이프라인을 사용하면 데이터 전처리와 학습 모형을 연결해 코드를 간결화할 수 있음

예를 들어, 간단한 회귀 모형을 만든다고 가정

우선 파이프라인을 적용하기 전 학습 과정은 아래와 같음

```python
# 표준화 스케일링
std_scale = StandardScaler()                    # 1
X_tn_std = std_scale.fit_transform(X_tn)        # 2
X_te_std = std_scale.transform(X_te)            # 3

# 학습
clf_linear = LinearRegression()                 # 4
clf_linear.fit(X_tn_std, y_tn)                  # 5
```

파이프라인 적용 전 코드는 위와 같이 표준화 단계와 학습 단계가 나뉘어 있으며 각자 따로 실행

1. 표준화 스케일러를 설정
2. 트레이닝 데이터를 표준화
3. 테스트 데이터를 표준화
4. 선형 회귀 모형을 설정
5. 트레이닝 데이터를 이용해 선형 회귀 모형을 적합

파이프라인을 사용한 코드

```python
from sklearn.pipeline import Pipeline             # 1
# 파이프라인
linear_pipeline = Pipeline([                      # 2
    ('scaler', StandardScaler()),
		('linear_regression', LinearRegression())
])

# 학습
linear_pipeline.fit(X_tn, y_tn)                   # 3
```

1. 사이킷런은 파이프라인을 사용할 수 있는 Pipeline이라는 함수를 제공
2. 파이프라인을 설정하는데, 데이터 표준화 이후 선형 모델을 실행하는 순서로 구성된 파이프라인을 만듦

    해당 파이프라인을 linear_pipeline이라고 이름 짓고, 해당 파이프라인을 실행

3. 파이프라인에 사용할 트레이닝 데이터 X_tn, y_tn만 넣으면 자동으로 데이터를 표준화하고, 선형 회귀 모형을 실행

### 파이프라인 사용 전 전체 코드

```python
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model_selection import train_test_split
from sklearn.matrics import mean_squared_error

raw_boston = datasets.load_boston()

X = raw_boston.data
y = raw_boston.target

# 트레이닝 / 테스트 데이터 분할
X_tn, X_te, y_tn, y_te = train_test_split(X,y,random_state = 7)

# 표준화 스케일링
std_scale = StandardScalar()
X_tn_std = std_scale.fit_transform(X_tn)
X_te_std = std_scale.transform(X_te)

# 학습
clf_linear = LinearRegression()
clf_linear.fit(X_tn_std, y_tn)

# 예측
pred_linear = clf_linear.predict(X_te_std)

# 평가
mean_squard_error(y_te, pred_linear)
```

### 파이프라인 사용 후 전체 코드

```python
# 트레이닝 / 테스트 데이터 분할
X_tn, X_te, y_tn, y_te = train_test_split(X,y,random_state = 7)

# 파이프라인
linear_pipeline = Pipeline([
		('scaler', StandardScaler()),
		('linear_regression', LinearRegression())
])

# 학습
linear_pipeline.fit(X_tn,y_tn)

# 예측
pred_linear = linear_pipelpine.predict(X_te)

# 평가
mean_squared_error(y_te, pred_linear)
```

# 7-4 그리드 서치

그리드 서치(grid search)는 머신러닝 과정에서 관심있는 매개 변수들을 대상으로 학습가능하도록 만드는 방식

ex) k-최근접 이웃 알고리즘

k-최근접 이웃 알고리즘에 사용할 수 있는 k값에는 여러 후보가 존재함

어떤 하이퍼파라미터 k가 가장 높은 성능을 보일지는 직접 학습하기 전에는 알 수 없음

학습시키기 전에 관심 있는 k의 후보군을 정해 놓고 학습시킨 후 모형 성능을 비교한 후 최적의 k를 선정할 수 있음

다음 코드는 k-최근접 이웃 알고리즘을 적용할 때부터 1부터 10까지의 k값 후보 중 가장 높은 성능을 보이는 k 값을 정하는 과정

```python
best_accuracy = 0                                    # 1
for k in [1,2,3,4,5,6,7,8,9,10]:                     # 2
		clf_knn = KNeighborClassifier(n_neighbors=k)     # 3
		clf_knn.fit(X_tn_std, y_tn)                      # 4
		knn_pred = clf_knn.predict(X_te_std)             # 5
		accuracy = accuracy_score(Y_te, knn_pred)        # 6
		if accuracy > best_accuracy:                     # 7
				best_accuracy = accuracy                     # 8
				final_k = 'k' : k                            # 9
```

1 : 가장 높은 정확도를 나타내는 best_accuracy라는 변수를 초기화

2 : 관심 있는 하이퍼파라미터 k의 범위를 정해 반복문 수행

3 : 해당 k값을 적용한 k-최근접 이웃 알고리즘을 실행함

4 : 학습 데이터를 이용해 모형을 적합시킴

5 : 예측값을 구함

6 : 정확도를 구함

7 : 정확도가 best_accuracy보다 높다

8 : best_accuracy를 갱신한다

9 : 해당 k값을 저장

# 7-5 손실 함수와 비용 함수

## 7.5.1 손실 함수와 비용 함수의 개념

손실 함수(loss fucntion)은 머신러닝을 통해 생성한 모형이 실젯값과 얼마나 차이가 나는지

즉, 손실 정도를 수치로 나타내는 함수

모형의 손실은 예측값과 실젯값의 차이를 이용해 측정

그리고 손실 함수와 비슷하게 비용 함수(cost function)라는 개념도 존재

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e947348-0ec1-409c-93f9-044ff2c2b74a/_2021-04-19__12.02.47.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e947348-0ec1-409c-93f9-044ff2c2b74a/_2021-04-19__12.02.47.png)

그림 7-8 손실 함수, 비용 함수 비교

손실 함수와 비용함수의 차이는 

[그림 7-8]과 같이 손실 함수는 각 데이터 포인트에 대해 예측값과 실젯값의 차이를 나타내지만, 비용 함수는 데이터 셋 전체를 대상으로 하는 손실을 의미

손실함수와 비용 함수는 엄밀하게 말하면 서로 다르다고 할 수도 있으나 실제로는 손실함수와 비용함수를 구분 없이 사용하기도 함

## 7.5.2 L1 손실함수

손실 함수에는 크게 L1 손실과 L2 손실이 존재

L1 손실 = L1 비용(L1 cost)

<!-- $L1 \ Loss = \Sigma |y_{true} - y_{predict}|$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=L1%20%5C%20Loss%20%3D%20%5CSigma%20%7Cy_%7Btrue%7D%20-%20y_%7Bpredict%7D%7C">

위 수식에서 <!-- $y_{true}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y_%7Btrue%7D">는 실젯값을 의미하고, <!-- $y_{predict}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y_%7Bpredict%7D">는 학습 모형을 이용해 예측한 값을 의미

즉 L1 손실은 실젯값과 예측값의 차이에 기댓값을 취한 것

실젯값과 예측값의 차이를 줄이는 것이 학습 목적

L1 손실과 관련된 비용 함수로 MAE(Mean Absolute Error)가 있음

<!-- $MAE = {1\over n}\sum_{i=1}^n|y_i-\hat y_i|$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=MAE%20%3D%20%7B1%5Cover%20n%7D%5Csum_%7Bi%3D1%7D%5En%7Cy_i-%5Chat%20y_i%7C">

MAE는 데이터셋의 L1 Loss 평균을 나타내는 비용 함수

위 수식에서 <!-- $y_i$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y_i">는 i번째 실젯값을 의미하고 <!-- $\hat y_i$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Chat%20y_i">는 i번째 예측값을 의미

## 7.5.3 L2 손실함수

L2 손실(L2 Loss)는 아래와 같음.

L2 손실은 실젯값과 예측값의 차이에 제곱을 취함으로써 구할 수 있음

$L2 \ Loss = \Sigma (y_{true} - y_{predict})^2$

L2 손실을 이용한 비용 함수에는 MSE(Mean Squared Error), RMSE(Root Mean Squared Error)가 존재

MSE와 RMSE는 다음과 같이 표현

$MAE = {1\over n}\sum_{i=1}^n(y_i-\hat y_i)^2$

$RMSE = \sqrt{MSE}$

MSE는 흔히 사용하는 비용 함수로 실젯값과 예측값의 차이의 제곱의 평균을 의미

RMSE는 MSE에 제곱근을 취한 형태

MSE를 구하는 과정에서 실젯값과 예측값을 제곱하므로 MSE는 이상치(outlier)의 변화에 민감

반면 MAE나 RMSE는 이상치와 상관없이 안정된 값을 보여줌

머신러닝 모형의 이상치에 중점을 두고 싶다면 MSE를 사용하고, 그렇지 않으면 MAE나 RMSE를 사용할 수 있음

## 7.5.4. 엔트로피

엔트로피는 정보 이론에서 사용하는 개념으로 확률 변수의 불확실성 정도를 측정하기 위해 사용

확률 변수 X의 엔트로피는 아래와 같이 정의

### 엔트로피

$Entropy(P) = -\sum P(x)\log P(x) = - E (logP(x))$

위 엔트로피 식은 Entropy(P)로 표기했지만 H(P) 혹은 H(X)라고 쓰기도 함

엔트로피는 의사 결정 나무에서 주로 사용되는데 자세한 내용은 의사 결정 나무 단원에서 다룸

### 크로스 엔트로피

$CrossEntropy(P,Q) = - \sum P(x)\log Q(X) = -E_p(\log Q(x))$

위 식은 크로스-엔트로피(cross-entropy)라고 하는데, 엔트로피는 하나의 분포를 대상으로 하는 반면, 크로스-엔트로피는 두 분포P(x), Q(x)를 대상으로 엔트로피를 측정해 두 분포 간의 차이를 계산

머신러닝에서 크로스-엔트로피를 사용할 때는 P(x)를 실제 모형의 분포, Q(x)를 추정 모형의 분포라고 설정

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a494a3bd-e8fc-4e24-8b5c-adccd58506f0/_2021-04-20__3.15.33.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a494a3bd-e8fc-4e24-8b5c-adccd58506f0/_2021-04-20__3.15.33.png)

그림 7-9 크로스-엔트로피 예제

$CrossEntropy(P,Q) = - \sum P(x)\log Q(X)  \\ = -(1 \times \log 0.92 + 0 \times \log 0.05 + 0 \times \log 0.01 \\ = 0.08$

이번에는 간단한 예를 들어 크로스-엔트로피를 구해봄

과일을 분류하는 문제에서 예측 확률 분포와 실제 확률 분포가 [그림 7-9]와 같을 때, 크로스 엔트로피를 계산하면 위 식과 같음

...뭐시기뭐시기!

# 7.6 모형 성능 평가

## 7.6.1 모형 성능 평가에 필요한 개념

모형의 성능을 평가하는 방법에는 여러 가지가 존재

어떤 평가 방법을 기준으로 놓고 보느냐에 따라 모형 성능이 좋아 보이기도 하고 나빠 보이기도 함

사이킷런에서 사용하는 성능 평가 변수의 네이밍 방법에는 암묵적인 규칙이 존재하는데, 규칙에 따르면 네이밍 방법만 봐도 숫자의 높고 낮음에 따른 성능 해석 방법을 유추할 수 있음

만약 메소드가 '_score'로 끝난다면 이는 결괏값이 클수록 모형 성능이 좋다는 것을 의미

반대로 '_error'나 '_loss'로 끝난다면 숫자가 작을수록 좋은 성능을 나타냄

이 절에서는 머신러닝 모형 평가에 쓰이는 여러 가지 개념을 알아보자

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f287cbf9-5a4f-4393-a297-2051bb68fcdb/_2021-04-20__3.23.56.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f287cbf9-5a4f-4393-a297-2051bb68fcdb/_2021-04-20__3.23.56.png)

표 7-1 이진 분류표

[표 7-1]은 이진 분류 문제에서 데이터를 예측값과 실젯값에 따라 분류한 표

[표 7-1]에서 예측과 실제 결과가 모두 양성이거나 모두 음성이면 올바르게 예측했으므로 정답으로 분류할 수 있고, 예측값과 실제 결과가 일치하지 않은 경우는 오답으로 분류할 수 있음

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84624278-c678-46f5-bc4d-6e88de334852/_2021-04-20__3.24.16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84624278-c678-46f5-bc4d-6e88de334852/_2021-04-20__3.24.16.png)

표 7-2 이진 분류 케이스

각 예측과 실제 결과 케이스별 세부적인 명칭은 [표 7-2]와 같음

먼저 정답으로 분류되는 경우를 보자

주어진 데이터를 양성(Positive)로 예측했을 때, 실젯값도 양성일 때는 정답(True)으로 분류하고, 이 경우를 True Positive(줄여서 TP)라고 함

반대로 예측했을 때 음성(Negative)이고 실제로도 음성으로 나타난다면 이 또한 정답(True)으로 분류되지만 음성 예측값에 대한 정답이므로 True Negative(줄여서 TN)라고 부름

다음으로는 오답으로 분류되는 상황

양성으로 예측했는데 실제 결괏값은 음성으로 나타날 때

이는 오답으로 분류되고, 이런 경우를 False Positive(FP)라고 부름

다른 말로는 Type 1 Error(제 1종 오류)라고도 부름

반대로 음성으로 예측했는데 실제로는 양성으로 나타나는 경우 이 또한 오답으로 분류되고, 이런 경우를 False Negative(FN) 또는 Type 2 Errer(제 2종 오류)라고 부름