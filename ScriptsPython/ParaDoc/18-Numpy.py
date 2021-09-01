a = np.array([34,25,7])
    print(type(a))
    print(a.shape)
    print(a[0],a[1],a[2])
    a[0]=5
    print(a[0],a[1],a[2])
    b = np.array([[1,2,3],[4,5,6]])
    print(b.shape)
    print(b[0,0],b[0,1],b[1,0])

    #matriz de 5 pos
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,0]
    lista3 = [4,6,1,5,0]
    matriz = np.array([lista1,lista2])
    #´reguntar als dimensiones de la matriz
    print(matriz.shape)
    #acceder a una pos especifica de la matriz
    print(matriz[1,2])#pos fila 2 y columna 3
    matriz[1,2]*=2
    print(matriz[1,2])#pos fila 2 y columna 3
    #imprimimos una matriz creada con 0 de 5*5
    matriz0 = np.zeros((5,5))
    print(matriz0)
    #imprimimos una matriz creada con 1 de 5*5
    matriz0 = np.ones((5,5))
    print(matriz0)
    #imprimimos una matriz y la llenamos con un valor x de 5*5
    y=7
    matriz0 = np.full((5,5),y)
    print(matriz0)
    # print("valor en la pos 0",x)
    #imprimimos una matriz y la llenamos con un valor x de 5*5    
    matriz0 = np.eye(5)
    print(matriz0)
    #matriz ramdon de 2*2
    e = np.random.random((2,2))
    print(e)

    #indexando matrices
    a = np.array([lista1,lista2,lista3])
    print(a,a.shape)
    #rebanando matrices
    b = a[0:2,1:3]
    print(b,b.shape)
    #actualizando valores y modificando la matriz    
    print(a[0,1])
    b[0,0]=77       # modificao la matriz ebanada
    print(a[0,1])   # observo como se actualzia la matriz original
    #invertir matriz en columnas
    print("matriz invertida",np.fliplr(a))
    #sectores
    print("Sectores".center(30,'-'))
    s = np.array([lista1,lista2,lista3])
    print(s)

    #mixto para capturar filas completas
    row_r1 = s[1,:]
    row_r2 = s[1:2,:]
    print(row_r1,row_r1.shape)
    print(row_r2,row_r2.shape)
    #mixto para capturar columnas completas
    col_r1 = s[:,1]
    col_r2 = s[:,1:2]
    print(col_r1,col_r1.shape)
    print(col_r2,col_r2.shape)
#indexacion de matrices de enteros
    print("Indexacion enteros unidos por fila y col".center(30,'-'))
    a = np.array([[1,2], [3, 4], [5, 6]])
    print(a,a.shape)
    row = [0,1,2]
    col = [0,1,0]
    print(a[row,col])
    '''
    [   [1 2]
        [3 4]
        [5 6]   ]
        rta = [1 4 5]
    '''
    print("Indexacion enteros separados".center(30,'-'))
    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))    

    print("Creacion desde la matriz anterios".center(30,'-'))
    print(a[[0, 0], [1, 1]])    
    print(np.array([a[0,1],a[0,1]]))

    print("Truco arange para mutar matriz".center(30,'-'))
    a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    '''
    [   [ 1  2  3]
        [ 4  5  6]
        [ 7  8  9]
        [10 11 12]  ] (4, 3)
    '''
    print(a,a.shape)
    b = np.arange(4)
    print(b)
    c = np.array([1,2,0,1])
    a[b,c] += 10
    print(a)
    
    print("Indexacion Boolneana".center(30,'-'))
    a = np.array([[1,2], [3, 4], [5, 6]])
    print(a)

    bool_idx = (a>2)

    print(bool_idx)

    print("Operaciones entre matrices".center(30,'-'))
    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)
    print(x)
    print(y)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(np.sqrt(x))

    print("Multiplicacion de matrices".center(30,'-'))
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])


    print(x)
    print(y)
    #estos son vectores
    print(v)
    print(w)
    #el prducto punbto de dos vctores da un valor numerico
    print("Multiplicacion vector y vector".center(60,'-'))
    print(v.dot(w))
    print("Multiplicacion vector y matiz".center(60,'-'))
    print(x.dot(v))
    print("Multiplicacion de matrices".center(60,'-'))
    print(x.dot(y))

    print("Trasponer una matriz".center(60,'-'))
    print(x)
    print(x.T)

    print("Broadcasting".center(60,'-'))
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    
    v = np.array([1,0,1])
    vv = np.tile(v,(4,1))
    print(vv)

    y = x+vv
    print(y)
    
    v = np.array([[1, 0],[3, 0]])
    print(v)
    print(3 in np.sum(v,axis=0))
    y = x+v
    print(y)
    # print("Un tercio = %f"%tercion)
    # print(f"El numero formateado es = {31}")
    # app.run(debug=True)#el debug = true es para trabajar en desarrollo