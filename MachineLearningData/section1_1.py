import numpy as np

np.random.seed(12345)

print("\n[np array 기본]\n")
data = [6, 7, 8, 0, 1]
arr1 = np.array(data)

print("data = ", data)
print("arr1 = ", arr1)

data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)
print("data2 = ", data2)
print("arr2 = ", arr2)

print("ndim = ", arr2.ndim)
print("shape = ", arr2.shape)
print("dtype = ", arr2.dtype)

arr3 = np.array([1,2,3,4,5], dtype=np.float32)
print("arr3 dtype = ", arr3.dtype)


arr4 = np.arange(10)
print("arr4 = ", arr4)

arr5 = np.zeros((3,4))
print("arr5 = ", arr5)

arr6 = np.ones((3,4))
print("arr6 = ", arr6)

arr7 = np.empty((3,4))
print("arr7 = ", arr7)

# scalar 연산
print("\n[scalar 연산]\n")
ma = np.array([[1, 2, 3], [4, 5, 6]])
print("ma * ma = ", ma * ma)
print("ma + ma = ", ma + ma)
print("ma - ma = ", ma - ma)
print("1/ma = ", 1/ma)

# scalar 색인
print("\n[scalar 색인]\n")
arr = np.arange(10)
print("arr[5] = ", arr[5])
print("arr[5] = ", arr[5:8])

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("arr[:2] = ", arr[:2]) # arr[행,열]인데 ,가 생략된 형태이며 :2 는 시작 0~1까지 행을 의미함.
print("arr[:2, 1:] = ", arr[:2, 1:]) # arr[행,열]인데 1: 는 열의 1~끝가지를 의미함.

# 불리언 배열을 통한 색인방법
print("\n[불리언 배열을 통한 색인방법]\n")
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4) # 7x4 랜덤 행렬을 만든다.

print("names = ", names, "\n")
print("data = ", data)

print("\n", names == 'Bob')
print("\n", data[names == 'Bob'])

print("\n", data[names == 'Bob', 2:])
print("\n", data[names == 'Bob', 3])

#배열 전치와 축이동
print("\n[배열 전치와 축이동 - 팬시색인 - 정수배열을 사용한 색인]\n")
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i

print("\n", arr)
print("\n", arr[[4,3,0,6]]) # arr에서 4열, 3열 0열 6열을 골라 표시한다. 즉 행값을 []형태로 집어 넣는다.
print("\n", arr[[-3, -5, -7]]) # index를 반대로 하기 위해서는 - 값을 붙이고 끝에서 부터 값을 선택한다. -1은 맨 끝을 의미함.

print("\n[배열의 재형성]\n")
arr = np.arange(8)
arr2 = arr.reshape((4,2))
print("arr = ", arr)
print("arr2 = ", arr2)

arr3 = arr.reshape((4,2)).reshape((2,4))
print("arr3 = ", arr3)

arr = np.arange(15).reshape((3,5))
print("arr = ", arr)
print("arr.T transpose method의 T속성 사용 = ", arr.T)
