#prompt user for input
height_of_shape = int(input("Enter height of shape: "))
#get the mid-point to start the decrease
decrease = height_of_shape / 2

#loop through the given height to print rows
for i in range (1, height_of_shape + 1):
        #condition to print * in an increasing succession
        if i <= decrease:
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
        #condition to print * in a decreasing succession
        else:
            for k in range(1, int(decrease)):
                print("*", end=" ")
            print()
            decrease -= 1
        height_of_shape -= 1