import Helper as santasLilHelper
import math

def Day1_ReportRepair(target):
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day1_Input.txt"
    file = open(filepath, 'r')
    expenseReport = file.readlines()

    for i in range(0, len(expenseReport) - 2):
        for j in range(i+1, len(expenseReport) - 1):
            if(int(expenseReport[i]) + int(expenseReport[j]) == target):
                return int(expenseReport[i]), int(expenseReport[j]), int(expenseReport[i]) * int(expenseReport[j])


def Day1_ReportRepair_2(target):
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day1_Input.txt"
    file = open(filepath, 'r')
    expenseReport = file.readlines()

    for i in range(0, len(expenseReport) - 3):
        for j in range(i+1, len(expenseReport) - 2):
            for k in range(i+1, len(expenseReport) - 1):
                if int(expenseReport[i]) + int(expenseReport[j]) + int(expenseReport[k]) == target:
                    return int(expenseReport[i]), int(expenseReport[j]), int(expenseReport[k]), int(expenseReport[i]) * int(expenseReport[j]) * int(expenseReport[k])


def Day2_PasswordRepair():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day2_Input.txt"
    file = open(filepath, 'r')
    passwordList = file.readlines()

    validCount = 0

    for line in passwordList:
        parts = line.split()
        range = parts[0].split('-')
        charDirty = parts[1]
        specialChar = charDirty[0]
        password = parts[2]

        charCount = 0
        for curChar in password:
            if curChar == specialChar:
                charCount += 1


        #print(specialChar + str(charCount) +' : ' + str(int(range[0])))
        if charCount >= int(range[0]) and charCount <= int(range[1]):
            validCount += 1

    return validCount


def Day2_PasswordRepair_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day2_Input.txt"
    file = open(filepath, 'r')
    passwordList = file.readlines()

    validCount = 0

    for line in passwordList:
        parts = line.split()
        index = parts[0].split('-')
        charDirty = parts[1]
        specialChar = charDirty[0]
        password = parts[2]

        if (password[int(index[0])-1] == specialChar) != (password[int(index[1])-1] == specialChar):
            validCount += 1

    return validCount


def Day3_TobagganPath():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day3_Input.txt"
    file = open(filepath, 'r')
    terrainMap = file.readlines()

    # -1 to remove line endings
    width = len(terrainMap[0]) - 1
    height = len(terrainMap)

    # slope defined as horizontal distance (+ive to the right) over vert distance (+ive going down)
    slope = 3

    treeCount = 0

    for i in range(0, height):
        colIndex = (i*slope) % width

        if(terrainMap[i][colIndex] == '#'):
            treeCount += 1
        elif(terrainMap[i][colIndex] != '.'):
            return -1

    return treeCount


def Day3_TobagganPath_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day3_Input.txt"
    file = open(filepath, 'r')
    terrainMap = file.readlines()

    treeCount =[]

    treeCount.append(santasLilHelper.tobaggan_path_calc(terrainMap, 1, 1))
    treeCount.append(santasLilHelper.tobaggan_path_calc(terrainMap, 3, 1))
    treeCount.append(santasLilHelper.tobaggan_path_calc(terrainMap, 5, 1))
    treeCount.append(santasLilHelper.tobaggan_path_calc(terrainMap, 7, 1))
    treeCount.append(santasLilHelper.tobaggan_path_calc(terrainMap, 1, 2))

    product = 1
    for cur in treeCount:
        product *= cur

    return product


def Day4_PassportValidation():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day4_Input.txt"
    file = open(filepath, 'r')
    batchPassports = file.readlines()

    passport_list = santasLilHelper.parse_batch_passports(batchPassports)

    valid_count = 0

    for passport in passport_list:
        if santasLilHelper.validate_passport(passport):
            valid_count += 1

    return valid_count


def Day4_PassportValidation_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day4_Input.txt"
    file = open(filepath, 'r')
    batchPassports = file.readlines()

    passport_list = santasLilHelper.parse_batch_passports(batchPassports)

    valid_count = 0

    for passport in passport_list:
        if santasLilHelper.validate_passport_2(passport):
            valid_count += 1

    return valid_count


