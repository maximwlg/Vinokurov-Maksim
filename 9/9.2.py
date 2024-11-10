def swap(matrix):
    minv = matrix[0][0]
    minx = (0, 0)
    maxv = matrix[0][0]
    maxx = (0, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < minv:
                minv = matrix[i][j]
                minx = (i, j)
            if matrix[i][j] > maxv:
                maxv = matrix[i][j]
                maxc = (i, j)
    
    
    matrix[minx[0]][minx[1]], matrix[maxx[0]][maxx[1]] = matrix[maxx[0]][maxx[1]], matrix[minx[0]][minx[1]]
    
    return matrix