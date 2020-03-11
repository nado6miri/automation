import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

obj = pd.Series([4, 7, -5, 3], index = ['a', 'b', 'c', 'd'])
print("obj = ", obj)
print("obj[obj > 2] = ", obj[obj > 2])
print("obj*2 = ", obj*2)
print("np.exp(obj) = ", np.exp(obj))

data = { 
    'state' : [ 'Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada' ],
    'year' : [ 2000, 2001, 2002, 2001, 2003, 2003 ],
    'pop' : [ 1.5, 1.7, 3.6, 2.4, 2.9, 3.2 ],
}

frame = pd.DataFrame(data)
print("Data Dic = \n", data)
print("pd.DataFrame(data) = \n", frame)

frame = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
print("frame = \n", frame)
print("frame.columns = \n", frame.columns)
print("frame['state'] = \n", frame['state'])
print("frame.year = \n", frame.year)
print("frame.loc['two'] = \n", frame.loc['two'])

frame['debt'] = 20
print("frame = \n", frame)
frame['debt'] = np.arange(6)
print("frame = \n", frame)

print("frame.values = \n", frame.values)
