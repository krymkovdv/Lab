numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count_of_numbers = len(numbers)
for i in range(len(numbers)):
    if numbers[i] == None:
        sum_of_numbers = sum(numbers[:i] + numbers[i+1:])
        numbers[i] = sum_of_numbers / count_of_numbers
        break
    else:
        i+=1
print("Измененный список:", numbers)
