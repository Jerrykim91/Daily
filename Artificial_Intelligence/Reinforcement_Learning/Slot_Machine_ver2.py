import numpy as np
import pandas as pd
import random
import math

import matplotlib.pyplot as plt

class Machine():
    # 속성 - 확률
    def __init__(self,p):
        # 확률이라는 속성을 부여 
        self.percentage = p
        # 외부에서 입력된 p로 인해 값이 초기화
        
    # 보상
    def reward(self):
        # 머신 선택시 보상 지급 
        # 세팅된 확률보다 랜덤 값이 적으면 1 아니면 0 
        if self.percentage > random.random():
            return 1.0
        else:
            return 0.0

# 랜덤 값의 범위 확인
# print([ random.random() for n in range(10)])

# Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]
# print(Machines) # 확인용

class Engine():
    # 초기화 함수 -> 알고리즘에 필요한 값을 초기화
    def initialize(self):
        # 값을 초기화
        pass

    def select_machin(self):
        # 기계를 선택
        pass

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self):
        # 파라미터를 핸들링
        pass
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        pass
    

"""
# Engine Class
- 표준 인터페이스
- 알고리즘 2개를 사용 예정 
"""


class UCB1_Engine(Engine):
       
    """
    #  UCB1 알고리즘

    - 1. 선택한 팔의 시행 횟수 +1
    - 2. 성공시(보상을 받으면), 선택한 팔의 성공 횟수 +1
    - 3. 시행 횟수가 0인 팔이 존재하는 경우, 가치를 갱신하지 않는다 => 0으로 나눌 수가 없어서
    - 4. 시행 횟수가 모두 0이상이면, 팔의 가치에 대해서 탐색과 이용에 대한 균형을 잡는다는 대전에 하에, 모든 팔의 가치를 갱신한다.

    - 모든 팔을 한번 이상 사용할때까지는 가치 갱신을 하지 않는다 => 탐색
    - 모든 팔을 최소 1회 이상 사용해 봤다면, 전체 arm에대 가치 갱신을 시도한다.

    """ 

    def initialize(self):
        # 값을 초기화
        # 시행 횟수
        # 팔의 가치 
        # 성공 횟수
        pass

    def select_machin(self):
        # 기계를 선택
        # 모든 머신을 한번씩 선택 
        # 그중에 값이 큰 머신을 선택 -> argmax()
        pass

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self):
        # 파라미터를 핸들링
        # 선택한 암의 시행 횟수(행동)+1 -> 시도에 대한 횟수 증가 
        # 만약 보상을 받았다면, 성공 횟수를 증가 -> 총 보상 + 1 
        # 시행 횟수가 0인 머신이 존재할 경우 -> 갱신하지 않는다. 
        # 
        # UCB1의 수식에 의해 모든 머신에 대한 가치 갱신
            # 성공률       = (개별 머신의 성공 수)/(개별 머신의 시행횟수)
            # 바이어스     = ( (2*math.log(모든 시행 횟수))/(개별 머신의 시행횟수) )**0.5
            # 개별팔의가치 = 성공률 + 편향(바이어스)
        # 
        pass
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        return 'UCB1 알고리즘'



def simulator(algo, Machines, simulator_cnt, episode_cnt):

    times   = np.zeros(simulator_cnt * episode_cnt) #'횟수'
    rewards = np.zeros_like(times)#'보상'

    # 시뮬 동작
    for action in range(simulator_cnt):
        # 주어진 팔의 개수만큼 자료구조를 생성 -> 0으로 초기화 
        algo.initialize(len(Machines))

        for time in range(episode_cnt):
            offset         = episode_cnt * action
            index          = offset + time
            times[index]   = time + 1 
            choice_machine = algo.select_machin()
            new_reward     = Machines[choice_machine].reward()
            rewards[index] = new_reward
            # 경험을 업데이트 
            algo.policyUpdate(choice_machine, new_reward)

    return times, rewards



# 시뮬레이터     
# 머신을 준비 -> 각 확률을 부여 
Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]  # 30%, 50%, 90%
# print(Machines) 
# 1개의 알고리즘 
algos = [UCB1_Engine()]
# 알고리즘 별로 시뮬레이션을 1000번
SIMULATION_COUNT = 1000
# 1번의 시뮬레이션에서는 250의 에피소드가 존재
EPISODE_COUNT    = 250

for algo in algos:
    result = simulator(algo, Machines, SIMULATION_COUNT , EPISODE_COUNT )
    # print(result)
    df      = pd.DataFrame( {'times':result[0], 'rewards':result[1]} )
    tmp     = df.groupby( 'times' ).mean()
    # 시각화(선형 차트)
    plt.plot( tmp, label=algo.Algo_Naming() )

# 그래프 표시
plt.xlabel('Episode')
plt.ylabel('Reward Average')
plt.legend(loc='best')
plt.show()