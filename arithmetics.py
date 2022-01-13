def my_sum(number):
    a_sum = 0
    for i in range(1, number+1):
        a_sum += i
    return a_sum


def average(a, b):
    return (a + b) / 2


def square_root(num, low, high):
    for i in range(20):
        guess = average(low, high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num:
            high = guess
        else:
            low = guess
    return guess


def factors(number):
    factor_list = []
    for i in range(1, number+1):
        if number % i == 0:
            factor_list.append(i)
    return factor_list


def gcf(num1, num2):
    """returns the greatest common factor of two numbers"""
    a = factors(num1)
    b = factors(num2)
    a.extend(b)
    a.sort()
    gcf = 1
    for i in a:
        if a.count(i) == 2:
            gcf = i
    return gcf


print(gcf(11, 44))
