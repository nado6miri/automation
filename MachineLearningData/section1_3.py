import numpy as np

np.random.seed(12345)

print("\n[선형대수]\n")

# 행렬의 곱셈,분할,행렬식, 정사각 행렬같은 선형대수 함수 제공
# matlab같은 언어와 다르게 2개의 2차원 배열을 * 연산자로 곱하는건 행렬의 곱셈이 아니라 대응하는 각각의 원소의 곱을 계산하는 것임.
x = np.array([[1,2,3], [4,5,6]])
y = np.array([[6,23], [1, -7], [8,9]])
print("x.dot(y) = ", x.dot(y))

print("\n", np.dot(x, np.ones(3)))

from numpy.linalg import inv, qr
x2 = np.random.randn(5,5)
print("x2 = ", x2)
print("x2.T = ", x2.T)
mat = x2.T.dot(x2)
print("mat = ", mat)
print("\ninv(mat) = ", inv(mat))

q, r = qr(mat)
print("q = \n", q)
print("r = \n", r)

data = np.identity(6)
print("identity = ", data)

print("\n[난수생성]\n")
# 4x4 크기의 정규 분포로 부터 표본을 생성함
samples = np.random.normal(size=(4,4))
print("random.normal = ", samples)

np.random.seed(1234)

data1 = np.random.rand(3,3) # 3*3 균등분포
data2 = np.random.randint(0, 3) # 0~3 정수값
data3 = np.random.randn(3,3) # 3*3 정규분포
data4 = np.random.normal(size=(3,3)) # 3*3 정규분포

print("rand = ", data1)
print("randint = ", data2)
print("randn = ", data3)
print("randnormal = ", data4)