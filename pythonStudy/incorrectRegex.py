import re

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            re.compile(input())
            print("True")
        except Exception as ex:
            print("False")
