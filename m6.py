"""for i in range(1, 6):
    print("*" * i)"""
    
"""for i in range(5, 0, -1):
    print("*" * i)"""

"""    
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)"""
    
"""for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)"""
    
"""
num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []"""
    
"""line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = []"""
    
"""num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []"""

"""
import random
def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return

print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
pcnum = get_computer_choice()

determine_winner(chnum)
"""

"""f = open("temp.txt", "w")
f.close()"""

"""
file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close()"""
    
    
"""f = open("C:\\Users\\Document\\temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")
    
f.close()"""

"""f = open("C:\\Users\\Document\\temp.txt", "w")

f.write("hello\n")
f.write("world")
    
f.close()"""

"""f = open("temp.txt", "r")
res = f.read()
print(res)

f.close()"""

"""
f = open("C:\\Users\\Document\\temp.txt", "r")
res = f.read()
print(res)

f.close()"""

"""f = open("temp.txt", "r")
for line in f:
    print(line)
    
f.close()"""

    
    