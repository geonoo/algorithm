sarr = [7,7,6,6,4,0,3,3]
ssarr = [1,1,3,3,7,15,9,9]
arr1 = 3
arr2 = [1,2,9,2]
arr3 = [1,13]



def star_print_star(a, b , c, d, e):

    for i in range(len(a)):
        print(" "*a[i]+"*"*b[i])
    print(" " * c + "*" * c + " " * c + "*" * c)
    print(" " * d[0] + "*" * d[1] + " " * d[2] + "*" * d[3])
    print("*"*e[0]+" "*e[1]+"*"*e[0])




star_print_star(sarr, ssarr, arr1, arr2, arr3)