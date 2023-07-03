"""
Benford's law describes the relative frequency distribution for leading digits of numbers in datasets.
"""

import numpy as np
def two_childs():
    times = 10000
    n = 0
    total = 0
    for _ in range(times):
        childs = [np.random.randint(0, 2), np.random.randint(0, 2)]
        if np.sum(childs) == 0:
            continue
        else:
            total += 1
            if np.sum(childs) == 2:
                n += 1

    print(n / total)


class Child:
    def __init__(self, gender, birthday):
        self.gender = gender
        self.birthday = birthday


def two_childs_Tuesday():
    times = 100000
    n = 0
    total = 0
    for _ in range(times):
        child1 = Child(np.random.randint(0, 2), np.random.randint(1, 8))
        child2 = Child(np.random.randint(0, 2), np.random.randint(1, 8))
        if child1.gender == 1 or child2.gender == 1:
            if child1.birthday == 2 and child1.gender == 1 or child2.birthday == 2 and child2.gender == 1:
                total += 1
                if child2.gender+child1.gender == 2:
                    n += 1

    print(n / total)


if __name__ == '__main__':
    two_childs()
    two_childs_Tuesday()
