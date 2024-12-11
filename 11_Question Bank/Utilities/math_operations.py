def calculate_average(list):
    size = len(list)
    avg = 0
    for i in list:
        avg += i
    avg = avg/size
    return avg