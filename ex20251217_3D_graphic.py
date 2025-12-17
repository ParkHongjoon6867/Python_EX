# ex20251217_3D_graphic.py
# 3차원 그래프 그리기.

#시간에 대한 library
from datetime import datetime

# 그래프 라이브러리
# Axes3D 모듈을 임포트
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("\n=== START : ex20251217_3D_graphic.py "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")

# subplot에서 projection을 3d로 선언
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# x좌표, y좌표, z좌표를 따로따로 지정
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
ax.plot(x, y, z)

ax.scatter(x, y, z, color = 'r', alpha = 0.5)
plt.show


print("\n=== END : ex20251217_3D_graphic.py "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")
