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
    return 1

def f_desc(DATA):
    return 1