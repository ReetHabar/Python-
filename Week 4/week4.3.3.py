def number_spiral(N):
    mat = [[0] * N for _ in range(N)]
    num = 1
    left, right, top, bottom = 0, N - 1, 0, N - 1
    
    while left <= right and top <= bottom: #left=0<=1 &top=0<=2-1=1
        for i in range(left, right + 1):
            mat[top][i] = num #top=0,left=0,right value =1+1=2
            num +=1  #num=num+1(1+1=2)
        top += 1
        for i in range(top, bottom + 1):
            mat[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            mat[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            mat[i][left] = num
            num += 1
        left += 1

    for row in mat:
        print(" ".join(f"{x:2}" for x in row))
    print()
number_spiral(2)
number_spiral(3)
number_spiral(4)
