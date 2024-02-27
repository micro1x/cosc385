import math

# Define the Taylor series approximation function
def exp_taylor(x, terms):
    result = 0
    for i in range(terms):
        result += x**i / math.factorial(i)
    return result

# Calculate the true value of e^3 using the built-in exp function
true_value = math.exp(3)

# Calculate the approximation of e^3 using the Taylor series with 10 terms
approximation = exp_taylor(3, 10)

# Calculate the true error
true_error = true_value - approximation

# Print the results
print("True value of e^3:", true_value)
print("Approximation of e^3 using Taylor series:", approximation)
print("True error:", true_error)