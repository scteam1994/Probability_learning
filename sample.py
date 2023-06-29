import numpy as np

def sample_interval():
    """
        confident interval evaluation
        total variance is unknown
        P 	    Z
        80% 	1.282
        85%	    1.440
        90%	    1.645
        95% 	1.960
        99% 	2.576
        99.5%	2.807
        99.9%	3.291
    using sampled_var to estimate confident interval is not correct, especially when sample number is small.
    That is because sampled_rm is a minimizer of sampled_var.Using sampled_rm generates biased sampled_var.
    P(mean >= sample mean + z_t_0.95(n-1) * unbiased std / (n ** 0.5)) = 2.5%
    when n is big(over 30) , t-distribution is approximated to a normal distribution

    """
    mean_in_interval_times_biased = 0
    mean_in_interval_times_unbiased = 0
    var_in_interval_times = 0
    times = 100000
    range_s = 11
    # mean
    z = 1.960
    # 95% t(10) = 2.228
    # 97.5% alpha(10) = 20.483; 2.5%3.247
    z_t = 2.228
    rm = 0
    rvar = 1
    for _ in range(times):
        sampled_r = np.random.randn(range_s)
        sampled_rm = np.mean(sampled_r)
        sampled_r_std = np.std(sampled_r)

        sampled_var = sampled_r_std ** 2
        unbiased_var = sampled_var * range_s / (range_s - 1)
        unbiased_std = unbiased_var ** 0.5
        if sampled_rm - z * sampled_r_std / (range_s ** 0.5) <= rm <= sampled_rm + z * sampled_r_std / (range_s ** 0.5):
            mean_in_interval_times_biased += 1
        if sampled_rm - z_t * unbiased_std / (range_s ** 0.5) <= rm <= sampled_rm + z_t * unbiased_std / (range_s ** 0.5):
            mean_in_interval_times_unbiased += 1
        if (range_s-1)*np.var(sampled_r)/20.483 <= rvar <=(range_s-1)*np.var(sampled_r)/3.247:
            var_in_interval_times += 1
    print(mean_in_interval_times_biased / times)
    print(mean_in_interval_times_unbiased / times)
    print(var_in_interval_times / times)



def sample_variance():
    """unbiased variance estimating"""
    times = 100000
    range_l = 10000
    range_s = 5
    sampled_var = []
    r = np.random.randn(range_l)
    for _ in range(times):
        sampled_r = np.random.choice(r, size=range_s)
        sampled_var.append(np.var(sampled_r))
        # unbiased var could calculated as sum((xi - mean(x))) / (n-1)
    # Xi - mean(X) follows chi-square distribution df = n-1
    # unbiased sampled_var follows chi-square distribution df = n-1
    print(np.mean(sampled_var))
    unbias_var = np.array(sampled_var) * range_s / (range_s - 1)
    print(np.mean(unbias_var))
    # var(unbias_var) = 2*(sigma**2)/(n-1)
    print(np.var(unbias_var), 2 * (1 ** 4) / (range_s - 1))


if __name__ == '__main__':
    """
    random choice from a long sequence doesn't make a  difference from making a short sequence directly.
    """
    # sample_variance()
    sample_interval()
