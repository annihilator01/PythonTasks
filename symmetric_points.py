def isSymmetric(points):
    one_line_points = [p[0] for p in points if p[1] == points[0][1]]
    sym_centre_x = sum(one_line_points) / len(one_line_points)

    dict = {}
    for p in points:
        sym_centre_point = (abs(p[0] - sym_centre_x), p[1]) # tuple[0] - distance to sym. centre, tuple[1] - 'y' coordinate
        if dict.get(sym_centre_point):
            dict[sym_centre_point] += 1
        else:
            dict[sym_centre_point] = 1

    if sum(dict.values()) == len(points) and sum(map(lambda x: x % 2, dict.values())) == 0:
        return True
    else:
        return False

points = [(5, -3), (4, 1), (4, 3), (1, -3), (-1, -3), (5, 0), (2, 3), (1, 0), (7, -3), (2, 1)]
points_2 = [(5, -3), (4, 1), (4, 3), (1, -3), (0, -3), (5, 0), (2, 3), (1, 0), (7, -3), (2, 1)]
points_3 = [(-1, 2), (1, 2), (2, 1), (-2, 1)]

print(isSymmetric(points))
