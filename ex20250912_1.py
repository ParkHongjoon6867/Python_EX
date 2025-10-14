# ex20250912_1.py

print("\n===== Program START ====================================")

file_name = "C:\\Users\\user\\Downloads\\역사연표_0912.txt"
print("읽을 파일 : ",file_name)

fd = open(file_name, 'rt', encoding='UTF8')
s = fd.read()
print("파일 내용 : ",s)
fd.close


print("\n=========================================")

with open(file_name, 'rt', encoding='UTF8') as fd1:    
    lines = fd1.readline()
    print(lines)
    lines = fd1.readline()
    print(lines)
    while fd1 == '':   # EOF : End Of File . 원하는 대로 작동하지 않음. 
        print("파일 끝 !")
    
    

print("\n파일 한번에 읽기=========================================\n")

with open(file_name, 'rt', encoding='UTF8') as fd1:    
    lines = fd1.readlines()
    print(lines)
    

print("\n파일 한줄씩 읽기=========================================\n")

search_str = ["연표"]
read_str = []
#fd2 = open(file_name, 'rt', encoding='UTF8')
print("찾는 문자열 : ",search_str)
with open(file_name, 'r', encoding='UTF8') as fd2:  
    while True:
        s2 = fd2.read()
        read_str = s2
        #print("read_str : ",read_str)
        
        if s2 == '':
            break
        elif search_str in read_str: # 오류 발생. 잰행 중지함.
            print(s2)
fd2.close


print("\n===== Program END ====================================\n")


