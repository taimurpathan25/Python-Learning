row = 5;

for i in range(row, 0, -1):

    for j in range(row - i):
        print("  ", end="")

    for k in range(i):
        print("* ", end="")

    print()


# n = 5;
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ", end=" ");
#     for k in range(i):
#         print("*",end=" ");
#     print()