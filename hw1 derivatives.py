def get_equation(func,xnum):
    xnum = str(xnum)
    func = list(func)
    equation = ""
    for i in range(len(func)):
        if func[i] == " " or func[i] == "":
            func.pop(i)
        if func[i] == "" or func[i] == " ":
            func.pop(i)
        if func[i] == "^":
            func[i] = "**"
        if func[i] == "x" or func[i] == "X":
            func[i] = xnum
        if i == len(func)-1:
            break
        elif func[i+1] == "x" or func[i+1] == "X":
            func[i+1] = "*"+xnum
        if ((func[i] == "x") and (func[i+1].isdigit() == True)):
            func.insert(i+1,"**")
    for things in func:
        equation += things
    return equation
        
def derivative(func,equation,xnum,deltax):
    equation1 = float(eval(get_equation(equation,xnum)))
    equation2 = float(eval(get_equation(equation,xnum = xnum+deltax))) 
    aprox_derivative = ((equation2-equation1)/deltax)
    true_derivative = int(aprox_derivative)
    true_error = abs(true_derivative-aprox_derivative)
    rel_true_error = abs(abs(true_derivative - aprox_derivative) / true_derivative) * 100
    abs_rel_true_error = (abs(true_derivative - aprox_derivative) / true_derivative)
    
    print("aproximate derivative: ",aprox_derivative)
    print("true derivative: ",true_derivative)   
    print("true error: ", true_error)
    print("relative true error: ", rel_true_error,"%")
    print("relative absolue true error: ", abs_rel_true_error)

equation3 = input("Enter your equation in the form of a quadratic equation (e.g., 'x^2 + 3*x - 4'): ")
xnum = float(input("Enter a number to represent x: "))
deltax = float(input("Enter your delta x: "))
derivative(get_equation, equation3, xnum, deltax)