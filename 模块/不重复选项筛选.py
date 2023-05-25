import random


def diff_many(main_list,frequency,*num) :
    #main,最初的列表;frequency,进行几次筛选;*num,不同次次筛选时应选出几个元素
    for j in range(frequency) :
        xuan_qu_zhi=random.sample(main_list,num[j])
        print(xuan_qu_zhi)
        for i in xuan_qu_zhi :
            main_list.remove(i)


def diff_only(main_list,frequency,num) :
    # main,最初的列表;frequency,进行几次筛选;num,每次次次筛选时应选出几个元素
    for j in range(frequency) :
        xuan_qu_zhi=random.sample(main_list,num)
        print(xuan_qu_zhi)
        for i in xuan_qu_zhi :
            main_list.remove(i)

