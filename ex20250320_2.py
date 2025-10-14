#ex20250320_2.py


def add(a,b):
    result = a + b
    return result

print("add의 결과 값 : ", add(3,4)) 


#Page 168
#number = input("숫자 입력 값 : ")

#Page 170
for i in range(10):
    print(i)
    
for i in range(10):
    print(i, end=' ')
    
#Page 171
f = open("D:/test_20250320_2.txt","w")
f.close()

#Page 179 - Q1 - Page 337

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = 4
a = is_odd(number)
if a == True:
    print("입력값 짝수 ")
elif a == False:
    print("입력값 홀수 ")
else: print("모르는 값 ")


#Page 179 - Q2 - Page 337
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print("평균 값 : ",avg_numbers(1,2))
print("평균 값 : ",avg_numbers(1,2,3,4,5))



#Page 179 - Q3 - Page 337
input1 = input("첫번째 입력 값 : ")
input2 = input("두번째 입력 값 : ")

total = int(input1) + int(input2)
print("출력 값 : %s" % total)

#Page 179 - Q4 - Page 337
print("park" "hong" "joon")
print("park", "hong", "joon")