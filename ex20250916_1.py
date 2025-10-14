# ex20250916_1.py


print("\n=== START =============================================\n")

import os 

print("os.name : ",os.name)
cur_dir = os.getcwd()
print("os.getcwd() : ",cur_dir)

del_dir = "C:\\Users\\user\\Downloads"
del_file = del_dir + "\history_20250916_bak.txt"
print("File Delete ?? ",del_file)
#os.remove(del_file)

old_file = "C:\\Users\\user\\Downloads" + "\history_20250917.txt"
new_file = "C:\\Users\\user\\Downloads" + "\history_20250916_1.txt"
#os.rename(old_file, new_file)

file_info = os.stat(old_file)
print("os.stat(old_file) => ",os.stat(old_file))
print("file_info.st_size =>", file_info.st_size)

directory_content = os.listdir('.')
print("현재 디렉토리 => ",directory_content)


print("\nos.environ 1 => ",os.environ)
print("\nos.environ 2 => ",os.environ['PATH'])

import time
print("time.strftime('%Y.%m.%d - %H:%M:%S') => ",time.strftime('%Y.%m.%d - %H:%M:%S') ) # 년.월.일 - 시간
# Output : '2022.04.04 - 01:33:26'
print("time.strftime('%y%m%d - %X') => ",time.strftime('%y%m%d - %X')  ) # 년월일 - 시간
# Output : '220404 - 01:35:57'
print("time.strftime('%x %X') => ",time.strftime('%x %X')  ) # 날짜 - 시간
# Output : '04/04/22 01:37:57'
print("time.strftime('%c') => ",time.strftime('%c')  ) # 전체시간 정보 한번에
# Output : 'Mon Apr  4 01:35:18 2022'
 
from datetime import datetime
## datetime.now()는 위의 time과 같은 기능.
print("datetime.now().strftime('%Y.%m.%d - %H:%M:%S') => ",datetime.now().strftime('%Y.%m.%d - %H:%M:%S')  ) # 년.월.일 - 시간
print("datetime.now().strftime('%y%m%d - %X') => ",datetime.now().strftime('%y%m%d - %X')  ) # 년월일 - 시간
print("datetime.now().strftime('%x %X') => ",datetime.now().strftime('%x %X')  ) # 날짜 - 시간
print("datetime.now().strftime('%c') => ",datetime.now().strftime('%c')  ) # 전체시간 정보 한번에

print("\n=== END =============================================\n", )