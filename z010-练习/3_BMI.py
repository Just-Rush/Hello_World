user_wight = float(input("请输入您的体重(单位:kg）:"))
user_height = float(input("请输入您的身高（单位：m）："))
user_BMI = user_wight/user_height**2
print("您的BMI值为："+str(user_BMI))
if user_BMI >= 28.0:
    print("您的体重为肥胖，请注意饮食，勤加锻炼")
elif 24 <= user_BMI < 28:
    print("您的体重为偏胖")
elif 20 <= user_BMI < 24:
    print("您的体重正常，请保持")
else:
    print("您的体重偏瘦，请注意")
