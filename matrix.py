import math


class Matrix(object):

    #m1 * m2 -> m2
    @staticmethod
    def mult( m1, m2 ):
        m = Matrix(m1.rows, m2.cols)
        for c in range( m.cols ):
            m.append([])
            for r in range( m.rows ):
                m[-1].append( 0 )
                for i in range(m1.cols):
                    m[c][r] += (m1[i][r] * m2[c][i])
        return m

    @staticmethod
    def ident(s=4):
        m = Matrix(s,s)
        for c in range( m.cols ):
            m.matrix[c][c] = 1
        return m

    @staticmethod
    def mover(x,y,z):
        m = Matrix.ident()
        m[0][3] = x
        m[1][3] = y
        m[2][3] = z
        return m
    
    def __init__(self, rows = 4, cols = 4):
        self.matrix = []
        self.rows = rows
        self.cols = cols
        for c in range( cols ):
            self.matrix.append( [] )
            for r in range( rows ):
                self.matrix[c].append( 0 )

    def __mul__(self, other):
        return Matrix.mult(self,other)

    def __imul__(self, other):
        self = other * self

    def __getitem__(self, i):
        return self.matrix[i]

    def __setitem__(self, i, val):
        self.matrix[i] = val

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        s = ""
        for r in range(self.rows):
            for c in range(self.cols):
                s += ("     "+str(self.matrix[c][r]))[-5:]
                s += ' '
            s += '\n'
        return s

    def append(self, val):
        self.matrix.append(val)

    def print( self ):
        print(self)

    def add_edge( self, x0, y0, z0, x1, y1, z1 ):
        self.add_point(x0,y0,z0)
        self.add_point(x1,y1,z1)

    def add_point( self, x, y, z=0 ):
        self.append([])
        self[-1].append(x)
        self[-1].append(y)
        self[-1].append(z)
        self[-1].append(1)
        self.cols += 1



