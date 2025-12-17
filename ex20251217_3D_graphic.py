# ex20251217_3D_graphic.py
# 3차원 그래프 그리기.

#시간에 대한 library
from datetime import datetime
from time import sleep

# 그래프 라이브러리
# Axes3D 모듈을 임포트
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("\n=== START : ex20251217_3D_graphic.py "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")


###############################################################################################
print("\n=== 3D 그래프 예제 1 =============================================\n")

# subplot에서 projection을 3d로 선언
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# x좌표, y좌표, z좌표를 따로따로 지정
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
ax.plot(x, y, z)
plt.show()

#3D scatter 선점도 그래프

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
ax.scatter(x, y, z, color = 'r', alpha = 0.5)
plt.show()

# sleep(10) # 초단위 대기.

ax.scatter(x, y, z, color = 'r', alpha = 0.5)
ax.scatter(x, z, y, color = 'g', alpha = 0.5) # y와 z축 swap

# ax.plot_surface라는 평면을 그리는 함수
# z에 선언하는 변수는 2차원의 형태
# x, y로 선언한 좌표를 np.meshgrid를 이용하여 격자 생성

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(0, 10, 0.1)
y = np.sin(x)
x_m, y_m = np.meshgrid(x, y)
z = x_m + 5 * y_m
ax.plot_surface(x, y, z, cmap="brg_r")
plt.show()

###############################################################################################
print("\n=== 3D 그래프 예제 2 =============================================\n")

# from mpl_toolkits import mplot3d # 위에서 이미 선언함.

# import numpy as np # 위에서 이미 선언함.
# import matplotlib.pyplot as plt # 위에서 이미 선언함.

# Figure, Axes &
fig = plt. figure ()
ax = plt.axes (projection='3d')

# x, y, z 축의 데미터 생성
z = np.linspace(0, 1, 200)
x = z * np.sin(30 * z)

y = z * np.cos(30 * z)

# 3D 그래프 생성
ax.plot3D(x, y, z, 'gray')
ax.set_title('Line Plot 3D')
plt.show()

print("\n=== END : ex20251217_3D_graphic.py "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")