def Day5_SeatSearch():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day5_Input.txt"
    file = open(filepath, 'r')
    boarding_pass_list = file.readlines()

    max_seat_id = -1
    max_row = 128
    max_col = 8
    for boarding_pass in boarding_pass_list:
        row_cursor = max_row
        cur_row = 0

        col_cursor = max_col
        cur_col = 0

        for cur_char in boarding_pass:
            if cur_char == 'B':
                row_cursor = row_cursor/2
                cur_row += row_cursor
            elif cur_char == 'F':
                row_cursor = row_cursor/2

            elif cur_char == 'R':
                col_cursor = col_cursor/2
                cur_col += col_cursor
            elif cur_char == 'L':
                col_cursor = col_cursor/2

        cur_seat_id = cur_row * 8 + cur_col

        if False: #Debug
            print(boarding_pass.rstrip() + ': (' + str(cur_row) + ', ' + str(cur_col) + ') - ' +str(cur_seat_id))

        max_seat_id = max(max_seat_id, cur_seat_id)

    return max_seat_id


def Day5_SeatSearch_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day5_Input.txt"
    file = open(filepath, 'r')
    boarding_pass_list = file.readlines()
    all_seat_id = []

    max_row = 128
    max_col = 8
    for boarding_pass in boarding_pass_list:
        row_cursor = max_row
        cur_row = 0

        col_cursor = max_col
        cur_col = 0

        for cur_char in boarding_pass:
            if cur_char == 'B':
                row_cursor = row_cursor/2
                cur_row += row_cursor
            elif cur_char == 'F':
                row_cursor = row_cursor/2

            elif cur_char == 'R':
                col_cursor = col_cursor/2
                cur_col += col_cursor
            elif cur_char == 'L':
                col_cursor = col_cursor/2

        cur_seat_id = cur_row * 8 + cur_col

        all_seat_id.append(cur_seat_id)

        if(False): #Debug
            print(boarding_pass.rstrip() + ': (' + str(cur_row) + ', ' + str(cur_col) + ') - ' +str(cur_seat_id))

    all_seat_id.sort()

    compare_id = all_seat_id[0]
    for i in range(1, len(all_seat_id)):
        if all_seat_id[i] != compare_id + 1:
            return compare_id + 1

        compare_id += 1

    return -1


def Day6_CustomsDeclaration():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day6_Input.txt"
    file = open(filepath, 'r')
    batch_declarations = file.readlines()

    declaration_list = santasLilHelper.parse_batch_customs_declarations(batch_declarations)

    total_count = 0

    for group_declaration in declaration_list:
        group_answers = {}

        for individual_declaration in group_declaration:
            for answer in individual_declaration:
                if answer not in group_answers.keys():
                    group_answers[answer] = 1
                else:
                    group_answers[answer] = group_answers[answer] + 1

        total_count += len(group_answers)

    return total_count


def Day6_CustomsDeclaration_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day6_Input.txt"
    file = open(filepath, 'r')
    batch_declarations = file.readlines()

    declaration_list = santasLilHelper.parse_batch_customs_declarations(batch_declarations)

    total_count = 0

    for group_declaration in declaration_list:
        group_answers = {}

        for individual_declaration in group_declaration:
            for answer in individual_declaration:
                if answer not in group_answers.keys():
                    group_answers[answer] = 1
                else:
                    group_answers[answer] = group_answers[answer] + 1

        for answer_count in group_answers.values():
            if answer_count == len(group_declaration):
                total_count += 1

    return total_count


def Day7_LuggageCheck():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day7_Input.txt"
    file = open(filepath, 'r')
    batch_luggage_rules = file.readlines()

    luggage_rules = santasLilHelper.parse_batch_luggage_rules(batch_luggage_rules)

    search_bag = {'shiny gold'}
    searched = set()
    candidates = santasLilHelper.search_for_candidate(search_bag, searched, luggage_rules)

    candidates.difference_update(search_bag)

    return len(candidates)


def Day7_LuggageCheck_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day7_Input.txt"
    file = open(filepath, 'r')
    batch_luggage_rules = file.readlines()

    luggage_rules = santasLilHelper.parse_batch_luggage_rules(batch_luggage_rules)

    return santasLilHelper.calculate_contained_bags('shiny gold', luggage_rules)


