####ML 8강 딥러닝의 기본 개념 : 시작과 XOR 문제

+ Ativation Functions
 입력값이 일정 기준을 넘으면 1 아니면 0을 출력.
 시그모이드 같은 느낌이랄까?

+ Deep Learning
 입력층과 출력층 사이에 여러 개의 은닉층들로 이뤄져 딥러닝은 더 복잡한 비선형 관계들을 학습할 수 있다.
 
+ XOR 문제
 기존 Linear regression은 XOR문제를 절대로 해결할 수 없는 문제점이 발생했다. 이로 구성된 딥러닝 또한 XOR문제에 맞닥들이면서 한동안 연구가 진행되지 않았다.
Minsky 교수님께서 XoR은 multi layer perceptron을 이용하면 풀 수 있지만, 아무도 학습을 시킬 수 없다고 주장을 하였다.

+ Backpropagation
 역전파. 출력값을 이용해서 역으로 진행하면서 w와 b값을 조절한다. Hinton
 XOR문제에 대한 해결방안. backpropagation이 완벽한 해답은 아니였다.
 매우 딥하게 (10여개 이상)레이어로 구성된 경우, 이 방법 성능이 많이 떨어져서 큰 문제에 맞닥들인다.
> 초기값을 잘 설정해주면 딥러닝 문제를 해결할 수 있다.

+ 고양이 시신경 실험(Convolution Neural Network)
  그림의 형태에 따라 일부의 뉴런만 반응을 하는 것을 보고 그림을 볼 때, 신경망 세포가 동시에 그림 전체를 보는 것이아니라 일부만 떼내어 본 후 나중에 합치는 것이 아닐까라는 생각을 이용해서 Convolution Neural Network를 개발.

#### 9강 XOR 문제 딥러닝으로 풀기
> 뉴럴네트워크를 이용해서 XoR의 문제를 푸는 방법을 알려준다.

![그림15.png](./그림15.png)

> w와 b값은 가정을 한 것이며, 단순히 풀릴 수 있는지만 확인을 해 보자.
 
![그림16.png](./그림16.png)
> 위 그림을 하나로 표현한 것이다.

+ How cna we learn W1,W2,B1,B2 from training data?
 - backpropagation(chain rule)을 이용하자.
 
![그림17.png](./그림17.png)
> forward로 진행을 한 후, backword 진행
> 가장 마지막 노드의 식을 먼저 구한다. 노드 전의 입력이 노드 출력에 미치는 영향을 알고 있다면, chain rule을 이용해서  backpropagation을 이용할 수 가 있다. 

+ 하지만, 전에도 언급했듯, Backpropagation은 매우 딥하게 구성되어 있는 뉴럴 네트워크에서는 사용을 할 수가 없다. Vanishing gradient 문제가 발생한다. (NN winter 2) 

#### 10강 ReLU, weight initialization, Dropout, Ensemble

+ ReLU(Rectified Linear Unit)
 Vanishing gradient문제를 해결하기 위해 sigmoid 대신 ReLU를 이용하자.

![그림18.png](./그림18.png)

> 확실히 NN에서 ReLU를 사용하면, cost도, accuracy도 좋아지는 모습을 볼수가 있다.
> ReLU말고도 더 upgrade된 함수가 있다. (activation function 검색)

+ weight initialization
 초기값을 0으로 주는 멍청한 짓은 하지말자. 학습을 할 수가 없다.
 + RBM(Restricted boatman Machine)
  Deep bilife network = RBM을 이용해서 초기화를 진행하는 네트워크
  	+ 방법
  	바로 앞 뒤 노드를 이용해 forward 진행 후 backward로 진행하면서 초기 입력값과 backward 한 입력값이 최대한 비슷하도록  weight 값을 초기화한다. (encoder / decoder)
  fine tuning
 + Xavier initialization
  굳이 RBM을 하지 않고 간단하게 좋은 초기값을 줄 수 있다.
  입력값 개수+출력값 개수/루트(입력값 개수)를 이용해서 weight의 초기값을 주면 학습이 잘 된다.
 + He initialization
  Xavier initialization / 2 하면 더 잘 된다.

+ Overfitting
 학습데이터를 이용해 평가를 한 것과 실제 데이터를 이용해 평가를 진행했을 때, 학습데이터에 대한 평가가 더 잘 나오면 overfitting이 발생한 것이다.이를 해결하기 위한 방법은 아래에 있다. 네트워크가 깊을수록 오버피팅이 더 잘 발생한다.
 
+ Dropout
 기존 뉴럴 네트워크에서 임의의 뉴럴들의 연결을 끊어버려서 학습을 진행할 때, 모든 뉴럴을 사용하지 않고 학습을 한다. 그 후 평가할 때는 모든 뉴럴을 이용해서 평가해야한다.

+ Ensemble
 여러 개의 네트워크(모델)를 각각 따로 학습시킨다. 그 후 결과를 출력할 때 네트워크의 결과값을 합쳐서 출력한다.

+ Fast forward
 네트워크에서 뉴럴을 앞으로 몇 단계 뛰어 넘으면서 학습한다.

