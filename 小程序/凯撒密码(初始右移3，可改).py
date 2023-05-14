mi_ma=input("请输入需要转换的文本：")
print("如果是密文文本，则以下是明文：")
for i in mi_ma:
    if "a" <= i <="z" :
        new1=chr(ord("a")+(ord(i)-ord("a")+3)%26)
        print(new1,end="")
    elif "A" <= i <="Z" :
        new2=chr(ord("A")+(ord(i)-ord("A")+3)%26)
        print(new2,end="")
    else:
        print(i,end="")
print("\n\n")
print("如果是明文文本，则以下是密文文本：")
for i in mi_ma:
    if "a" <= i <="z" :
        new1=chr(ord("a")+(ord(i)-ord("a")-3)%26)
        print(new1,end="")
    elif "A" <= i <="Z" :
        new2=chr(ord("A")+(ord(i)-ord("A")-3)%26)
        print(new2,end="")
    else:
        print(i,end="")
