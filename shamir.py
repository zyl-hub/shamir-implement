from random import randint
from primes import get_large_enough_prime


def SecretDistribution(n, t, s, filename):
    if t < 2:
        raise ValueError("t >=2 is required")
        return -1
    if t > n:
        raise ValueError("t <= n is required")
        return -1
    prime_q = get_large_enough_prime([s, n])

    """---------------------------------------
        随机生成系数a并且采样出n个函数上的点
    ---------------------------------------"""
    a = []
    points_x = []
    points_y = []
    a.append(s)
    for i in range(t-1):
        a.append(randint(0, prime_q-1))
    for x in range(1, n+1):
        y = a[0]
        for i in range(1, len(a)):
            y = y + a[i] * x**i
        points_x.append(x)
        points_y.append(y)

    """---------------------------------------
        打开文件写入函数的系数，素数q的数值，t的数值，n个采样点的信息
        line 1: f(x)
        line 2: q
        line 3: t
        line 4: n points of f(x) 按照x,y,x,y...的顺序排序
    ---------------------------------------"""
    file = open(filename, mode='w')
    a_str = " ".join([str(x) for x in a])
    points_x_str = " ".join(str(x) for x in points_x)
    points_y_str = " ".join(str(x) for x in points_y)
    file.write(a_str)
    file.write("\n")
    file.write(str(prime_q))
    file.write("\n")
    file.write(str(t))
    file.write("\n")
    file.write(points_x_str)
    file.write("\n")
    file.write(points_y_str)
    return 0


def SecretRecovery(filename):
    """---------------------------------------
        打开文件获取函数的各项系数，n个点的信息，素数q的数值，t的数值
    ---------------------------------------"""
    file = open(filename, mode='r')
    secretBook = file.readlines()
    for line in range(len(secretBook)):
        secretBook[line] = secretBook[line].strip('\n')
    a_list = secretBook[0].split(' ')
    a_list = list(map(int, a_list))
    prime_q = int(secretBook[1])
    t = int(secretBook[2])
    points_x_list = secretBook[3].split(' ')
    points_x_list = list(map(int, points_x_list))
    points_y_list = secretBook[4].split(' ')
    points_y_list = list(map(int, points_y_list))

    """---------------------------------------
        异常处理
    ---------------------------------------"""
    if(t > len(points_x_list)):
        raise ValueError("t <= n is required")
        return -1

    """---------------------------------------
        通过拉格朗日插值发计算出a0的数值，也就是secret的数值
    ---------------------------------------"""
    r = 0
    for j in range(t):
        x = 1
        for m in range(t):
            if m != j:
                x = x*(points_x_list[m]/(points_x_list[m]-points_x_list[j]))
        r += points_y_list[j]*x
    return r


if __name__ == '__main__':
    filename = "key_book"
    n = 4
    t = 3
    s = 2
    SecretDistribution(n=n, t=t, s=2, filename=filename)
    r = SecretRecovery(filename=filename)
    if r == s:
        print("success")
    else:
        print("fail")
