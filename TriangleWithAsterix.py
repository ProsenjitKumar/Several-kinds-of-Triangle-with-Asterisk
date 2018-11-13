
print("**************** Several kinds of Triangle with Asterisk **************")



# # **************************** 1 *******************************

n = int(input("Enter a integer number: "))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end="")
    print("\r")

# **************************** 2 *******************************


k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("*", end=" ")
    print("\r")

# **************************** 3 *******************************

def up_to_down_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print('' * ( t + 1 ) + '*' * i)
        return up_to_down_triangle( i - 1, t + 1 )

up_to_down_triangle(int(input("Enter a Number: ")))

# **************************** 4 *******************************
print("**************** Pyramid **************")

def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

triangle(int(input("Enter a number: ")))
