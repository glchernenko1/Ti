import math

import numpy as np

# q = 3
# p = np.array([0.02, 0.07, 0.01, 0.14, 0.05, 0.45, 0.25, 0.01])
# arr= np.array([5,3,6,2,4,1,2,6])
# # qi = np.zeros(8)
# qi[0] = p[0] / 2
# for i in range(1, 8):
#     for j in range(0, i):
#         qi[i] += p[j]
#     qi[i] += + p[i] / 2
# print(qi)
#
# sum = 0
# for i in range(0, 8):
#     tmp = -p[i] * math.log2(p[i])
#     sum += tmp
#     print(tmp)
# print("Ответ " + str(sum))
# sum=0
# for i in range(0, 8):
#    print(-math.log2(p[i])+1)
# print("Средняя длина"+  str(np.sum( p.dot(arr))))


# Задание 4
old=np.array([0,0.1,0.3,0.55,0.95,1])

def fun(a,b,oldarr):
    newarr = np.zeros(6)
    newarr[0]=oldarr[a]
    newarr[5]=oldarr[b]
    old=oldarr[5]-oldarr[0]
    new=newarr[5]-newarr[0]
    k=new/old
    new_range=np.zeros(5)
    for i in range (0, 6-1):
        new_range[i]=oldarr[i+1]-oldarr[i]

    new_range=new_range.dot(k)
    for i in range(1,6):
        newarr[i]=newarr[i-1]+new_range[i-1]
    return newarr

old=fun(0,1,old)
print(old)
old=fun(1,2,old)
print(old)
old=fun(3,4,old)
print(old)
old=fun(1,2,old)
print(old)
old=fun(0,1,old)
print(old)
print(-math.log2(0.00018)+1)


q=0.02188
str=""
for i in range (0,15):
    q+=q
    if int(q)==1:
        str+="1"
        q=q%1
    else:
        str+="0"
print(str)

