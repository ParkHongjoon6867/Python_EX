#ex20250408_3.py 

#내장함수 - import가 필요 없다. 

#positive.py 
def positive(l):
    result = []
    print("입력 항목의 갯수 : ",len(l))
    for i in l:
        print("출력 항목 : i -> ",i)
        if i > 0:
            #print(i)
            result.append(i)
        return result
    
print(positive([1,-3,2,0,-5,6]))

