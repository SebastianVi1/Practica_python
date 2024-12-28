def generate(numRows) :
    if numRows == 1:
        return 1
    arr = []
    cont = 0
    for i in range(numRows):
        cont += 1
        for j in range(i + 1):
            print(j, end="")
            arr.append(i + j)
    print()
    print(arr)
generate(5)