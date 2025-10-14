#ex20250408_2.py 

#상속받는 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩이라고 부른다.
#예외 처리 기법은 상황에 맞게 구현해야 한다. 

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    
# 1.예외처리 방법
#say_nick("천사")
#say_nick("바보")


# 2.예외처리 방법 
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명 입니다.")