# ex20250913_1.py


print("\n===== ex20250913_1.py START ====================================\n\n")

file_name = "C:\\Users\\user\\Downloads\\역사연표_0913.txt"
print("읽을 파일 : ",file_name)


print("\n===== 딕셔너리 사용 실패 ====================================\n")

st2 = {"연표","실록"}
print("찾는 문자열 : ",st2)

#with open(file_name, 'r', encoding='UTF8') as fd2:  
#    while True:
#        s2 = fd2.readline()
#        if s2 == '':
#            break
#        if s2.find(st2) != -1:  
#            print(s2)
#fd2.close


print("\n===== 리스트 사용 ====================================\n")


search_str = ["연표","실록"]
#search_str[1] = "연표"
#search_str[2] = "실록"

print("찾는 문자열 : ",search_str[0])

with open(file_name, 'r', encoding='UTF8') as fd2:  
    while True:
        s2 = fd2.readline()
        if s2 == '':
            break
        if s2.find(search_str[1]) != -1:  # while을 이용한 리스트의  반복이 필요하다.
            print(s2)
fd2.close

print("\n===== 리스트 for, while 사용 ====================================\n")

for i in range(len(search_str)):
    print("찾고 싶은 문자열 : ",search_str[i])

with open(file_name, 'r', encoding='UTF8') as fd2:
    for line in fd2:
        for i in range(len(search_str)):
            #print(i,search_str[i])
            if s2.find(search_str[i]) != -1:  # while을 이용한 리스트의  반복이 필요하다.
                print(line.strip('\n'))
fd2.close


print("\n===== Program END ====================================\n\n")


