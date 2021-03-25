#...............................Functions...............................

def print_result (sign, result):
    if(result == 0):
        print("= 0")
    else:
        print("= " + sign +  str(result))  

def addition_steps(sign1, sign2, num1, num2):
   #Similar Signs
    if(sign1 == sign2):
        print("= " + sign1 + " ( | " + sign1 + num1 + " | ) + ( | " + sign2 + num2 + " | )")
        print("= " + sign1 + " ( " + num1 + " + " + num2 + " )")
        result = int(num1) + int(num2)
        print_result(sign1, result) 
    #Different Signs
    elif(sign1 != sign2):
        if(int(num1) >= int(num2)):
            print("= " + sign1 + " ( | " + sign1 + num1 + " | - | " + sign2 + num2 + " | )")
            print("= " + sign1 + " (" + num1 + " - " + num2 + ")")
            result = int(num1) - int(num2)
            print_result(sign1, result)  
        else:
            print("= " + sign2 + " ( | " + sign2 + num2 + " | - | " + sign1 + num1 + " | )")
            print("= " + sign2 + " (" + num2 + " - " + num1 + ")")
            result = int(num2) - int(num1)
            print_result(sign2, result) 

def subtraction_steps(sign1, sign2, num1, num2):
    #Transform the subtraction to addition
    if (sign2 == "+"):
        sign2 = "-"
    else:
        sign2 = "+"
    
    print("= ( " + sign1 + num1 + " ) + ( " + sign2 + num2 + " )")
    
    #Apply Addition Steps after transformation
    addition_steps(sign1, sign2, num1, num2)


expr = input ("Enter Your Expression in format ( +x ) + ( -y ): ")

#Parsing Input
sign1 = expr[2]
num1 = expr[3]
sign2 =  expr[11]
num2 = expr[12]
operation = expr[7]

# Adding
if (operation == "+"):
    addition_steps(sign1, sign2, num1, num2)
# Subtraction
elif (operation == "-"):
    subtraction_steps(sign1, sign2, num1, num2)