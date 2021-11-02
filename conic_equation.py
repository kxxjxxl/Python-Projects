#Funtion that takes A,B and C and does calc to check
def checking_char(charA,charB,charC):
    if charB**2-4*(charA*charC)==0:
        print("The conic section is a parabola!")
    elif charB**2-4*(charA*charC)<0 and charA == charC:
        print("The conic section is a circle!")
    elif charB**2-4*(charA*charC)<0 and charA != charC:
        print("The conic section is a ellipse!")
    elif charB**2-4*(charA*charC)>0:
        print("The conic section is a hyperbola!")

#input for A,B and C
charA = int(input("What is the value of A? "))
charB = int(input("What is the value of B? "))
charC = int(input("What is the value of C? "))

#using funtion to check and display
checking_char(charA,charB,charC)






