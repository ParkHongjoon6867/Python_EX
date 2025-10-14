# ex20250905_1.py

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print("초기 딕셔너리 ",x, "\n")

x.setdefault('a1')
print("딕셔너리 추가",x)

x.setdefault('a2')
print("딕셔너리 추가",x)

x.setdefault('a3',80)
print("딕셔너리 추가",x)

x.update(a3=81)
print("딕셔너리 변경",x)

x.update(a4=90)
print("딕셔너리 변경",x)

x.pop('a1')
print("딕셔너리 삭제",x)

print("\n=====================================================")
