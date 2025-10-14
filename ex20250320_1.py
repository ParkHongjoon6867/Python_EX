#ex20250320_1.py

    
#Page 147 - Q4 - Page 334

for i in range(1,101):
    print("출력 값 : ",i)
    
    
#Page 148 - Q5 - Page 334

A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print("출력 값 : ",average)
    
    
#Page 148 - Q6 - Page 334
numbers = [1,2,3,4,5]

result = []
for n in numbers:
    if n%2 == 1:
        result.append(n*2)
        
print("출력 값 : ", result)


