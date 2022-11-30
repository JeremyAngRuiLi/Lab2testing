def get_user_input():
    x=int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    z = int(input("Enter third value: "))

    print("The values are" + str(x) + "," + str(y) + "," + str(z))
    return [x,y,z]

def calc_average(user_input):
    average= sum(user_input)/len(user_input)
    print("Average is: " , average)

def find_min_max(user_input):
    print("The largest number is: "+str(max(user_input)))
    print("The smallest number is: "+str(min(user_input)))

def sort_tem(user_input):
    print(sorted(user_input))

def calc_median_temperature(user_input):
    middle_index = (len(user_input) + 1) // 2
    print(user_input[middle_index - 1])


def main():
    user_input=get_user_input()
    calc_average(user_input)
    find_min_max(user_input)
    sort_tem(user_input)
    calc_median_temperature(user_input)



if __name__ == "__main__":
    main()