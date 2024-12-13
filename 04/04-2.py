def find_x_mas_count(data):
    count = 0
    for i in range(1,len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == "A":
                match data[i-1][j-1], data[i+1][j+1], data[i-1][j+1], data[i+1][j-1]:
                    case "M", "S", "M", "S":
                        count +=1 
                    case "M", "S", "S", "M":
                        count +=1
                    case "S", "M", "M", "S":
                        count +=1
                    case "S", "M", "S", "M":
                        count +=1
                    case _:
                        continue
    return count




with open("04/test-input") as f:
    data = f.read().splitlines()

# for method in find_direction_methods:
#     print(method.__name__, method(data))
print(find_x_mas_count(data))



with open("04/input") as f:
    data = f.read().splitlines()

    print(find_x_mas_count(data))