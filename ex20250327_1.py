#ex20250327_1

# Page204
# 메서드 오버라이딩 (Overriding, 덮어쓰기)
# : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것.

import mod1
#from mod1 import *

print(mod1.add(3,5))

#a = mod1()
#print(a.add(3,5))
print(mod1.sub(3,5))

# Page 223
# try, except 

try:
    4/0
except ZeroDivisionError as e:
    print(e)
finally:
    print("must run statement ...")
    
