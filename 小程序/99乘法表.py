for i in range(1,10):

    for j in range(1,i+1):
        print(f"{i}x{j}={i*j}",end="  ")
        if i<=j :
            print()
