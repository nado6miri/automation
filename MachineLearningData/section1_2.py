import numpy as np

np.random.seed(12345)

print("\n[np array 유니버셜 함수 ufunc]\n")

arr = np.arange(10)
print("arr = ", arr, " np.sqrt = ", np.sqrt(arr))
print("arr = ", arr, " np.exp = ", np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)
z = np.maximum(x, y)
print("x = ", x)
print("y = ", y)
print("z = ", z)

print("\n[where 함수]\n")
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x, y, c in zip (xarr, yarr,cond)]
print("result = ", result)

result2 = np.where(cond, xarr, yarr)
print("result2 = ", result2)

arr = np.random.randn(4,4)
result = np.where(arr>0, 2, -2)
print("result = ", result)

result = np.where(arr>0, 2, arr)
print("result = ", result)

print("\n[수학 메서드와 통계 메서드]\n")
arr = np.random.randn(5,4)
print("arr = ", arr)

print("mean1 = ", arr.mean())
print("mean2 = ", np.mean(arr))
print("sum = ", arr.sum())

print("\n", arr.mean(axis=1)) # row축
print("\n", arr.sum(axis=0)) # col축

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print("\n arr.cumsum() = ", arr.cumsum())

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("\n arr.cumsum(axis = 1) = ", arr.cumsum(axis=1))
print("\n arr.cumsum(axis = 0) = ", arr.cumsum(axis=0))
print("\n arr.cumprod(axis = 1) = ", arr.cumprod(axis=1))
print("\n arr.cumprod(axis = 0) = ", arr.cumprod(axis=0))

print("\n[불리언 배열을 위한 메서드]\n")
arr = np.random.randn(100)
(arr>0).sum() # arr[(arr>0)]과 동일함.
print("arr = ", arr)
print("(arr>0).sum() = ", (arr>0).sum())

# any 함수는 요소의 값이 True가 하나라도 있으면 True 그렇지 않으면 false
# all 함수는 요소의 모든 값이 True일때 True 그렇지 않으면 False 리턴...
print("\n[any, all method]]\n")
arr = np.random.randn(100)
print("(arr>0).sum() = ", (arr>0).sum())

bools = np.array([[False, False, True, False], [False, False, False, False]])
print(bools.any(axis=1), "\n")
print(bools.all(axis=0), "\n")

data = np.random.randn(10,4)
data = data * 2
print("\ndata = ", data)
#행값을중에 3보다 큰 값이 하나라도 있으면 그 행을 가져온다.
print("\ndata[(data>3).any(axis=1)] = ", data[(data>3).any(axis=1)]) 

# 정렬 및 집합함수
print("\n[Sort]\n")
arr = np.random.randn(3,3)
print("arr = ", arr)

arr.sort(axis=1)
print("arr.sort(axis=1) = ", arr)

arr.sort(axis=0)
print("arr.sort(axis=0) = ", arr)

intData = np.array([3,3,3,2,2,1,1,4,4])
print("unique = ", np.unique(intData))
values = np.array([6, 0, 0, 3, 2, 5, 6])
print("union = ", np.union1d(values, [2,3,6]))
print("intersection = ", np.intersect1d(values, [2,3,6]))
print("diff = ", np.setdiff1d(values, [2,3,6]))


