# Exemplo de entrada com saída esperada de -19:

arr = [
    [0, -4, -6, 0, -7, -6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3, -6, 0, -8, -6, -7]
]


def hourglassSum(arr):
    max_glass = arr[0][0] + arr[0][1] + arr[0][2] + \
        arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]

    for i in range(4):
        for j in range(4):
            glass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if glass > max_glass:
                max_glass = glass

    return max_glass


print(hourglassSum(arr))
