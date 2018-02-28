from subprocess import Popen, PIPE
from os import remove
from matrix import *

class PPMGrid(object):

    ############################################################################
    # original sauce
    ############################################################################

    #constants
    XRES = 500
    YRES = 500
    MAX_COLOR = 255
    RED = 0
    GREEN = 1
    BLUE = 2

    DEFAULT_COLOR = [0, 0, 0]

    def __init__( self, width = XRES, height = YRES ):
        self.screen = []
        for y in range( height ):
            row = []
            self.screen.append( row )
            for x in range( width ):
                self.screen[y].append( PPMGrid.DEFAULT_COLOR[:] )

    def plot( self, color, x, y ):
        newy = PPMGrid.YRES - 1 - y
        if ( x >= 0 and x < PPMGrid.XRES and newy >= 0 and newy < PPMGrid.YRES ):
            self.screen[newy][x] = color[:]

    def clear( self ):
        for y in range( len(self.screen) ):
            for x in range( len(self.screen[y]) ):
                self.screen[y][x] = PPMGrid.DEFAULT_COLOR[:]

    def save_ppm( self, fname ):
        f = open( fname, 'w' )
        ppm = 'P3\n' + str(len(self.screen[0])) +' '+ str(len(self.screen)) +' '+ str(PPMGrid.MAX_COLOR) +'\n'
        for y in range( len(self.screen) ):
            row = ''
            for x in range( len(self.screen[y]) ):
                pixel = self.screen[y][x]
                row+= str( pixel[ PPMGrid.RED ] ) + ' '
                row+= str( pixel[ PPMGrid.GREEN ] ) + ' '
                row+= str( pixel[ PPMGrid.BLUE ] ) + ' '
            ppm+= row + '\n'
        f.write( ppm )
        f.close()

    def save_extension( self, fname ):
        ppm_name = fname[:fname.find('.')] + '.ppm'
        self.save_ppm( ppm_name )
        p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
        p.communicate()
        remove(ppm_name)

    def display( self ):
        ppm_name = 'pic.ppm'
        self.save_ppm( ppm_name )
        p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
        p.communicate()
        remove(ppm_name)

    ############################################################################
    # line
    ############################################################################

    def draw_line( self, x0, y0, x1, y1, color ):
        if ( x1 < x0 ):
            (x0, x1) = (x1, x0)
            (y0, y1) = (y1, y0)
        a = y1 - y0
        b = x0 - x1
        (x,y) = (x0,y0)
        if ( 0 <= a <= -b ): # oct 1
            d = 2*a + b
            while ( x <= x1 ):
                self.plot( color, x, y)
                if ( d > 0 ):
                    y += 1
                    d += 2*b
                x += 1
                d += 2*a
            return
        if ( -b <= a ): # oct 2
            d = a + 2*b
            while ( y <= y1 ):
                self.plot( color, x, y)
                if ( d < 0 ):
                    x += 1
                    d += 2*a
                y += 1
                d += 2*b
            return
        if ( b <= a <= 0 ): # oct 8
            d = 2*a - b
            while ( x <= x1 ):
                self.plot( color, x, y)
                if ( d < 0 ):
                    y -= 1
                    d -= 2*b
                x += 1
                d += 2*a
            return
        if ( a <= b ): # oct 7
            d = a - 2*b
            while ( y >= y1 ):
                self.plot( color, x, y)
                if ( d > 0 ):
                    x += 1
                    d += 2*a
                y -= 1
                d -= 2*b
            return

    ############################################################################
    # matrix
    ############################################################################

    def draw_lines( self, matrix, color ):
        for c in range(matrix.cols//2):
            self.draw_line( matrix.matrix[c*2][0],
                            matrix.matrix[c*2][1],
                            matrix.matrix[c*2+1][0],
                            matrix.matrix[c*2+1][1],
                            color )
                            
        

