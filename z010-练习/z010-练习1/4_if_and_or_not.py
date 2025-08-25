mood_index=int(input("对象今天的心情指数为："))
at_home = str(input("对象今天是否在家："))
if mood_index<=30 and at_home=="否" or "不在":
    print("得过且过")
else :
    print('好好好')