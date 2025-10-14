#ex20250318_1

print("PHJ")

a={'a1':'a11', 'a2':'a22', 'a3':'a33'}
#a.keys()
print("print a dict_keys ->",a.keys())
print("print a dict_values ->",a.values())
print("print a.dict_items->",a.items())
#print("print a.dict_items->",a.items('a1')) #false statsments
print("print a.get->",a.get('a1')," , ",a.get('a2'), ' , ',a.get('a2','a3'))

a.clear()
print("print a.clear after ->",a.items())

#set
s1 = set("Park Hong Joon")
s2 = set("park seo young")
print("print s1 set -> ",s1)
print("print intersection s1, s2 -> ",s1&s2)
print("print intersection s1, s2 -> ",s1.intersection(s2))
print("print union s1, s2 -> ",s1|s2)
print("print union s1, s2 -> ",s1.union(s2))
print("print difference s1, s2 -> ",s1-s2)
print("print difference s1, s2 -> ",s1.difference(s2))
print("print difference s2, s1 -> ",s2-s1)
print("print difference s2, s1 -> ",s2.difference(s1))

#boolean
print("Boolean 2=2, 2>1, 2<1 -> ", 2==2, 2>1, 2<1)

#Page 112 - Q1
z1 = 80
z2 = 75
z3 = 56
ztot = z1 + z2 + z3
print("z1 = ",z1)
print("z2 = ",z2)
print("z3 = ",z3)
print("ztot = ",ztot, ", z average = ",ztot/3)


#Page 112 - Q2
#znum = 14
znum = input("숫자를 입력하세요 : ")
znum = int(znum)
print("znum = ", znum , " , znum / 2 = ",znum/2," , znum%2 = ",znum%2)
print("bool(znum%2) -> ",bool(znum%2)) 
if(bool(znum%2)) :
    print(znum, "은 홀수 입니다") 
else :  
    print(znum, "은 짝수 입니다") 

