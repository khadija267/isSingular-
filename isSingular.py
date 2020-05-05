# turning the matrix(4X4 matrix) into echelon form.
import numpy as np
def isSingular(A) :
    B = np.array(A, dtype=np.float_) # Make B as a copy of A, since we're going to alter it's values.
    try:
        fixRow(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular:
        return True
    return False
class MatrixIsSingular(Exception): pass

# the first element = 1.
def fixRowZero(A) :
    if A[0,0] == 0 :
        A[0] = A[0] + A[1]
    if A[0,0] == 0 :
        A[0] = A[0] + A[2]
    if A[0,0] == 0 :
        A[0] = A[0] + A[3]
    if A[0,0] == 0 :
        raise MatrixIsSingular()
    A[0] = A[0] / A[0,0]
    return A
def fixRowOne(A) :
    A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        raise MatrixIsSingular()
    A[1] = A[1] / A[1,1]
    return A
def fixRowTwo(A) :
    A[2]=A[2]-A[2,0]*A[0]
    A[2]=A[2]-A[2,1]*A[1]
    if A[2,2] == 0 :
        A[2]=A[2]+A[3]
        A[2]=A[2]-A[2,0]*A[0]
        A[2]=A[2]-A[2,1]*A[1]
    if A[2,2] == 0 :
        raise MatrixIsSingular()
    A[2]=A[2]/A[2,2]
    return A
def fixRowThree(A) :
    A[3]=A[3]-A[3,0]*A[0]
    A[3]=A[3]-A[3,1]*A[1]
    A[3]=A[3]-A[3,2]*A[2]
    if A[3,3]==1:
        raise MatrixIsSingular()
    return A
    ###############################TEST################
A = np.array([

        [2, 0, 0, 0],

        [0, 3, 0, 0],

        [0, 0, 4, 4],

        [0, 0, 5, 5]

    ], dtype=np.float_)

print(isSingular(A))

#False
