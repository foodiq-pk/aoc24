import re



def get_multiplied_numbers_sum(data: str) -> int:
    numbers = re.findall(r"mul\((\d+),(\d+)\)", data)
    return sum([int(a)*int(b) for a,b in numbers])


def find_valid_instructions(data: str):
    data = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", data)
    return data

def parse_instructions(instructions):
    return [[x for x in instruction if x] for instruction in instructions]

def execute_instructions(clean_instructions):
    add_next_multiply = True
    number_sum = 0
    for instr in clean_instructions:
        match instr:
            case ["don't"]:
                add_next_multiply = False
            case ["do"]:
                add_next_multiply = True
            case [a,b]:
                if add_next_multiply:
                    number_sum += int(a) * int(b)

    return number_sum





with open("03/test-inp") as f:
    data = f.read()


print(get_multiplied_numbers_sum(data))


with open("03/test-inp2") as f:
    data = f.read()

print(execute_instructions(parse_instructions(find_valid_instructions(data))))




with open("03/input") as f:
    data = f.read()

print(get_multiplied_numbers_sum(data))

print(execute_instructions(parse_instructions(find_valid_instructions(data))))