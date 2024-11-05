import data
import math
from data import Point

# Write your functions for each part in the space below.

#Part 1: A function that extracts the first element from each sublist within a list of lists
#Parameters:
# inputList: a list of lists containing integers
# Returns: A list of the first elements from each sublist in inputListdef first_element(inputList: list[list[int]]) -> list:
    newList = []
    for sublist in inputList:
        if len(sublist) > 0:
            newList.append(sublist[0])
    return newList

#Part 2: A function that extracts the x-coordinates from a list of Point objects
#Parameters:
# inputList: a list of Point objects
# Returns: A list of x-coordinates from each Point in inputListdef x_coordinates(inputList:list[Point]) -> list:
    xList = []
    for points in inputList:
        xList.append(points.x)
    return xList

#Part 3: A function that filters Point objects located in the positive quadrant
#Parameters:
# inputList: a list of Point objects
# Returns: A list of Point objects where both x and y coordinates are positive
def are_in_positive_quadrant(inputList:list[Point]) -> list:
    pos_coord_list = []
    for points in inputList:
        if points.x > 0 and points.y > 0:
            pos_coord_list.append(points)
    return pos_coord_list

#Part 4: A function that calculates the Euclidean distance between two points
#Parameters:
# point1: the first Point object
# point2: the second Point object
# Returns: The Euclidean distance between point1 and point2
def distance(point1: Point, point2: Point) -> float:
    euclidean = math.sqrt(((point2.x - point1.x) ** 2) + ((point2.y - point1.y) ** 2))
    return euclidean

# Part 5: A function that calculates the Manhattan distance between two points
# Parameters:
# point1: the first Point object
# point2: the second Point object
# Returns: The Manhattan distance between point1 and point2
def manhattan_distance(point1: Point, point2: Point) -> float:
    manhattan = (abs(point1.x - point2.x) + abs(point1.y - point2.y))
    return manhattan

# Part 6: A function that calculates the Manhattan distance from the origin for each point in a list
# Parameters:
# inputList: a list of Point objects
# Returns: A list of Manhattan distances from the origin (0,0) for each Point in inputList
def distance_all(inputList: list[Point]) -> list:
    origin = Point(0,0)
    distanceList = []
    for point in inputList:
        distanceList.append(manhattan_distance(point, origin))
    return distanceList