import numpy as np

def first_num():
    # Benford’s law
    res = np.zeros(9)
    for _ in range(100000):
        r = np.random.randint(1, 99999999)
        # uniform distribution
        num = np.random.randint(1, r)
        # first number of num
        num_f = int(str(num)[0])
        res[num_f - 1] += 1
    print(res / 100000)

if __name__ == '__main__':
    first_num()