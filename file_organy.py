# file_organy.py
# 파일 정리 - 특정 문자 제거

import os
import glob # 파일 구성 라이브러리
from pathlib import Path
import time
from datetime import datetime

#변수 선언
fileread_nm1 = "history_1"
filewrt_nm1 = "history_1_bak"
# 파일 읽기 정보
fileread_dir = ""
fileread_ext = ".txt"
fileread_nm  = ""
#파일 쓰기 정보
filewrt_dir  = ""
filewrt_ext = ".txt"
filewrt_nm = ""

find_str = ('실록','연표','고려사')

search_folder = "Downloads"
search_in = "Downloads" #찾는 대상
search_out = ["Default","Public","TEMP","AppData"] #제외대상

print("\n=== START : file_organy "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")

def dir1():
    print("\n=== START : dir1() =============================================\n")

    
    cur_path = os.getcwd()
    print("현재 폴더 위치 : ",cur_path)

    all_folder = glob.glob(cur_path+'\\*')
    print("파일 : ",all_folder)

    # 상위 경로로 이동.
    os.chdir("..")
    cur_path = os.getcwd()
    print("현재 폴더 위치2 : ",cur_path)

    # 최상위 경로로 직접 이동
    os.chdir("c:\\")
    cur_path = os.getcwd()
    print("현재 폴더 위치3 : ",cur_path)

    all_folder = glob.glob(cur_path+'*')
    print("파일3 : ",all_folder)


    ## 현재 폴더의 하위에 있는 폴더와 파일(현재 폴더는 포함 안됨)
    print("찾는 폴더 : ",search_folder)
    for f in glob.glob('*//*'): ## 또는 **/**, **/*, */**
        if search_folder in f :
            print("같음, 포함 : ",f)
    


    #all_file = [x for x in all_folder if os.path.isfile(x)]
    #for file_name in all_file:
    #    print(file_name)

    print("\n=== END : dir1() =============================================\n")
    

def dir2():
    print("\n=== START : dir2() =============================================\n")

    
    # 최상위 경로로 직접 이동
    os.chdir("c:\\")
    cur_path = os.getcwd()
    print("현재 폴더 위치 : ",cur_path)

    entries = Path('Temp')

    #print(type(entries),"\n")
    #print(dir(entries),"\n")

    for entry in entries.iterdir():
        print(entry.name)

    print("\n=== END : dir2() =============================================\n")
    

def dir3():
    print("\n=== START : dir3() =============================================\n")

    # 최상위 경로로 직접 이동
    os.chdir("c:\\")
    cur_path = os.getcwd()
    print("현재 폴더 위치 : ",cur_path)
    
    # C:\Users\user\Downloads
    
    all_folder = glob.glob('*//*')
    #print("파일 : ",all_folder)
    print("찾는 폴더 : ",search_folder)
    
            
    #for f in all_folder:
    #    print("확인 : ",f)
    
    for s1 in search_out:
        print("제외폴더:",s1)
        
    for (path, dir, files) in os.walk("C:\\"):
        #print("검사대상0:",path)
        for s1 in search_out:
            if path.find(s1) <= 0 :
                #if path.find(search_in) > 0 : # 단어가 포함되어 있지 않고 단어가 포함되어 있는 경우.
                print("찾은 폴더 위치:",path.find(search_in)," : ",path,"=>",s1) 
                return
            

    print("\n=== END : dir3() =============================================\n")
    

def dir4():
    print("\n=== START : dir4() =============================================\n")
            
    print("찾는 폴더:",search_in)
    print("제외폴더 크기:",len(search_out))   
    for s1 in search_out:
        print("제외폴더:",s1)

    for (path, dir, files) in os.walk("C:\\"):
        #print("검사대상0:",path)
        i = 0
        for s1 in search_out:
            if path.find(s1) > 0 :
                i = i + 1
                #print("i = ",i)
                
            if path.find(search_in) > 0 and i == 0: #제외 대상 등록 갯수만큼 확인했는지 여부.
                print("찾은 폴더 위치:",path.find(search_in),":",s1,"=>", search_in, path,"=>i = ",i,"=>",path.find(s1))
                return

    print("\n=== END : dir4() =============================================\n")
    



#폴더 위치 찾기 완성본.
def dir5():
    print("\n=== START : dir5() =============================================\n")
            
    print("찾는 폴더:",search_in)
    print("제외폴더 크기:",len(search_out))   
    for s1 in search_out:
        print("제외폴더:",s1)

    for (path, dir, files) in os.walk("C:\\"):
        if path.find(search_in) > 0: #찾는 폴더 존재
            i = 0
            for s1 in search_out:
                if path.find(s1) > 0 :
                    i = i + 1
                    
            if i == 0:
                print("찾은 폴더 위치:",path.find(search_in)," : ",path) 
                # 전역변수에 저장
                global fileread_dir
                global filewrt_dir
                fileread_dir = path + "\\"
                filewrt_dir = path + "\\"
                print("위치 : ",fileread_dir)
                return

    print("\n=== END : dir5() =============================================\n")

def file_proc():
    print("\n=== START : file_proc() =============================================\n")

    print("위치 : ",fileread_dir)
                
    fileread_nm = fileread_dir + fileread_nm1 + fileread_ext
    print("읽을 파일 : ", fileread_nm)
    #파일 쓰기 정보
    filewrt_nm = filewrt_dir + filewrt_nm1 + filewrt_ext
    print("쓰기 파일 : ", filewrt_nm)

    with open(filewrt_nm, 'w', encoding='utf-8') as fdwrt :
        with open(fileread_nm, 'r', encoding='utf-8') as fdread :
            while True:
                str1 = fdread.readline()
                str2 = fdread.readline()
                if (not str1) or (not str2):
                    break
                str1 = str1.replace("\n"," - ") # 개행문자 제거
                str = str1 + str2
                for i in range(len(find_str)):
                    if find_str[i] in str:
                        #print(str)
                        fdwrt.write(str)
            
    fdread.close
    fdwrt.close

    print("\n=== END : file_proc() =============================================\n")
    
#dir1()
#dir2()
#dir3()
#dir4()
dir5()
file_proc()

#  폴더 찾기
# Downloads 폴더 찾기 - PC별 위치가 다를 수 있다. - PC 사용자 ID를 특별하게 정의한 경우임.


# history_1 파일 찾기 - 없는 경우 생성.
# history_1_bak 파일 생성.



print("\n=== END : file_organy "+ datetime.now().strftime('%Y.%m.%d - %H:%M:%S')+" =============================================\n")

