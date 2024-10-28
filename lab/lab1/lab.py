from math import *

def discriminant(a, b, c):

    d = b**2-4*a*c

    if d > 0:
        t1 = ((-b)+(sqrt(d)))/(2*a)
        t2 = ((-b)-(sqrt(d)))/(2*a)

        if t1 >= 0:
            x1 = sqrt(t1)
            x2 = -sqrt(t1)
            print(f"x1:{x1}, x2:{x2}")
        
        if t2 >= 0:
            x3 = sqrt(t2)
            x4 = -sqrt(t2)
            print(f"x3:{x3}, x4:{x4}")
        
        else:
            print("No roots")
        
    elif d == 0:
        x0 = -b / (2*a)

        if x0 >= 0:
            x1 = sqrt(x0)
            x2 = -sqrt(x0)
            print(f"x1:{x1}, x2:{x2}")

        else:
            print("No roots")
        
    else:
        print("Discriminant < 0, no roots")


def main():

    while True:
        try:
            a = int(input("Enter coef a: "))
            b = int(input("Enter coef b: "))
            c = int(input("Enter coef c: "))
            break

        except ValueError:
            continue

    discriminant(a, b, c)


main()


    