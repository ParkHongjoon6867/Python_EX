#ex20250408_1.py 


try:
    a = [1,2]
    print(a[3])
    4/0
#except ZeroDivisionError as e:
#    print(e)
#except IndexError as e:
#    print(e)
    
#오류 내용을 동시에 처리할 수 있다.
except (ZeroDivisionError,IndexError) as e:
    print(e)
    
    