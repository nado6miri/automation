import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

# Data 변경
print("[Data 변형]")
print("1. Data의 중복제거")
data = pd.DataFrame({'k1' : ['one'] * 3 + ['two']*4, 
                    'k2' : [1,1,2,3,3,4,4]})

print("\ndata = \n", data)
print("\ndata.duplicated() = \n", data.duplicated())
print("\ndata.drop_duplicates() = \n", data.drop_duplicates())
print("\ndata.drop_duplicates(['k1']) = \n", data.drop_duplicates(['k1']))
print("\ndata.drop_duplicates(['k1, k2']) = \n", data.drop_duplicates(['k1', 'k2']))
print("\ndata.drop_duplicates(['k1, k2'], keep = 'last) = \n", data.drop_duplicates(['k1', 'k2'], keep = 'last'))

print("2. Data의 매핑")
data = pd.DataFrame({'food' : ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                        'ounces' : [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print("data = \n", data)

meat_to_animal = {
    'bacon' : 'pig',
    'puuled pork' : 'pig',
    'pastrami' : 'cow',
    'corned beef' : 'cow',
    'honey ham' : 'pig',
    'nova lox' : 'salmon'
}

#'food'의 data를 소문자로 변경 후 meat_to_animal에서 mapping하여 data['animal']에 추가한다.
data['animal'] = data['food'].map(str.lower).map(meat_to_animal) 
print("mapped data = \n", data)
