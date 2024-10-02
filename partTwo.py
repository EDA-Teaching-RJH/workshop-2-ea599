import math
def main():
    a = int(input("Enter one value of the triangle: "))
    b = int(input("Enter another value of the triangle: "))
    pythag(a,b)

def pythag(A,B):
    C = float(round(math.sqrt(A*A+B*B), 2))
    
    print("The hypotenuse is: " + str(C))

main()
