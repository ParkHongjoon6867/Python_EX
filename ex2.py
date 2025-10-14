
import numpy as np
import matplotlib.pyplot as plt

t1 = np.linspace(-2, 2, 100)

# x와 y 배열 생성
x = 2 * t1
y = t1**2 #+ 2 * t1

# 그래프 그리기
plt.figure(figsize=(8, 6))  # 그래프 크기 설정
#plt.plot(x, y, marker='o', linestyle='-')  # 선 그래프 그리기
plt.plot(x, y, linestyle='-')  # 선 그래프 그리기
plt.xlabel('x')  # x축 레이블 설정
plt.ylabel('y')  # y축 레이블 설정
plt.show()  # 그래프 표시