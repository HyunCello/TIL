# Bagfile 만들기

kitti dataset http://www.cvlibs.net/datasets/kitti/

\
ROS에서 볼 수 있는 데이터로 만들려면 ex) 토픽들

.bag 라는 파일로 만들어야 한다

쉽게 만드는 방법은 https://github.com/tomas789/kitti2bag -> 요게 제일 유명

근데 각 이미지의 정보가 필요한데 이건 어떻게 받지

## 토픽의 종류
- 흑백 좌, 우 이미지
- 컬러 좌, 우 이미지
- 라이다 데이터 (bin파일)