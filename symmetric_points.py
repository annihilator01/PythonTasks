"""
Task:
Given points on the coordinate plane, return true if there is vertical symmetry among them,
if not return false.
"""


from typing import Dict, List, Tuple


def isSymmetric(points: List[Tuple[int, int]]) -> bool:
    x_sym_center: int = sum([p[0] for p in points]) / len(points)

    points_dict: Dict[Tuple[int, int], int] = {}
    for point in points:
        points_dict[point] = points_dict.get(point, 0) + 1

    for point in points_dict.keys():
        if points_dict[point] != points_dict.get(findSymmetricPoint(point, x_sym_center), 0):
            return False

    return True


def findSymmetricPoint(point: Tuple[int, int], x_sym_center: int) -> Tuple[int, int]:
    return (x_sym_center * 2 - point[0], point[1])


if __name__ == '__main__':
    points: List[Tuple[int, int]] = [(5, -3), (4, 1), (4, 3), (1, -3), (-1, -3), (5, 0), (2, 3), (1, 0), (7, -3), (2, 1)]
    points_2: List[Tuple[int, int]] = [(5, -3), (4, 1), (4, 3), (1, -3), (0, -3), (5, 0), (2, 3), (1, 0), (7, -3), (2, 1)]
    points_3: List[Tuple[int, int]] = [(-1, 2), (1, 2), (2, 1), (-2, 1)]
    points_4: List[Tuple[int, int]] = [(0, 0), (2, 0), (1, 2)]
    print(isSymmetric(points_4))
