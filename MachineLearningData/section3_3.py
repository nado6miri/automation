import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

# Data 변경
print("[문자열 처리]")
print("1. 문자열 처리 method")

val = 'a,b, kim'
print("val = \n", val.split(','))
pieces = [ x.strip() for x in val.split(',')]
print("pieces = \n", pieces)

first, second, third = pieces
print("\n '::'.join(pieces) = ", '::'.join(pieces))
print("val.index(',') = \n", val.index(','))
print("val.count(',') = \n", val.count(','))

print("val.replace(',', '::') = ", val.replace(',', '::'))

print("2. 정규 표현식 - re 모듈(패턴매칭, 치환,분리)")
import re

text = 'foo  bar\t bax  \tqux'
print("text = \n", text)
print("\n re.split('\s+', text) = \n", re.split('\s+', text))

regex = re.compile('\s+')

print("regex.split(text) = \n", regex.split(text))
print("regex.findall(text) = \n", regex.findall(text))

text = '''Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com'''

print("text = \n", text)

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(" findall = ", regex.findall(text), "\n")

m = regex.search(text)
print("text = ", text[m.start():m.end()], "\n")

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@lge.com')
print("m.groups() = ", m.groups(), "\n")





