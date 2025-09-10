mood_index=int(input("对象今天的心情指数为："))
at_home = str(input("对象今天是否在家："))
if mood_index>=60:
    print("今天爽歪歪")
elif mood_index<=30:
    if at_home=="否":
        print("问题不大")
    elif at_home=="是":
        print("直接等死")
else:
    print("一般，普普通通")
