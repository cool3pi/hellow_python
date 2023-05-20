def gonggongshu(a,b) :
    c=a*b
    while b :
        d=a%b
        a=b
        b=d
    print("两者最大公约数为：",a)
    print()
    print("两者最小公倍数为：",c//a)
    e={"两者最大公约数":a,"两者最小公倍数":c//a}
    return e
print(gonggongshu(15,25))