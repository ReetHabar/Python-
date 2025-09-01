def diamond_shape(N):
    for i in range(N):
        print(" " * (N - i - 1) + "* " * (i + 1))
    for i in range(N - 1):
        print(" " * (i + 1) + "* " * (N - i - 1))
    print()
diamond_shape(3)
diamond_shape(4)
diamond_shape(5)
