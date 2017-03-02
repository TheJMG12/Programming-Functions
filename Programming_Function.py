#1
def triangleArea(base,height):
    area = base*height//2
    return area

print(triangleArea(3,8))


#2
def convertFtoC(fahrenheight):
    celsius = (fahrenheight-32)*(5/9)
    return celsius

print(convertFtoC(95))

#3
def cubeArea(sideLength):
    area = 6*sideLength**2
    return area
print(cubeArea(6))

#4
'''
4.1 is 5
4.2 is 25
4.3 is 7
'''

#5
'''
A recursive function is a code which calls itselft multiple times depending
on how my times its set.
'''

#6
'''
35.
[][][][]
[][][]
[][]
[]
None

36.
10

37.
5

38.

def main():
    makeTriangle(1)

def makeTriangle(sideLength):
    if sideLength < 1: return
    makeTriangle(sideLength-1)
    print("[]"*sideLength)

main()
'''
