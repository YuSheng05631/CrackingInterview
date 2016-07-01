"""
A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
The height of the screen, of course, can be derived from the length of the array and the width.
Implement a function drawHorizontalLine(byte[] screen, int width, int x1, int x2, int y) which draws a horizontal line from (x1, y)to(x2, y).
"""

def drawHorizontalLine(screen, width, x1, x2, y):

    startBit = width * y + x1
    endBit = startBit + (x2 - x1 + 1)
    if x1 < 0 or x2 < 0 or x1 > x2 or x2 >= width or endBit > len(screen):
        return "Error"
    return screen[startBit:endBit]


n = 0b10011001
n <<= 8; n += 0b11110000
n <<= 8; n += 0b10101111
n <<= 8; n += 0b01010000
screen = list()
while n > 0:
    screen.insert(0, n%2)
    n >>= 1
print(screen)
print(drawHorizontalLine(screen, 8, 2, 7, 1))
print(drawHorizontalLine(screen, 8, 2, 2, 1))
print(drawHorizontalLine(screen, 8, 2, 7, 4))
print(drawHorizontalLine(screen, 4, 1, 2, 4))
