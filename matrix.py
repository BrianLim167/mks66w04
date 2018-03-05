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
        m[3][0] = x
        m[3][1] = y
        m[3][2] = z
        return m

    @staticmethod
    def scaler(x,y,z):
        m = Matrix.ident()
        m[0][0] = x
        m[1][1] = y
        m[2][2] = z
        return m

    @staticmethod
    def rotx(a):
        m = Matrix.ident()
        m[1][1] = math.cos(a)
        m[1][2] = math.sin(a)
        m[2][1] = -math.sin(a)
        m[2][2] = math.cos(a)
        return m
    
    @staticmethod
    def roty(a):
        m = Matrix.ident()
        m[2][2] = math.cos(a)
        m[2][0] = math.sin(a)
        m[0][2] = -math.sin(a)
        m[0][0] = math.cos(a)
        return m
    
    @staticmethod
    def rotz(a):
        m = Matrix.ident()
        m[0][0] = math.cos(a)
        m[0][1] = math.sin(a)
        m[1][0] = -math.sin(a)
        m[1][1] = math.cos(a)
        return m
        
    
    def __init__(self, rows = 4, cols = 4):
        self.matrix = []
        self.rows = rows
        self.cols = cols
        for c in range( cols ):
            self.append( [] )
            for r in range( rows ):
                self[c].append( 0 )

    def __mul__(self, other):
        return Matrix.mult(self,other)

    def __imul__(self, other):
        self = other * self
        return self

    def __getitem__(self, i):
        return self.matrix[i]

    def __setitem__(self, i, val):
        self.matrix[i] = val
        return self.matrix[i]

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        s = ""
        for r in range(self.rows):
            for c in range(self.cols):
                s += ("     "+str(self.matrix[c][r]))[:10][-5:]
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



