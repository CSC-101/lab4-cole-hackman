import data
import math
from data import Point

# Write your functions for each part in the space below.

# Part 1
def first_element(inputList: list[list[int]]) -> list:
    newList = []
    for sublist in inputList:
        if len(sublist) > 0:
            newList.append(sublist[0])
    return newList

# Part 2
def x_coordinates(inputList:list[Point]) -> list:
    xList = []
    for points in inputList:
        xList.append(points.x)
    return xList

# Part 3
def are_in_positive_quadrant(inputList:list[Point]) -> list:
    pos_coord_list = []
    for points in inputList:
        if points.x > 0 and points.y > 0:
            pos_coord_list.append(points)
    return pos_coord_list
# Part 4
def distance(point1: Point, point2: Point) -> float:
    euclidean = math.sqrt(((point2.x - point1.x) ** 2) + ((point2.y - point1.y) ** 2))
    return euclidean

# Part 5
def manhattan_distance(point1: Point, point2: Point) -> float:
    manhattan = (abs(point1.x - point2.x) + abs(point1.y - point2.y))
    return manhattan

# Part 6
def distance_all(inputList: list[Point]) -> list:
    origin = Point(0,0)
    distanceList = []
    for point in inputList:
        distanceList.append(manhattan_distance(point, origin))
    return distanceList