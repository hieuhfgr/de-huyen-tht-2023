from random import randint
import os

path = "./bai1"
for test in range(10):
    filename= f"{test+1}.inp"
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as f:
        f.write(f"{randint(1, 100)}")

path = "./bai2"
for test in range(10):
    filename= f"{test+1}.inp"
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as f:
        f.write(f"{randint(1, 65000)} {randint(1, 65000)}")

path = "./bai3"
for test in range(9):
    filename= f"{test+1}.inp"
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as f:
        n = randint(1, 100)
        f.write(f"{n}\n")
        a = []
        for i in range(n):
            num = randint(1, 1000)
            if (num in a):
                num = randint(1, 1000)
            a.append(num)
            f.write(f"{num}\n")
        num = randint(1, 1000)
        if (num in a):
            num = randint(1, 1000)
        f.write(f"{num}")

path = "./bai4"
for test in range(9):
    filename= f"{test+1}.inp"
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as f:
        n = randint(1, 100)
        f.write(f"{n}\n")
        a = []
        for i in range(n):
            num = randint(1, 32000)
            if (num in a):
                num = randint(1, 32000)
            a.append(num)
            f.write(f"{num} ")