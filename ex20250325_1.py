#ex20250325_1


#Page 179 - Q5 - Page 337
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close() #파일 쓰기후 반드시 닫아 주어야 한다.

f2 = open("test.txt",'r')
print(f2.read())


#Page 179 - Q6 - Page 337
atxt = "park hong joon"
f1 = open("test.txt",'a')
f1.write("Life is too short 222")
f1.write("\n\n")
f1.write("Life is too short 333")
btxt = atxt.replace("joon","joon2")
f1.write("\n\n")
f1.write(btxt)

f1.close() #파일 쓰기후 반드시 닫아 주어야 한다.

f2 = open("test.txt",'r')
print(f2.read())
