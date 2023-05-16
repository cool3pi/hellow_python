import random

a=["A",2,3,4,5,6,7,8,9,"J","Q","K"]
pai=[]
for i in a :
    pai.append(("黑桃",i))
    pai.append(("梅花",i))
    pai.append(("红心",i))
    pai.append(("方块",i))
def player_way(num1,playnum,main_list,*num):
    #num1,玩家数量;palynum,屏幕前玩家名字;main_list,含有所有牌的列表;*num,给玩家依次发几张牌
    player = {}
    player_name=[]
    personalyname = input("请本玩家输入你自己的游戏名：")
    for q in range(playnum) :
        if q >= 1:
            jixu = input("是否进入下一局：")
            print("进入下一局")
            print("\n" * 3)
        for j in range(num1) :
            if q==0 :
                name=input("请进入的玩家输入你的游戏名：")
                player_name.append(name)
            elif q>=1 :
                ok=0
            xuan_qu_zhi=random.sample(main_list,num[j])
            player[player_name[j]]=xuan_qu_zhi
            for i in xuan_qu_zhi :
                main_list.remove(i)
        if personalyname=="" :
            ok=2
        elif personalyname in player_name :
            print(player[personalyname])
        ming_pai=input("是否明牌：")
        if ming_pai=="是" :
            print(player)
        elif ming_pai !="是":
            ok=2

ming_pai=player_way(4,100,pai,3,3,3,3)






