#ex20250319_2

#if statement 

pocket = ['paper','money','cellphone']

if 'money' in pocket:
    print("돈 있음")
    pass
    print("돈 있음2")
else:
    print("돈 없음")

#Page 143
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=", ")
    print(' ')
    
#Page 146 - Q1 - Page 333
    
#Page 146 - Q2 - Page 334
result = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result += i
    i += 1
    
print("출력 값 : ",result)

    
#Page 146 - Q3 - Page 334
i = 0
while True:
    i += 1
    if i > 5: break
    #print("*",end="")
    print("출력 값","*"*i)