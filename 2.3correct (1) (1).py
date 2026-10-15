
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
num_4 = int(input("Enter number 4: "))

if num_1 == num_2 == num_3 == num_4:
    print("All four numbers are equal")

elif num_1 == num_2 == num_3 and num_1 > num_4:
    print("Numbers 1, 2 and 3 are equal and greatest")

elif num_1 == num_2 == num_4 and num_1 > num_3:
    print("Numbers 1, 2 and 4 are equal and greatest")

elif num_1 == num_3 == num_4 and num_1 > num_2:
    print("Numbers 1, 3 and 4 are equal and greatest")

elif num_2 == num_3 == num_4 and num_2 > num_1:
    print("Numbers 2, 3 and 4 are equal and greatest")

elif num_1 == num_2 and num_1 > num_3 and num_1 > num_4:
    print("Numbers 1 and 2 are equal and greatest")

elif num_1 == num_3 and num_1 > num_2 and num_1 > num_4:
    print("Numbers 1 and 3 are equal and greatest")

elif num_1 == num_4 and num_1 > num_2 and num_1 > num_3:
    print("Numbers 1 and 4 are equal and greatest")

elif num_2 == num_3 and num_2 > num_1 and num_2 > num_4:
    print("Numbers 2 and 3 are equal and greatest")

elif num_2 == num_4 and num_2 > num_1 and num_2 > num_3:
    print("Numbers 2 and 4 are equal and greatest")

elif num_3 == num_4 and num_3 > num_1 and num_3 > num_2:
    print("Numbers 3 and 4 are equal and greatest")

elif num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
    print("Number 1 is greatest")

elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
    print("Number 2 is greatest")

elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4:
    print("Number 3 is greatest")

elif num_4 > num_1 and num_4 > num_2 and num_4 > num_3:
    print("Number 4 is greatest")
