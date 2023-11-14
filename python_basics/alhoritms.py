def is_prime(x):
    prime = True
    for i in range(2,x):
        if x%i == 0:
            prime = False
    return prime
if __name__ == '__main__':
    count = 0;
    number = 2;
    while (count < 10000):
        if (is_prime(number)):
            print(number)
            count = count+1
        number = number+1
        