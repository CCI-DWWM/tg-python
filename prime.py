def is_prime(n):
    if n <= 1 :
        return False
    else :
        for i in range(2, n-1, 1) :
            if n % i == 0 :
                return False
        else:
            return True