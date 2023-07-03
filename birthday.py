"""

"""
import numpy as np
import matplotlib.pyplot as plt
def birthday():
    """
    when n_students = 253 and 23, P1 and P2 meet 0.5
    """
    n_students = 25
    times = 10000
    match_n1 = 0
    match_n2 = 0
    for _ in range(times):
        stu_a = np.random.randint(0, 365)
        class_birthday = np.random.randint(0, 365, (n_students))
        if len(set(class_birthday)) < n_students:
            match_n2 += 1
        if stu_a in class_birthday:
            match_n1 += 1
    print('number of students:', n_students)
    print('at least one student in the classroom share the same birthday of given student:', match_n1 / times)
    print('there are at least 2 students in the classroom share the same birthday of given student:', match_n2 / times)


def birthday2():
    "the expectation of n_students where there are at least 2 students in the classroom share the same birthday"
    times = 100000
    n_students_list = []
    for _ in range(times):
        match_n = False
        class_birthday = []
        while not match_n:
            new_stu = np.random.randint(0, 365)
            if new_stu in class_birthday:
                match_n = True
                n_students = len(class_birthday)+1
                n_students_list.append(n_students)
            else:
                class_birthday.append(new_stu)
    print(np.mean(n_students_list))
    print(np.var(n_students_list))
    plt.hist(n_students_list, bins=365)
    plt.show()

def calcu():
    M = 365
    res =0
    for n in range(1,M+1):
        res += np.math.factorial(M-1)*(n**2)/((M**n)*np.math.factorial(M-n))
    print(res+1)

def calcu2():
    M = 365
    res =0
    for n in range(1,M+1):
        res += np.math.factorial(M)/((M**n)*np.math.factorial(M-n))
    print(res+1)

if __name__ == '__main__':
    # calcu2()
    # birthday()
    birthday2()