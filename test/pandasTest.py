from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])
print(obj)

obj2 = Series([4, 7, -5, 3], index=['d','b','a','c'])
print(obj2)

sdata = {'Ohio':35000, 'Texas':7100, 'Oregon':1600,'Utah':500}
obj3 = Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)

data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada','Nevada'], 'year':[2000, 2001, 2002, 2011, 2002], 'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)

frame2 = DataFrame(data, columns=['year', 'state', 'pop']) # 指定列
print(frame2)

frame3 = DataFrame(data, columns=['year', 'state', 'pop'],index=['one', 'two', 'three', 'four', 'five']) # 指定列和索引
print(frame3)

errors = [('c',1,'right'), ('b', 2,'wrong')]
df = pd.DataFrame(errors)
print(df)

df = pd.DataFrame(errors, columns=['name', 'count', 'result']) # 指定列名
print(df)

# pop = {'Nevada':{2001:2.4, 2002:2.9}, 'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
# frame4 = DataFrame(pop)
# print(frame4)
#
# a = pd.Series([1,2,3])
# b = pd.Series([2,3,4])
# c = pd.DataFrame([a,b])
# print(c)
#
# c = pd.DataFrame({'a':a,'b':b})
# print(c)
#
# import numpy as np
# data = DataFrame(np.arange(16).reshape((4,4)),index=['Ohio', 'Colorado','Utah','New York'],columns=['one','two','three','four'])
# print(data)
# print(data['two'])
# print(data.ix['Ohio'])
# print(data.ix['Ohio', ['two','three']])
# print(data.ix[data.three > 3, :3])

# for ix, row in df.iterrows():
#     print(ix, row)

for ix, col_type in df.iteritems():
    print(ix)
    print(col_type)


# frame = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
# print(frame.sum())