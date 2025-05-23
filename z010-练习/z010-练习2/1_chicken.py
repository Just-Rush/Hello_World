"""公鸡一个五块钱，母鸡一个三块钱，小鸡三个一块钱，现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？"""
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 301):
            if x+y+z == 100 and 5*x+3*y+1/3*z == 100:
                print(x, y, z)
