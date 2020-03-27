####ML 7강 Learning Rate, Overfitting Regularization

+ Learning rate
 한글로 학습률이다. 데이터에 대해 학습을 진행할 때 Learning rate를 적절한 값을 줘야한다.
  + 값이 클 경우
  값이 클 경우, overshooting이 발생한다. overshooting이 발생하면 모델이 학습할 때, 적절한 cost값을 찾지 못하며, 범위 밖으로 벗어날 위험이 있다.
  + 값이 작을 경우
  값이 너무 작을 경우, 학습시간이 매우 오래 걸리며, 때에 따라 최적화 된 cost를 찾지 못하고 학습이 종료 될 수도 있다.

+ Overfitting
 머신러닝에서 발생할 수 있는 큰 문제이다. 학습용 데이터만 가진 채 너무 많은 학습을 진행할 경우 overfitting이 발생한다. 학습용 데이터에 대해 완벽한 학습을 거쳐 완벽한 답을 내놓지만, 테스트용 데이터나 실제 사용할 데이터에 대해서는 기존 모델보다 못한 오차가 발생하며 오류가 날 수 있다.
 + 해결방안
 Training set과 Test set을 나눠야 한다.
 
+ Normalization(Standardization)
 데이터 간의 차이가 심할 경우, 학습이 제대로 진행되지 않는다. 그래서 데이터간의 차이가 심하면,데이터를 다듬어줄 필요가 있다.(일반화? 정규화?)
 
+ Regularization
 Cost를 구할 때, 함수끝에 weight의 가중치를 더해 중요도를 표시하고 이를 이용하여 cost를 구한다.
 
+ Online Learning
 데이터의 양이 광대할 경우, 많은 데이터를 한 번에 학습시키기에는 오래걸릴 뿐더러, 오류가 발생할 가능성이 있다. 따라서 데이터의 양을 분할하여 학습하는 방법이다.
