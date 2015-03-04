'''
The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. To find the weakest point we should find the weakest row and column. The weakest point is placed in the intersection of these rows and columns. Row (column) durability is a sum of cell durability in that row (column). You should find coordinates of the weakest point (row and column). The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point.

Input: A durability map as a list of lists with integers.

Output: The coordinates of the weak point as a list (tuple) of integers.
'''


def weak_point(matrix):
    # Make a list of sums of all rows of matrix
    row_sum = list(map(sum, matrix)) 
    # Makes a list of sums of all rows of matrix. Transponse matrix first
    column_sum = list(map(sum, zip(*matrix))) 
    # Get an index of first weakes row 
    index1 = row_sum.index(min(row_sum))
    #Get an index of first weakes column
    index2 = column_sum.index(min(column_sum))
    # Return coordinates
    return [index1,index2]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
