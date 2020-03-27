#### ML 4강 multi-variable linear regression
> 지금까지는 Linear regression의 원리를 파악하기 위해 1개의 입력값으로만 설명을 했다면, 실제 머신러닝에서 쓰이는 여러 개의 입력값에 대해  Linear regression이 적용되는지 알아보자.

![그림5.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image5.png) 
> 위 그림은 여러 시험점수를 입력값으로 받아 최종 점수를 출력하는 것을 표로 나타낸 것이다.

+ Multi-variable linear regression의 표현
이전 까지는 입력값이 1개였고, 그에 따라 가설을 세우면 H(x)=wx+b라고 표현할 수 있었다. 위와 같이 여러 개를 입력값으로 받는 것은 아래와 같이 표현할 수 있다.

![그림6.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image6.png)

쉽게 생각해서 입력값에 대해 각각의 가중치를 부여해주면 된다.

![그림8.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image8.png)

위 그림은 매트릭스로 표현을 했다. 일반적으로 매트릭스로 표현한다. 

+ Multi-variable linear regression의 cost

![그림7.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image7.png)

cost를 구하는 방법도 이전과 동일하다.

####ML 5강 Logistic Classification의 가설 함수 정의

시험공부 시간에 따라 합격 / 불합격을 판별해주는 프로그램이 있다고 생각하자. 이 프로그램은 출력값 0과 1 두 개로 충분하다. 
5시간 이상 공부한 사람에게 합격을 준다고 가정하면 5시간도 합격, 10시간도 합격, 100시간도 합격이다. 
이는 우리가 알고 있는 가설의 기본식인 H(x)=wx+b로 표현할 수 없을 것이다. (합격 기준이 무너질 수도 있으며, 출력값이 0과 1을 벗어날 수 있다.)
이를 해결하기 위해 sigmoid function을 이용한다.

+ Sigmoid Function(Logistic Function)
 어떠한 입력값에도 0과 1사이의 값으로 출력해준다.
 식은 아래와 같이 생겼다. 
 
![그림9.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image9.png)
> 그림에서 말하는 -W^T^X는 오타이며 -WX가 맞고, WX는 4강에서 배웠듯 H(x)를 매트릭스로 표현한 것이다.

+ Cost function for Sigmoid Function
 코스트를 구하는 방법은 실제 출력값(y)과 기대 출력값(H(x))의 차이를 구하는 것은 같으나, 식이 조금 달라졌다.
 
![그림10.png](https://github.com/Jangbyeongwook/firstgit/blob/master/study/image10.png)
>식이 길어보이지만, 실제 출력값(y)이 0 또는 1이기 때문에 사라지는 것이 있어서, 길지 않다.

+ Cost 최소화
 여기서 또한 Gradient descent Algorithm을 이용해서 cost 최소화를 진행한다.