def Day8_GameRepair():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day8_Input.txt"
    file = open(filepath, 'r')
    batch_game_instructions = file.readlines()

    game_instructions = santasLilHelper.parse_batch_game_instructions(batch_game_instructions)

    acc_val = 0
    index = 0

    while(game_instructions[index][2] < 1):
        index, acc_val = santasLilHelper.run_instruction(index, acc_val, game_instructions)

    return acc_val


def Day8_GameRepair_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day8_Input.txt"
    file = open(filepath, 'r')
    batch_game_instructions = file.readlines()

    game_instructions = santasLilHelper.parse_batch_game_instructions(batch_game_instructions)

    # toggled instruction index
    toggle_index = 0

    error_found = False

    while(not error_found):
        test_flag = False
        if game_instructions[toggle_index][0] == 'jmp':
            game_instructions[toggle_index][0] = 'nop'
            test_flag = True
        elif game_instructions[toggle_index][0] == 'nop':
            game_instructions[toggle_index][0] = 'jmp'
            test_flag = True

        repeat_found = False

        if(test_flag):
            index = 0
            acc_val = 0

            while(not repeat_found and not error_found):

                index, acc_val = santasLilHelper.run_instruction(index, acc_val, game_instructions)

                if index >= len(game_instructions):
                    error_found = True

                elif game_instructions[index][2] == 1:
                    repeat_found = True

        if(not error_found):
            if game_instructions[toggle_index][0] == 'jmp':
                game_instructions[toggle_index][0] = 'nop'
            elif game_instructions[toggle_index][0] == 'nop':
                game_instructions[toggle_index][0] = 'jmp'

            for instruction in game_instructions:
                instruction[2] = 0

        toggle_index += 1

    return acc_val


def Day9_EncodingError():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day9_Input.txt"
    file = open(filepath, 'r')
    code_stream = file.readlines()

    preamble_len = 25

    for i in range(preamble_len, len(code_stream)):
        valid_flag = False

        for j in range(i-preamble_len, i - 1):
            for k in range(i-preamble_len + 1, i):
                val1 = int(code_stream[j])
                val2 = int(code_stream[k])
                cur_val = int(code_stream[i])

                if val1 + val2 == cur_val:
                    valid_flag = True

                    if(False): #Debug
                        print('Valid combination found at index: ' + str(i) + ', combination of (' + str(val1) + ', ' + str(val2) +') at indices (' + str(j) + ', ' + str(k) + ')')

                    continue

            if valid_flag:
                continue

        if not valid_flag:
            return int(code_stream[i])

    return -1


def Day9_EncodingError_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day9_Input.txt"
    file = open(filepath, 'r')
    code_stream = file.readlines()

    invalid_num = int(Day9_EncodingError())

    i_start = - 1
    i_end = 0

    set_found = False

    debug_str = 'Sum Start: '
    while not set_found and i_start < len(code_stream):
        cur_sum = 0
        i_start += 1
        for i in range(i_start, len(code_stream) - 1):
            debug_str += str(code_stream[i]) + ' + '

            cur_sum += int(code_stream[i])
            i_end = i
            if cur_sum == invalid_num:
                set_found = True
                break
            elif cur_sum > invalid_num:
                break

        if(False): #Debug
            debug_str = debug_str[:-2] + '= ' + str(cur_sum) + ', indexRange (' + str(i_start) + ', ' + str(i_end) + ')'
            debug_str += ', Invalid Num: ' + str(invalid_num)
            
            print(debug_str)
            debug_str = 'Sum Start: '

    max = -1
    min = invalid_num + 1

    for i in range(i_start, i_end + 1):
        cur_val = int(code_stream[i])

        if cur_val > max:
            max = cur_val

        if cur_val < min:
            min = cur_val

    return max + min


