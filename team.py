<<<<<<< HEAD
def f_avg(Data):
    return 1

def f_sum(data):
    return 1

def f_sort(data):
    n = len(data)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if data[j] < data[mini]:
                mini = j
        data[i], data[mini] = data[mini], data[i]
    return data

a = f_sort([1,3,5,7,9,2,4,6,8])
print(a)


def f_desc(DATA):
=======
<<<<<<< HEAD
def f_avg(Data):
    return 1

def f_sum(data):
    return 1

def f_sort(data):
    return 1

def f_desc(DATA):
=======
def f_avg(Data):
    return 1

def f_sum(data):
    return 1

def f_sort(data):
    return 1

def f_desc(DATA):
>>>>>>> 3258e092a3133ae8ed48418ad90367c02a5e195f
>>>>>>> c2082bf7667ccdbb1ba278ea58b0c3743e6886ec
    return 1