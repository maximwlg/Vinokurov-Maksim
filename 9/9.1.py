def smallest(matrix):
    smallest_elements = []    
    for i in range(len(matrix)):
        if i % 2 == 1:  
            smallest_element = min(matrix[i])  
            smallest_elements.append(smallest_element)              
    return smallest_elements

A = [
    [1, 2, 4],
    [4, 6, 5],
    [7, 8, 8],
    [1, 11, 12]
]

result =smallest(A)
print(result)