def Day10_AdapterArray():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day10_Input.txt"
    file = open(filepath, 'r')
    jolts_list_str = file.readlines()

    # 0 for outlet start voltage
    jolts_list =[0]
    for jlt_str in jolts_list_str:
        jlt = int(jlt_str.rstrip())
        jolts_list.append(jlt)

    # Add adapter voltage
    jolts_list.append(max(jolts_list) + 3)
    jolts_list.sort()

    diff_array = [0, 0, 0]
    jlt_sum = 0

    for i in range(1, len(jolts_list)):
        front_jlt = jolts_list[i]
        back_jlt = jolts_list[i - 1]
        diff = int(front_jlt - back_jlt - 1)
        jlt_sum += diff+1

        diff_array[diff] += 1

    return diff_array, jlt_sum, diff_array[0]*diff_array[2]


def Day10_AdapterArray_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day10_Input.txt"
    file = open(filepath, 'r')
    jolts_list_str = file.readlines()

    # 0 for outlet start voltage
    jolts_list = [0]
    for jlt_str in jolts_list_str:
        jlt = int(jlt_str.rstrip())
        jolts_list.append(jlt)

    # Add adapter voltage
    jolts_list.append(max(jolts_list) + 3)
    jolts_list.sort()

    adapter_tree = santasLilHelper.build_adapter_tree(jolts_list)

    return santasLilHelper.calculate_tree_branch_count(adapter_tree, jolts_list)


def Day11_SeatingSystem():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day11_Input.txt"
    file = open(filepath, 'r')
    raw_seat_map = file.readlines()
    seat_map = []

    for row in raw_seat_map:
        seat_map.append(row.strip())

    prev_seat_map = seat_map
    duplicate_found = False

    while not duplicate_found:
        seat_map = santasLilHelper.get_next_seat_state(seat_map)

        if seat_map == prev_seat_map:
            duplicate_found = True

        prev_seat_map = seat_map

    occ_count = 0
    for row in seat_map:
        for seat in row:
            if seat == '#':
                occ_count += 1

    #print(seat_map)

    return occ_count


def Day11_SeatingSystem_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day11_Input.txt"
    file = open(filepath, 'r')
    raw_seat_map = file.readlines()
    seat_map = []

    for row in raw_seat_map:
        seat_map.append(row.strip())

    prev_seat_map = seat_map
    duplicate_found = False

    while not duplicate_found:
        seat_map = santasLilHelper.get_next_seat_state_2(seat_map)

        if seat_map == prev_seat_map:
            duplicate_found = True

        prev_seat_map = seat_map

    occ_count = 0
    for row in seat_map:
        for seat in row:
            if seat == '#':
                occ_count += 1

    #print(seat_map)

    return occ_count


def Day12_RainRisk():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day12_Input.txt"
    file = open(filepath, 'r')
    instruction_list = file.readlines

    # E, N, rotation (CCW +ve)
    ship_state = [0, 0, 0]

    for instruction in instruction_list:
        instr = str(instruction[0])
        val = int(instruction[1:])
        ship_state = santasLilHelper.move_ship(ship_state, instr, val)

    return ship_state, math.fabs(ship_state[0]) + math.fabs(ship_state[1])


def Day12_RainRisk_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day12_Input.txt"
    file = open(filepath, 'r')
    instruction_list = file.readlines()

    # E +ve, N +ve
    ship_state = [0, 0]
    waypoint_state = [10, 1]

    for instruction in instruction_list:
        instr = str(instruction[0])
        val = int(instruction[1:])
        ship_state = santasLilHelper.move_ship_2(ship_state, waypoint_state, instr, val)

    return ship_state, waypoint_state, math.fabs(ship_state[0]) + math.fabs(ship_state[1])


def Day13_ShuttleSearch():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day13_Input.txt"
    file = open(filepath, 'r')
    bus_schedule = file.readlines()

    depart_time = int(bus_schedule[0])
    in_service_list_raw = bus_schedule[1].strip().split(',')
    in_service_list = []

    for id in in_service_list_raw:
        if id != 'x':
            in_service_list.append(int(id))


    closest_times = {}

    for id in in_service_list:
        closest_mins = id
        while(closest_mins < depart_time):
            closest_mins += id

        closest_times[id] = closest_mins

    best_time = [-1, 2*depart_time]
    for id in closest_times.keys():
        if closest_times[id] < best_time[1]:
            best_time = [id, closest_times[id]]

    return best_time[0]*(best_time[1]-depart_time)


