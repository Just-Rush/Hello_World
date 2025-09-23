"""三门问题测试"""
import random

def monty_hall():
    i1 = 0
    i2 = 0
    for i in range(10000):
        door = [0, 0, 1]
        people_choice = random.choice(door)
        remain_doors = door.copy()
        remain_doors.remove(people_choice)
        remain_doors.remove(0)
        people1 = people_choice
        people2 = remain_doors[0]
        if people1 == 1:
            i1 += 1
        if people2 == 1:
            i2 += 1
    print(f"不换门赢的概率{i1/10000}, 换门赢的概率{i2/10000}")
    print(remain_doors)

if __name__ == "__main__":
    monty_hall()





