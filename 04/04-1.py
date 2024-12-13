def find_lr(data): # left_right ->
    count = 0
    locations = []
    for i in range(len(data)):
        for j in range(len(data[0])-3):
            if data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3] == "XMAS":
                count +=1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_rl(data): # right left <-
    count = 0
    locations = []
    for i in range(len(data)):
        for j in range(3, len(data)):
            if data[i][j] + data[i][j-1] + data[i][j-2] + data[i][j-3] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_td(data): # top down \|/
    count = 0
    locations = []
    for i in range(len(data) - 3):
        for j in range(len(data[i])):
            if data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_dt(data): # down top /|\
    count = 0
    locations = []
    for i in range(3, len(data)):
        for j in range(len(data[i])):
            if data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_tl_dr_lr(data): # top left right down diagonal _\|
    count = 0
    locations = []
    for i in range(len(data) - 3):
        for j in range(len(data[i]) - 3):
            if data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_tl_dr_rl(data): # top left right down diagonal ^\
    count = 0
    locations = []
    for i in range(3, len(data)):
        for j in range(3, len(data[i])):
            if data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3] == "XMAS":
                count += 1
                location = ([i,j],[i-3,j-3])
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_tr_dl_rl(data): #top right left down |/_
    count = 0
    locations = []

    for i in range(3, len(data)):
        for j in range(len(data[i]) - 3):
            if data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations

def find_tr_dl_lr(data): #top right left down /^
    count = 0
    locations = []
    for i in range(len(data) - 3):
        for j in range(3, len(data[i])):
            if data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] == "XMAS":
                count += 1
                locations.append(([i,j],[i+3,j-3]))
                
    return count, locations


find_direction_methods = [find_lr, find_rl, find_td, find_dt, find_tl_dr_lr, find_tl_dr_rl, find_tr_dl_lr, find_tr_dl_rl]

with open("04/test-input") as f:
    data = f.read().splitlines()

# for method in find_direction_methods:
#     print(method.__name__, method(data))

print(sum([method(data)[0] for method in find_direction_methods]))


with open("04/input") as f:
    data = f.read().splitlines()

# for method in find_direction_methods:
#     print(method.__name__, method(data))

print(sum([method(data)[0] for method in find_direction_methods]))
