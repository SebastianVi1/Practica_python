
def read_numbers():
    list= []
    while True:
        num = input()
        if num == "done":
            break
        
        list.append(float(num))
        

    return list
        

def average(list):
    sumaTotal = 0
    sumaTotal = sum(list)/len(list)
    return print(sumaTotal)

average(read_numbers())

