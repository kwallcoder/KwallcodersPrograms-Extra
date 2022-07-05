stop_Questions = False
number_List = []
number_Total = 0
while stop_Questions == False:
    user_Question = input("Input a number(Enter nothing to stop entering values):")
    if user_Question != "":
        number_List.append(user_Question)

    else:
        stop_Questions = True
        for i in range(0, len(number_List)):
                    number_Total += int(number_List[i])
        average = number_Total / len(number_List)

print("The average of the given numbers was", average)
