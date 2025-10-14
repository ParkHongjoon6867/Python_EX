# ex20250912_2.py


file_name = "C:\\Users\\user\\Downloads\\역사연표_0912.txt"
print("읽을 파일 : ",file_name)

search_str[1] = "연표"
search_str[2] = "실록"

print("찾는 문자열 : ",search_str)

with open(file_name, 'r', encoding='UTF8') as fd2:  
    while True:
        s2 = fd2.readline()
        if s2 == '':
            break
        if s2.find(search_str) != -1:
            print(s2)
fd2.close


print("\n===== Program END ====================================\n\n")


