import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        
        if self.h > 2 :
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        return self.g[0][0] if self.h == 1 else (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]) 

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        return sum([self.g[i][i] for i in range(self.h)])
       

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return Matrix([[1/self.g[0][0]]])
        else:
            det = self.determinant()
            trace = self.trace() 
            id_matrix = identity(self.h)
            inverse = zeroes(2,2)
            
            for i in range(self.h):
                for j in range(self.w):
                    inverse[i][j] = ((trace * id_matrix[i][j]) - self.g[i][j]) * (1/det)
                    
            return inverse
         
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        matrix = self.g
        
        #helper to get the given column of a matrix.
        def get_col(matrix, idx):
            col = [] 
            for row in matrix:
                col.append(row[idx])
            return col
        
        #compute transpose.
        for i in range(len(matrix[0])):
            col = get_col(matrix, i)
            transpose.append(col)
        
        return Matrix(transpose)
       
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        sum_ = zeroes(self.h, self.w)
        
        for row in range(self.h):
            for col in range(self.w):
                sum_[row][col] = self.g[row][col] + other[row][col]
                
        return sum_

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negged = zeroes(self.h, self.w)

        for i in range(self.h):
            for j in range(self.w):
                negged[i][j] = self.g[i][j] * -1 
        
        return negged

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        subbed = zeroes(self.h, self.w)
        
        for row in range(self.h):
            for col in range(self.w):
                subbed[row][col] = self.g[row][col] - other[row][col]
        
        return subbed

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        if self.w != other.h:
            raise ValueError("Matrix dimensions do not match! Left columns {} Right Rows {}".format(self.w, other.h))
        
        prod = zeroes(self.h, other.w)
        
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    prod[i][j] += self.g[i][k] * other.g[k][j]
        
        return prod

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
   
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            r_prod = zeroes(self.h, self.w)
        
            for i in range(self.h):
                for j in range(self.w):
                    r_prod[i][j] = self.g[i][j] * other
        
            return r_prod
     
            