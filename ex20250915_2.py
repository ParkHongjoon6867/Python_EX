# ex20250915_2.py

#import 정보
import time
from datetime import datetime

# 파일 읽기 정보
fileread_nm1 = "history_1"
filewrt_nm1 = "history_1_bak"

fileread_dir = "C:\\Users\\user\\Downloads\\"
fileread_ext = ".txt"
fileread_nm = fileread_dir + fileread_nm1 + fileread_ext
print("읽을 파일 : ", fileread_nm)
#파일 쓰기 정보
filewrt_dir = "C:\\Users\\user\\Downloads\\"
filewrt_ext = ".txt"
filewrt_nm = filewrt_dir + filewrt_nm1 + filewrt_ext
print("쓰기 파일 : ", filewrt_nm)

find_str = ('실록','연표','고려사')

print("\n=== START "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")

with open(filewrt_nm, 'w', encoding='utf-8') as fdwrt :
    with open(fileread_nm, 'r', encoding='utf-8') as fdread :
        while True:
            str1 = fdread.readline()
            str2 = fdread.readline()
            if (not str1) or (not str2):
                break
            #print(str1.strip())
            #print(str2.strip())
            #str1.strip('\n')
            #str2.strip('\n')
            str1 = str1.replace("\n"," - ") # 개행문자 제거
            str = str1 + str2
            for i in range(len(find_str)):
                if find_str[i] in str:
                    #print(str)
                    fdwrt.write(str)
            
fdread.close
fdwrt.close

print("\n=== END "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")

