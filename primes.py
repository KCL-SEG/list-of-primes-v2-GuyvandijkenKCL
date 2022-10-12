def primes(number_of_primes):
    list = [2]
    x = 3
    if number_of_primes < 1:
        raise ValueError("Needs to be at least 1")
    while (len(list) < number_of_primes):
        y = 0
        prime = True
        while y < len(list):
            if x % list[y] == 0:
                prime = False
            y = y + 1
        if prime == True:
            list.append(x)
        x = x + 2
    return list




