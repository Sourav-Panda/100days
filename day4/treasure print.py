a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
try:
    b = (input("where do you want to place the treasure"))
    q = int(b[0])
    w = int(b[1])
    a[q][w] = 'x'
    for i in range(3):
        #clear
        # print(i)
        print(a[i])
except e:
    print("invalid input")