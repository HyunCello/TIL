# 01 파이토치 패키지의 기본 구성

## 1. torch

메인 네임스페이스

텐서 등의 다양한 수학 함수가 포함되어 있으며 Numpy와 유사한 구조를 가짐

## 2. torch.autograd

자동 미분을 위한 함수들이 포함되어져 있음

자동 미분의 on/off를 제어하는 콘텍스트 매니저(enable_grad/no_grad)나 자체 미분 가능함수를 정의할 때 사용하는 기반 클래스인 'Function'등이 포함되어져 있음

## 3. torch.nn

신경망을 구축하기 위한 다양한 데이터 구조나 레이어 등이 정의되어져 있음

ex. RNN, LSTM과 같은 레이어,ReLU와 같은 활성화 함수, MSELoss와 같은 손실 함수들

## 4. torch.optim

확률적 경사 하강법(Stochastic Gradient Descent, SGD)를 중심으로 한 파라미터 최적화 알고리즘이 구현

## 5. torch.utils.data

SGD의 반복 연산을 실행할 때 사용하는 미니 배치용 유틸리티 함수가 포함되어져 있음

## 6. torch.onnx

ONNX(Open Neural Network Exchange)의 포맷으로 모델을 익스포트(export) 할 때 사용

ONNX는 서로 다른 딥 러닝 프레임워크 간에 모델을 공유할 때 사용하는 포맷

