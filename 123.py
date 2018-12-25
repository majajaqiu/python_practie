import random

length = int(input())

array = []
for i in range( 0, length ):
    array.append([])
for i in range( 0, length ):
    for j in range( 0, length ):
        array[i].append( random.uniform( 1, 10 ) )

xvar = []
for i in range( 0, length ):
    xvar.append([])

answer = []
for i in range( 0, length ):
    answer.append( random.uniform( 1, 10 ) )

count = 0
for i in range(0, length):
    for j in range(0, length):
        if count % length == 0:
            print(end='\n')
        print( '%.5f' % array[i][j], end = '  \t' )
        count = count+1
    print( xvar[i], end = '\t' )
    print( '%.5f' % answer[i], end = '\t' )
print( end='\n' )

n = len(array)
for k in range( 0, n-1 ):
    for i in range( k+1, n ):
        tmp = array[i][k]
        for j in range( k, n ):
            array[i][j] = array[i][j] - array[k][j] / array[k][k] * tmp
        answer[i] = answer[i] - answer[k] / array[k][k] * tmp
count = 0
for i in range(0, length):
    for j in range(0, length):
        if count % length == 0:
            print(end='\n')
        print( '%.5f' % array[i][j], end = '  \t' )
        count = count+1
    print( xvar[i], end = '\t' )
    print( '%.5f' % answer[i], end = '\t' )
print( end='\n\n' )

for i in range( n-1, -1, -1):
    for j in range( n-1, -1, -1 ):
        xvar[i] = (answer[i] - array[i][j]) / array[i][i]

for i in range( 0, n ):
    print( xvar[i], end = '\n' )
