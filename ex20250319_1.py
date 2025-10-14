#ex20250319_1

from typing import List


#Page 112 - Q3


pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print("yyyymmdd = ",yyyymmdd)
print("num = ",num)


#Page 113 - Q4
print("성별 식별자 : ",pin[7])

#Page 113 - Q5
a = "a:b:c:d"
b = a.replace(":","#")
print("문자열 변경 : ",b)

#Page 113 - Q6
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#Page 114 - Q7 - Page 331
a = ['Life', 'is','too','short']
print("입력 값 : ",a)
result = " ".join(a)
print("출력 값 : ",result)

#Page 114 - Q8 - Page 332
a = (1,2,3)
a = a + (4,)
print(a)

#Page 115 - Q10 - Page 332
a = {'A':90,'B':80,'C':70}
print("출력 값 제거 전 : ", a)
result = a.pop('B')
print("출력 값 제거 후 : ",a)
print("제거된 값 : ",result)

#Page 115 - Q11 - Page 333
a = [1,1,1,2,2,3,3,3,4,4,5]
print("입력 값 : ",a)
aSet = set(a)
print("중복제거 집합 값 : ",aSet)
b = list(aSet) # List <> list
print("집합의 리스트 값 : ",b)