def tukar(x,y):
    temp=x
    x=y
    y=temp
    print("Sesudah di tukar:")
    print("nilai x: %d" %x)
    print("nilai y: %d" %y)

def main():
    x = 30
    y = 50

    print("sebelum di tukar:")
    print("nilai x: %d" %x)
    print("nilai y: %d" %y)

    tukar(x,y)

    for x in range(50):
        if x == 50:break
        print(x)
    else:
        print("berhenti") 
main()