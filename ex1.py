
print("1.Park hongjoon !!!")  # => 1.Park hongjoon !!!
print("2.Park hongjoon !!! ' ")  # => 2.Park hongjoon !!! ' 
print('"3.Park hongjoon !!! " ')  # => "3.Park hongjoon !!! "

print("4.Park hongjoon !!! \' ")  # => 4.Park hongjoon !!! '
print("5.Park hongjoon !!! \" ")  # => 5.Park hongjoon !!! "
print("\"6.Park hongjoon !!! \" ")  # => "6.Park hongjoon !!! "
print("7.Park hongjoon !!! %d" %3.1)  # => 7.Park hongjoon !!! 3
print("8.Park hongjoon !!! %d , %f" %(3.1, 3.0))  # => 8.Park hongjoon !!! 3 , 3.000000
print("\n")

y = float(3.14 * 2)
print(y)
y = 3.14 ** 2 # power of 2 : comments
print(y)

#행렬 : matrix 

import numpy as np

a_matrix = np.matrix([[2, 5], [1, 3], [6, 1]])      # numpy.matrix를 사용하여 a행렬 생성
b_matrix = np.matrix([[3], [2]])                    # numpy.matrix를 사용하여 b행렬 생성
c_matrix = a_matrix*b_matrix                        # numpy.matrix의 행렬의 곱 연산
print(c_matrix)                                     # 행렬의 곱 연산 결과 출력
print(type(c_matrix))                               # matrix의 type 출력

a_array = np.array([[2, 5], [1, 3], [6, 1]])        # numpy.array를 사용하여 a행렬 생성
b_array = np.array([[3], [2]])                      # numpy.array를 사용하여 b행렬 생성
c_array = a_array @ b_array                         # numpy.array의 행렬의 곱 연산
print(c_array)                                      # 행렬의 곱 연산 결과 출력
print(type(b_array))                                # array의 type 출력


#2차원 그래프
import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4])
#plt.show()

#3차원 그래프
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
ax.plot(x, y, z)
plt.show()