def Day13_ShuttleSearch_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day13_Input.txt"
    file = open(filepath, 'r')
    bus_schedule = file.readlines()

    in_service_list = bus_schedule[1].strip().split(',')

    for i in range(0, len(in_service_list)):
        if in_service_list[i] != 'x':
            in_service_list[i] = int(in_service_list[i])

    lcd_index = 1
    lcd = 1
    t = 0
    found = False

    while not found:
        t += lcd

        xcount = 0
        for i in range(0, len(in_service_list)):
            if in_service_list[i] != 'x':
                if santasLilHelper.is_multiple(int(t + i), int(in_service_list[i])):

                    lcd = lcd * int(in_service_list[i])
                    in_service_list[i] = 'x'
                    lcd_index += 1
            else:
                xcount += 1

        if xcount == len(in_service_list):
            return t - lcd

    return t


def Day14_DockingData():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day14_Input.txt"
    file = open(filepath, 'r')
    instr_list_batch = file.readlines()

    instr_list = santasLilHelper.parse_mem_instructions(instr_list_batch)

    mem = {}
    mask = ''

    for i in range(0, len(instr_list)):
        mem, mask = santasLilHelper.parse_instr(instr_list[i], mem, mask)

    sum = 0
    for addr, val in mem.items():
        sum += val


    return sum


def Day14_DockingData_2():
    filepath = "C:\\Users\\User\\PycharmProjects\\Advent of Code 2020\\Day14_Input.txt"
    file = open(filepath, 'r')
    instr_list_batch = file.readlines()

    instr_list = santasLilHelper.parse_mem_instructions(instr_list_batch)

    mem = {}
    mask = ''

    for i in range(0, len(instr_list)):
        mem, mask = santasLilHelper.parse_instr_2(instr_list[i], mem, mask)

    sum = 0
    for addr, val in mem.items():
        sum += val


    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if(False):
        print('Day 1 Part 1: ' + str(Day1_ReportRepair(2020)))
        print('Day 1 Part 2: ' + str(Day1_ReportRepair_2(2020)))
        print('Day 2 Part 1: ' + str(Day2_PasswordRepair()))
        print('Day 2 Part 2: ' + str(Day2_PasswordRepair_2()))
        print('Day 3 Part 1: ' + str(Day3_TobagganPath()))
        print('Day 3 Part 2: ' + str(Day3_TobagganPath_2()))
        print('Day 4 Part 1: ' + str(Day4_PassportValidation()))
        print('Day 4 Part 2: ' + str(Day4_PassportValidation_2()))
        print('Day 5 Part 1: ' + str(Day5_SeatSearch()))
        print('Day 5 Part 2: ' + str(Day5_SeatSearch_2()))
        print('Day 6 Part 1: ' + str(Day6_CustomsDeclaration()))
        print('Day 6 Part 2: ' + str(Day6_CustomsDeclaration_2()))
        print('Day 7 Part 1: ' + str(Day7_LuggageCheck()))
        print('Day 7 Part 2: ' + str(Day7_LuggageCheck_2()))
        print('Day 8 Part 1: ' + str(Day8_GameRepair()))
        print('Day 8 Part 2: ' + str(Day8_GameRepair_2()))
        print('Day 9 Part 1: ' + str(Day9_EncodingError()))
        print('Day 9 Part 2: ' + str(Day9_EncodingError_2()))
        print('Day 10 Part 1: ' + str(Day10_AdapterArray()))
        print('Day 10 Part 2: ' + str(Day10_AdapterArray_2()))
        print('Day 11 Part 1: ' + str(Day11_SeatingSystem()))
        print('Day 11 Part 2: ' + str(Day11_SeatingSystem_2()))
        print('Day 12 Part 1: ' + str(Day12_RainRisk()))
        print('Day 12 Part 2: ' + str(Day12_RainRisk_2()))
        print('Day 13 Part 1: ' + str(Day13_ShuttleSearch()))
        print('Day 13 Part 2: ' + str(Day13_ShuttleSearch_2()))
        print('Day 14 Part 1: ' + str(Day14_DockingData()))

    print('Day 14 Part 12: ' + str(Day14_DockingData_2()))