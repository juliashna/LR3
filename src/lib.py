def Fibonacchi(n):
    if(n < 2):
        return None
        print("Введите число не меньше 2")
    else:
        fib = [0, 1]
        for i in range(n - 2):
            Fn = fib[i] + fib[i + 1]
            fib.append(Fn)
    return fib

def Bubble(n):
    for i in range(0, len(n) - 1):
        for j in range(len(n) - 1):
            if (n[j] > n[j + 1]):
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n

def Calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Неверный оператор")
        return None

    return result
