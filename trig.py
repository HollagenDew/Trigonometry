"""
Program name : trig.py
Author       : Prateek Mahadev Waghmare
Written on   : 25-Apr-24 10:17:49.03 IST
Description  : I am presently engaged in learning Python and have developed this modest code to assess my proficiency 
in Python programming. The program is designed to address fundamental trigonometric problems, and I have endeavored 
to craft it to the best of my abilities. Should you wish to offer corrections or enhancements to this code, your 
input would be welcomed. 
"""

import math #I have imported the built-in 'math' module to streamline the code and facilitate calculations such as square roots.

sin = (0,1/2,1/math.sqrt(2),math.sqrt(3)/2,1) # values of sin(θ)
cos = (1,math.sqrt(3)/2,1/math.sqrt(2),1/2,0) # values of cos(θ)
tan = (0,1/math.sqrt(3),1,math.sqrt(3),"undefined") # values of tan(θ)
cot = ("undefined",math.sqrt(3),1/math.sqrt(3),0) # values of cot(θ)
sec = (1,2/math.sqrt(3),math.sqrt(2),2,"undefind") # values of sec(θ)
cosec = ("undefind",2,math.sqrt(2),2/math.sqrt(3),1) # values of cosec(θ)


def print_banner():
    banner = """
██████╗  █████╗ ███████╗██╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██║██╔════╝
██████╔╝███████║███████╗██║██║     
██╔══██╗██╔══██║╚════██║██║██║     
██████╔╝██║  ██║███████║██║╚██████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝            
"""
    banner2 = """
    ████████╗██████╗ ██╗ ██████╗  ██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗███████╗████████╗██████╗ ██╗   ██╗    
    ╚══██╔══╝██╔══██╗██║██╔════╝ ██╔═══██╗████╗  ██║██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝    
       ██║   ██████╔╝██║██║  ███╗██║   ██║██╔██╗ ██║██║   ██║██╔████╔██║█████╗     ██║   ██████╔╝ ╚████╔╝     
       ██║   ██╔══██╗██║██║   ██║██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗  ╚██╔╝      
       ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║   ██║       
       ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝       
                                                                                                              

"""
    banner3 = """
             ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     ██╗
            ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██║
            ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ██║
            ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ╚═╝
            ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ██╗
             ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝
                                                                                                      
"""
    print(banner)
    print(banner2)
    print(banner3)

# Example usage:
print_banner() # Prints Tool Name Banner at starting of program 
print("Welcome to the Basic Trigonometry Calculator!")
print("This tool can help you with the following terms:")

lst = """
sin(30)    sin(45)    sin(60)    sin(90)
cos(30)    cos(45)    cos(60)    cos(90)
tan(30)    tan(45)    tan(60)    tan(90)
cot(30)    cot(45)    cot(60)    cot(90)
sec(30)    sec(45)    sec(60)    sec(90)
cosec(30)  cosec(45)  cosec(60)  cosec(90)

"""
print("You can use from the current available terms from the following:\n",lst)
print("Operation that can be performed between terms are: \n Addition(+),Substraction(-),Multiplication(*),Divison(/). You can also use '() , [], {}.'\n")

def convert_to_list(eqt):
    # Split the inputed eqution string at whitespace
    terms = eqt.split()

    # Initialize an empty list to store the converted elements
    eq_list = []

    # Iterate over the terms
    for term in terms:
        # If term is not whitespace, add it to the list
        if term.strip() != "":
            eq_list.append(term.strip())

    return eq_list

# # Example usage

print("Please maintain whitespaces between each term\nFor Ex: a + b")
eqt = input("Enter yor equation: ")
result_list = convert_to_list(eqt) # Used to call convert_to_list function and store the resltant list.

#dictionary for reference 
sin_dict = {"sin(30)":0, "sin(45)":1, "sin(60)":2, "sin(90)":3}
cos_dict = {"cos(30)":0, "cos(45)":1, "cos(60)":2, "cos(90)":3}
tan_dict = {"tan(30)":0, "tan(45)":1, "tan(60)":2, "tan(90)":3}
cot_dict = {"cot(30)":0, "cot(45)":1, "cot(60)":2, "cot(90)":3}
sec_dict = {"sec(30)":0, "sec(45)":1, "sec(60)":2, "sec(90)":3}
cosec_dict = {"cosec(30)":0, "cosec(45)":1, "cosec(60)":2, "cosec(90)":3}

final_equation = [] # empty list to store equation


def build_final_equation(list):
    for term in list:
        if term == "+" or term == "-" or term == "*" or term == "/":
            value = str(term)
            final_equation.append(value) # Adds the value to final_eqution list
            pass
        elif term == "(" or term == ")" or term == "[" or term == "]" or term == "{" or term == "}":
            value = str(term)
            final_equation.append(value) # Adds the value to final_eqution list
            pass
        elif term == "sin(30)" or term == "sin(45)" or term == "sin(60)" or term == "sin(90)":
            index = sin_dict[term] # stores the value of dictionary in the index
            value = str(sin[index]) # retrives the value of 'sin' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list        
            pass
        elif term == "cos(30)" or term == "cos(45)" or term == "cos(60)" or term == "cos(90)":
            index = cos_dict[term] # stores the value of dictionary in the index
            value = str(cos[index]) # retrives the value of 'cos' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list
            pass
        elif term == "tan(30)" or term == "tan(45)" or term == "tan(60)":
            index = tan_dict[term] # stores the value of dictionary in the index
            value = str(tan[index]) # retrives the value of 'tan' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list
            pass
        elif term == "cot(45)" or term == "cot(60)" or term == "cot(90)":
            index = cot_dict[term] # stores the value of dictionary in the index
            value = str(cot[index]) # retrives the value of 'cot' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list
            pass
        elif term == "sec(30)" or term == "sec(45)" or term == "sec(60)":
            index = sec_dict[term] # stores the value of dictionary in the index
            value = str(sec[index]) # retrives the value of 'sec' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list
            pass
        elif term == "cosec(45)" or term == "cosec(60)" or term == "cosec(90)":
            index = cosec_dict[term] # stores the value of dictionary in the index
            value = str(cosec[index]) # retrives the value of 'cosec' tuple and stores in value
            final_equation.append(str(value)) # Adds the value to final_eqution list 
            pass
        elif term == "cosec(30)" or term == "sec(90)" or term == "cot(30)" or term == "tan(90)": # Error handling caused due to "undefined" in the tuple
            print(f'Invalid term encounterd: {term} which is "undefined"')
        else:
            print("Invalid Term")


build_final_equation(result_list)  # Function is called and result_list list is passed as a parameter


def evaluate_expression_and_print_result(equation):
    """
    Function to evaluate a mathematical expression represented as a list of strings and print the result.
    
    Parameters:
        equation (list): A list containing the elements of a mathematical expression.

    Returns:
        float: The result of evaluating the mathematical expression.
    """
    # Join the elements of the equation list into a single string
    # Removes quotes and whitespaces
    f_equation = ''.join(equation)

    # Evaluate the mathematical expression represented by f_equation
    # using the eval() function
    end_result = eval(f_equation)

    # Print the result of the evaluation
    print(f"\n$ Answer:-\n  Value of {eqt} is",end_result,"$")

    # Return the result
    return end_result


evaluate_expression_and_print_result(final_equation) # Function is called and final_equation list is passed as a parameter