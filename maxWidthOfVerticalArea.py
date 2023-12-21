def maxWidthOfVerticalArea(points):
    points.sort(key=lambda point: point[0])
    widest_vertical_area = 0
    x = [i for i, j in points]

    for i in range(1, len(x)):
        widest_vertical_area = max(widest_vertical_area, x[i] - x[i - 1])
    return widest_vertical_area



