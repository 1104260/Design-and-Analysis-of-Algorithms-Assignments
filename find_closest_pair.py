from math import sqrt

def find_closest_pair(points):
    if len(points) <= 1:
        return -1,-1
    min = 100000
    index1 = -1
    index2 = -1
    for i in range(len(points) - 1):
        for j in range(i+1,len(points)):
            d = sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
            if d < min:
                min = d
                index1 = i
                index2 = j
    return index1, index2