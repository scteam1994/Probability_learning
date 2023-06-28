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


def sample_interval():
    """
        sample interval evaluation
        P 	    Z
        80% 	1.282
        85%	    1.440
        90%	    1.645
        95% 	1.960
        99% 	2.576
        99.5%	2.807
        99.9%	3.291
    """
    in_interval_times = 0
    times = 100000
    range_l = 10000
    range_s = 5
    z = 1.960
    for _ in range(times):
        r = np.random.randn(range_l)
        rm = np.mean(r)
        sampled_r = np.random.choice(r, size=range_s)
        sampled_rm = np.mean(sampled_r)
        sampled_rstd = np.std(sampled_r)
        sampled_var = sampled_rstd ** 2
        unbias_var = sampled_var * range_s / (range_s - 1)
        unbias_std = unbias_var ** 0.5
        if sampled_rm - z * unbias_std / (range_s ** 0.5) <= rm <= sampled_rm + z * unbias_std / (range_s ** 0.5):
            in_interval_times += 1

    print(in_interval_times / times)

def sample_variance():
  "ubias variance estimating"
    times = 100000
    range_l = 10000
    range_s = 5
    sampled_var = []
    for _ in range(times):
        r = np.random.randn(range_l)
        sampled_r = np.random.choice(r, size=range_s)
        sampled_var.append(np.var(sampled_r))

    print(np.mean(sampled_var))
    unbias_var = np.array(sampled_var) * range_s / (range_s - 1)
    print(np.mean(unbias_var))


if __name__ == '__main__':
    # sample_variance()
    sample_interval()
