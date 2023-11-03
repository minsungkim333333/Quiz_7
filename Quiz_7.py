height=int(input('트리의 높이를 입력해주세요.'))
for i in range(height):
    for j in range(height-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
