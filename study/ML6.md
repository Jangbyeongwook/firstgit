####ML 11강 Convorutional Neural Network
>살짝 설명이 부족한 느낌이 많이 들어요.

+ 유래
 고양이 시신경 실험을 통해 만들어진 네트워크이다.

+ Convolution 진행
 전체의 이미지를 한 번에 받지 않고, 일부만 받아들인다.
 일부만 받아들인 것을 필터를 이용해서 1개의 값으로 나타낸다.(Linear regression 하듯이)
 전체 이미지를 받아들일 때 까지 계속 반복한다.
 
 ex)32X32X3 image를 5X5X3 filter로 받아들이면 총 받아들이는 이미지의 개수는 (32-5)/stride size+1 = 28개 가 나온다. stride는 이미지를 몇 칸씩 옮기냐에 따라 사이즈가 달라진다.
 
 필터를 여러개수로 여러번 진행한다. 필터를 거쳐 나온 결과에 대해 한 번 더 convolution을 진행하며 반복하면 된다.

+ padding
 필터로 진행할 때마다 이미지의 원본이 작아져 데이터 유실을 방지하기위해 원본 이미지와 동일한 사이즈를 유지하도록 해주는 것. 이미지 테두리에 0을 추가한다.
 
+ Pooling (sampling)
 간단하게 샘플링한다고 생각하면된다. 필터하고 나온 레이어에 대해 resize를 진행한다.

 ex) 4X4의 이미지를 2X2의 필터(stride=2)를 이용해 풀링을 진행한다. 
 
 풀링을 진행하는 방법도 여러가지 있지만 여기서는 max pooling인 가장 큰값을 뽑아주는 것을 이용한다.

+ CNN 예시
 처음에는 Lecun 교수님이 사용했다. 손글씨를 분류할 수 있는 것.
 알렉스 넷 : 이미지넷 경진대회에서 1등 했다.
 구글 넷 : inception module 살짝 특이하게 생김.
 ResNet : 에러율을 확 줄여버렸다. 레이어를 152개를 사용했다.(fast forward기법 사용)

####ML 12강 Recurrent Neural Network
> RNN은 이론적으로 알려주기보다는 실습과 병행하여 알려주기 때문에 이론적인 면은 많이 적을 것이다.

+ Sequence Data
 우리가 사용하는 데이터는 시퀀스 데이터인 경우가 아주 많다 
 ex) 음성, 말, 글 등

이를 해결하기 위해 RNN이 탄생하였다. 하나의 뉴럴에서 현재 스테이트 결과값이 다음의 결과값에 영향을 미친다. 
![그림19.png](./그림19.png)

+ Vanilla Recurrent Neural Network

![그림20.png](./그림20.png)
> 다음 스테이트에 넘겨주기 위한 h~t~가 있으며, 결과값을 출력해주는 y~t~가 존재한다.
