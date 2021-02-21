print("Do enter your name")
name = input()         # User enters his/her name

print("Welcome Potterhead " + name)      # Displays welcome message and name

print("\nEnter five random numbers!")
while True:
    try:
        num1 = float(input())
        num2 = float(input())
        num3 = float(input())
        num4 = float(input())
        num5 = float(input())
        num_list = [num5, num4, num3, num2, num1]
        num_list.sort()
        print(num_list)
        print("\nDone, see you soon!")
        break

    except ValueError:              # Catches errors not aligned with the float data type
        print("Kindly input numbers not words. Thanks much!")
        continue

