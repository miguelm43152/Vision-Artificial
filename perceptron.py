# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Grupo: 6E

import numpy as np

def sign(z):
    if z >= 0:
        return 1
    if z < 0:
        return -1

alpha = 1/2
W = np.array( [1,1,1] )
x0 = 1
X = np.array( [ [x0,-1, -1],
                [x0,-1, 1 ],
                [x0,1, -1 ],
                [x0,1, 1  ]
    ])

Y = np.array( [-1,-1,-1,1] )

for n in range( len( X )):
    ys = sign( W[0]*X[n][0] + W[1]*X[n][1] + W[2]*X[n][2] )
    W = W + alpha*( Y[n] - ys)*X[n][0:3]
    W = W.astype( np.int8 )
    #print(W)

def compuertaAnd(x1,x2):
    return sign( W[0]*x0 + W[1]*x1 + W[2]*x2 )

for n in range( len(X)):
    print( compuertaAnd( X[n][1], X[n][2] ) )
