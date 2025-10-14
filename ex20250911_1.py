# ex20250911_1.py
# 역사 연표 파일 변경 

file_name = "C:\\Users\\user\\Downloads\\역사연표_0911.txt"
print("읽을 파일 : ",file_name)

fd = open(file_name, 'rt', encoding='UTF8')
s = fd.read()
print("파일 내용 : ",s)
fd.close


print("\n=========================================")

with open(file_name, 'rt', encoding='UTF8') as fd1:    # 역사연표_0911.txt 파일을 읽기 모드(r)로 열기
    lines = fd1.readline()
    print(lines)
    lines = fd1.readline()
    print(lines)
    while fd1 == '':   # EOF : End Of File 
        print("파일 끝 !")
    
    

print("\n=========================================")

with open(file_name, 'rt', encoding='UTF8') as fd1:    # 역사연표_0911.txt 파일을 읽기 모드(r)로 열기
    lines = fd1.readlines()
    print(lines)
    

print("\n===== Program END ====================================")