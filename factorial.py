import time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_factorial():
    factorial_list = [factorial(i) for i in range(50)]
    result = sum(factorial_list)
    
    print("Final SUM is {}".format(result))
    return result

if __name__ == "__main__":
    sum_factorial()
