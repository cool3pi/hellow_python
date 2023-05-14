import string

def s_my(mi_ma):
    #mi_ma 是你想要破解的文本或字符串
    def str_list(str):
        new = []
        for i in str:
            new.append(i)
        return new
    def list_str(list):
        new = ""
        for i in list:
            new = new + i
        return new
    mi_ma_n=str_list(mi_ma)
    yuan1=str_list(string.ascii_lowercase)+["a","b","c"]
    yuan2=str_list(string.ascii_uppercase)+["A","B","C"]
    a=-1
    for i in mi_ma_n:
        a += 1
        if i in yuan1:
            old=yuan1.index(i)
            n=yuan1[old+3]
            mi_ma_n[a]=n
        elif i in yuan2:
            old = yuan2.index(i)
            e = yuan2[old + 3]
            mi_ma_n[a] = e
        else:
            continue
    mi_ma_n=list_str(mi_ma_n)
    return mi_ma_n

def rb_my(mi_ma):
    #mi_ma 是你想要破解的文本或字符串
    def str_list(str):
        new = []
        for i in str:
            new.append(i)
        return new
    def list_str(list):
        new = ""
        for i in list:
            new = new + i
        return new
    mi_ma_n=str_list(mi_ma)
    yuan1=str_list(string.ascii_lowercase)
    yuan2=str_list(string.ascii_uppercase)
    a=-1
    for i in mi_ma_n:
        a += 1
        if i in yuan1:
            old=yuan1.index(i)
            n=yuan1[old-3]
            mi_ma_n[a]=n
        elif i in yuan2:
            old = yuan2.index(i)
            e = yuan2[old - 3]
            mi_ma_n[a] = e
        else:
            continue
    mi_ma_n=list_str(mi_ma_n)
    return mi_ma_n




