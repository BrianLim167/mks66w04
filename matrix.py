import math


class Matrix(object):

    #m1 * m2 -> m2
    @staticmethod
    def mult( m1, m2 ):
        m = Matrix(m1.rows, m2.cols)
        for c in range( m.cols ):
            m.matrix.append([])
            for r in range( m.rows ):
                m.matrix[-1].append( 0 )
                for i in range(m1.cols):
                    m.matrix[c][r] += (m1.matrix[i][r] * m2.matrix[c][i])
        return m

    @staticmethod
    def ident(s=4):
        m = Matrix(s,s)
        for c in range( m.cols ):
            m.matrix[c][c] = 1
        return m
    
    def __init__(self, rows = 4, cols = 4):
        self.matrix = []
        self.rows = rows
        self.cols = cols
        for c in range( cols ):
            self.matrix.append( [] )
            for r in range( rows ):
                self.matrix[c].append( 0 )

    def print( self ):
        s = ""
        for r in range(self.rows):
            for c in range(self.cols):
                s += ("     "+str(self.matrix[c][r]))[-5:]
                s += ' '
            s += '\n'
        print(s)


    def add_edge( self, x0, y0, z0, x1, y1, z1 ):
        self.add_point(x0,y0,z0)
        self.add_point(x1,y1,z1)

    def add_point( self, x, y, z=0 ):
        self.matrix.append([])
        self.matrix[-1].append(x)
        self.matrix[-1].append(y)
        self.matrix[-1].append(z)
        self.matrix[-1].append(1)
        self.cols += 1



