if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = input().split()

        try:
            print(int(a) // int(b))
        except Exception as ex:
            print("Error Code:", ex)



