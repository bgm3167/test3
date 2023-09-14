def f_avg(data):
    if not data:
        return None

    total = sum(data)
    average = total / len(data)
    return average
   
def f_sum(data):
    result = 0
    for i in data:
        result += i
    return result

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
    return 1