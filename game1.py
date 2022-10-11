# 唐僧大战白骨精

# 身份选择
print("==================欢迎光临唐僧大战白骨精游戏==================")
print("请选择你的身份：")
print("\t1. 唐僧")
print("\t2. 白骨精")
player_choice = input("请选择[1-2]： ")

# 打印一条分割线
print("="*49)

# 游戏进行
if player_choice == '1':
    print('你已经选择了1，你将以->唐僧<-的身份来进行游戏')
elif player_choice == '2':
    print('你竟然选择了白骨精，系统将自动分配身份，你将以->唐僧<-的身份来进行游戏')
else:
    print('你的输入有误，系统将自动分配身份，你将以->唐僧<-的身份来进行游戏')

# 打印一条分割线
print("="*49)

# 进入游戏
player_assault = 2    # 攻击力
player_live = 3    # 生命值

boss_assault = 10
boss_live = 10

# 显示玩家的信息（攻击力，生命值）
print(f"你的身份是->唐僧<-，你的攻击力是：{player_assault}，你的生命值是：{player_live}")

# 打印一条分割线
print("="*49)

while True:

    # 选择玩家可以进行的操作
    print("\t1. 练级")
    print("\t2. 打BOSS")
    print("\t3. 逃跑")
    game_choose = input("请选择你要做的操作[1-3]： ")

    # 处理用户的选择
    if game_choose == "1":
        # 增加玩家的生命值和攻击力
        player_live += 2
        player_assault += 2
        print("恭喜你升级了")
        # 显示玩家的信息（攻击力，生命值）
        print(f"你的身份是->唐僧<-，你现在的攻击力是：{player_assault}，你的生命值是：{player_live}")
    elif game_choose == "2":
        # 玩家攻击BOSS
        # 减去BOSS的生命值，减去的生命值应该等于玩家的攻击力
        boss_live -= player_assault
        # 打印一条分割线
        print("="*49)
        print("唐僧攻击了白骨精")
        # 检查BOSS是否死亡
        if boss_live <= 0:
            # BOSS死亡，玩家胜利，游戏结束
            print(f"白骨精受到了{player_assault} 点伤害，重伤不治，唐僧赢得了胜利")
            # 游戏结束
            break
        # BOSS要反击玩家
        # 减去玩家的生命值
        player_live -= boss_assault
        print('白骨精攻击了唐僧')
        # 检查玩家是否死亡
        if player_live <= 0:
            # 玩家死亡，BOSS胜利，游戏结束
            print(f"唐僧受到了{boss_assault} 点伤害，重伤不治，GAME OVER！")
            # 游戏结束
            break

    elif game_choose == "3":
        # 逃跑，退出游戏
        print("唐僧一扭头就跑了")
        break
    else:
        print("你的输入有误，请重新输入")

