#memo_test_20250415_1.py

#입력받은 재용을 저장하고 읽을 수 있는 기능.
#입력 및 읽기 여부 결정. 
#입력 선택시 글을 입력 받아 저장.(특정 파일 지정함.) 
#읽기 선택시 저장한 파일의 글을 보여준다. 
#파일을 선택하여 쓰기/읽기는 없음. 


import sys 
import time

#time.strftime('%Y.%m.%d - %H:%M:%S') # 년.월.일 - 시간
print("실행시각 : ", time.strftime('%Y.%m.%d - %H:%M:%S'))
print("memo_test_20250415_1.py : 파일 입출력 테스트")
print("출력 1 : ",sys.argv)

f_name = "meno_test.txt"

fstatement = input("기록할 내용을 입력 하세요 : ")

#파일 생성
fd = open(f_name,"a")
#파일 쓰기
fd.write(fstatement)
fd.write("\n")
#파일 닫기
fd.close()

#파일 읽기
fd = open(f_name,"r")
f_line = fd.read()
print(f_line)


print("\n")

