from random import randint
from primes import get_large_enough_prime


def SecretDistribution(n, t, s, filename):
    if t < 2:
        raise ValueError("t >=2 is required")
        return -1
    if n >= t:
        raise ValueError("t < n is required")
        return -1
    prime_q = get_large_enough_prime([s, n])
    """
    """
    a = []
    points = []
    a.append(s)
    for i in range(t-1):
        a.append(randint(0, prime_q-1))
    for x in range(1, n+1):
        y = a[0]
        for i in range(1, len(a)):
            y = y + a[i] * x**i
        points.append((x, y))
    """ open file
        line 1: f(x)
        line 2: q
        line 3: t
        line 4: n points of f(x)
    """
    file = open(filename, mode='w')
    a_str = " ".join([str(x) for x in a])
    points_str = " ".join(str(x) for x in points)
    file.write(a_str)
    file.write("\n")
    file.write(str(prime_q))
    file.write("\n")
    file.write(str(t))
    file.write("\n")
    file.write(points_str)
    return 0


def SecretRecovery(filename):
    r = filename
    return r


if __name__ == '__main__':
    SecretDistribution(n=3, t=4, s=2, filename="key_book")
