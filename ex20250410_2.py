#ex20250410_2.py 

#Q1 : Page 262 -> Page 340
print("연습_1")
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        
        
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print("Q1 출력 값 : ",cal.value)



#Q2 : Page 262 -> Page 340
print("연습_2")

class MacLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
        
        
cal = MacLimitCalculator()
cal.add(50)
cal.add(51)

print("Q2 출력 값 : ",cal.value)


#Q3 : Page 263 -> Page 340
print("연습_3")
print("Q3_1 출력 값 : ",all([1,2,abs(-3)-3]))
print("Q3_2 출력 값 : ",chr(ord('a')) == 'a')


#Q4 : Page 263 -> Page 340
print("연습_4")
print("Q4 출력 값 : ",list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))


#Q6 : Page 264 -> Page 340
print("연습_6")
print("Q6 출력 값 : ",list(map(lambda x:x*3,[1,2,3,4])))

#Q7 : Page 264 -> Page 340
print("연습_7")
str_val = [-8,2,7,5,-3,5,0,1]
print("Q7 출력 값_1 : ",max(str_val))
print("Q7 출력 값_2 : ",min(str_val))

#Q8 : Page 265 -> Page 340
print("연습_8")
val = 17/3
print("Q8 출력 값 : ",val)
print("Q8 출력 값 : ",round(val,4))

#Q13 : Page 265 -> Page 340
import random
print("연습_13")
val = random.randrange(1,45)
print("Q13 출력 값 : ",val)

result = []
while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)
        
print("Q13 출력 값 : ",result)
