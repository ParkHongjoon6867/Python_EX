# ex20250915_1.py

# 파일 읽기 정보
fileread_dir = "C:\\Users\\user\\Downloads\\"
fileread_nm1 = "history_20250915"
fileread_ext = ".txt"
fileread_nm = fileread_dir + fileread_nm1 + fileread_ext
print("읽을 파일 : ", fileread_nm)
#파일 쓰기 정보
filewrt_dir = "C:\\Users\\user\\Downloads\\"
filewrt_nm1 = "history_20250915_bak"
filewrt_ext = ".txt"
filewrt_nm = filewrt_dir + filewrt_nm1 + filewrt_ext
print("쓰기 파일 : ", filewrt_nm)

find_str = ('실록','연표','고려사')

print("\n================================================\n")

with open(filewrt_nm, 'w', encoding='utf-8') as fdwrt :
    with open(fileread_nm, 'r', encoding='utf-8') as fdread :
        while True:
            str = fdread.readline()
            if not str:
                break
            print(str.strip())
            for i in range(len(find_str)):
                if find_str[i] in str:
                    print(str)
                    fdwrt.write(str)
            
fdread.close
fdwrt.close

print("\n=== END =============================================\n")

