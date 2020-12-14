import math

#Day 3 Helper
def tobaggan_path_calc(terrainMap, slopex, slopey):
    # -1 to remove line endings
    width = len(terrainMap[0]) - 1
    height = len(terrainMap)

    treeCount = 0

    colIndex = 0
    for i in range(0, height, slopey):
        if (terrainMap[i][colIndex] == '#'):
            treeCount += 1
        elif (terrainMap[i][colIndex] != '.'):
            return -1

        colIndex = (colIndex + slopex) % width

    return treeCount

#Day 4 Helper
def validatebyr(byr):
    try:
        val = int(byr)
        if val < 1920 or val > 2002:
            return False
    except:
        return False

    return True


def validateiyr(iyr):
    try:
        val = int(iyr)
        if val < 2010 or val > 2020:
            return False
    except:
        return False

    return True


def validateeyr(eyr):
    try:
        val = int(eyr)
        if val < 2020 or val > 2030:
            return False
    except:
        return False

    return True


def validatehgt(hgt):
    try:
        val = int(hgt[0:-2])
        units = hgt[-2:]

        if units == 'cm':
            if val < 150 or val > 193:
                return False
        elif units == 'in':
            if val < 59 or val > 76:
                return False
        else:
            return False
    except:
        return False

    return True


def validatehcl(hcl):
    if hcl[0] != '#':
        return False

    if len(hcl) != 7:
        return False

    for i in range(1, len(hcl)):
        chr_ord = ord(hcl[i])

        if chr_ord >= 48 and chr_ord <= 57: #Digits 0-9
            continue
        elif chr_ord >= 97 and chr_ord <= 102: #Letters a-f
            continue
        else:
            return False

    return True


def validateecl(ecl):
    if(ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry'
            or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
        return True

    return False


def validatepid(pid):
    if len(pid) != 9:
        return False

    for i in range(0, len(pid)):
        chr_ord = ord(pid[i])
        if chr_ord >= 48 and chr_ord <= 57: #Digits 0-9
            continue
        else:
            return False

    return True


def validatecid(cid):
    return True


required_pp_fields = {
    'byr': validatebyr,
    'iyr': validateiyr,
    'eyr': validateeyr,
    'hgt': validatehgt,
    'hcl': validatehcl,
    'ecl': validateecl,
    'pid': validatepid,
    'cid': validatecid
}


def parse_batch_passports(batchPassports):
    passport_list = []

    passport = {}
    for line in batchPassports:
        kv_pair_list = line.rstrip().split(' ')

        if kv_pair_list[0] == '': # detect blank line
            passport_list.append(passport)
            passport = {}
        else:
            for kv_pair in kv_pair_list:
                kv = kv_pair.split(':')
                passport[kv[0]] = kv[1]

    passport_list.append(passport)
    return passport_list


def validate_passport(passport):
    for rq_key in required_pp_fields.keys():
        if rq_key == 'cid':
            continue
        if rq_key not in passport:
            return False
    return True


def validate_passport_2(passport):
    for rq_key in required_pp_fields.keys():
        if rq_key == 'cid':
            continue
        if rq_key not in passport:
            return False

        if not required_pp_fields[rq_key](passport[rq_key]):
            if(False): #Debug
                print('Failed ' + rq_key + ' check.')
                print(passport)
            return False

    return True


#Day 6 Helper
def parse_batch_customs_declarations(batch_declarations):
    declaration_list = []
    group_declaration = []

    for line in batch_declarations:
        if line.rstrip() == '':  # detect blank line
            declaration_list.append(group_declaration)
            group_declaration = []
        else:
            group_declaration.append(line.rstrip())

    declaration_list.append(group_declaration)
    return declaration_list


#Day 7 Helper
def parse_batch_luggage_rules(batch_luggage_rules):
    luggage_rules = {}

    for line in batch_luggage_rules:
        rule_tokens = line.rstrip().rstrip('.').split(' bags contain ')

        cur_rules = rule_tokens[1].split(', ')
        cur_rule_dict = {}

        for rule in cur_rules:
            if 'no other bags' not in rule:
                val = int(rule.split(' ')[0])
                key = rule.replace(str(val) + ' ', '').replace('bags', 'bag').replace(' bag', '')
                cur_rule_dict[key] = val

        luggage_rules[rule_tokens[0]] = cur_rule_dict

    return luggage_rules


def search_for_candidate(candidates, searched, luggage_rules):
    new_candidates = set()

    search_count = 0
    for search_bag in candidates:
        if search_bag not in searched:
            search_count += 1
            searched.add(search_bag)
            for bag_rule in luggage_rules.keys():
                if bag_rule != search_bag:
                    for contained_bag in luggage_rules[bag_rule].keys():
                        if contained_bag == search_bag:
                            new_candidates.add(bag_rule)
                            if(False): #Debug
                                print('Identified candidate: ' + bag_rule)
                                print(luggage_rules[bag_rule])

    candidates = candidates.union(new_candidates)

    if search_count == 0:
        return candidates
    else:
        return search_for_candidate(candidates, searched, luggage_rules)


def calculate_contained_bags(parent_bag, luggage_rules):

    parent_bag_count = 0
    printStr = parent_bag + ' contains '
    if len(luggage_rules[parent_bag]) != 0:
        for child_bag in luggage_rules[parent_bag].keys():
            cur_bag_count = luggage_rules[parent_bag][child_bag]
            contained_bag_count = calculate_contained_bags(child_bag, luggage_rules)
            parent_bag_count += (contained_bag_count * cur_bag_count) + cur_bag_count

            printStr += str(cur_bag_count) + ' ' + child_bag + ' bags, '
    else:
        printStr += 'no bags  '

    if(False): # Debug
        print(printStr[:-2] + ' which totals ' + str(parent_bag_count) + ' bags')
        print(luggage_rules[parent_bag])

    return parent_bag_count


#Day 8 Helper
def parse_batch_game_instructions(batch_game_instructions):
    game_instructions = []

    for line in batch_game_instructions:
        tokens = line.rstrip().split(' ')
        instruction = tokens[0]
        val = int(tokens[1][1:])
        val_sign = tokens[1][0]

        if val_sign == '-':
            val *= -1

        full_instruction = [instruction, val, 0]
        game_instructions.append(full_instruction)

    return game_instructions


def run_instruction(index, acc_val, game_instructions):
    new_index = index
    new_acc_val = acc_val

    game_instructions[index][2] += 1

    if game_instructions[index][0] == 'nop':
        new_index += 1
    elif game_instructions[index][0] == 'acc':
        new_acc_val += game_instructions[index][1]
        new_index += 1
    elif game_instructions[index][0] == 'jmp':
        new_index += game_instructions[index][1]

    return new_index, new_acc_val


#Day 10 Helper
def build_adapter_tree(jolts_list):
    adapter_tree = {}

    for i in range(0, len(jolts_list)-1):
        cur_adap_jlt = jolts_list[i]

        tail_nodes = []

        for j in range(i + 1, min(i+4, len(jolts_list))):
            test_adap_jlt = jolts_list[j]
            diff = test_adap_jlt - cur_adap_jlt

            #print('   ' + str(test_adap_jlt) + ' - ' + str(cur_adap_jlt) + ' = ' + str(diff))
            if diff <= 3:
                tail_nodes.append(test_adap_jlt)

        adapter_tree[str(cur_adap_jlt)] = tail_nodes

    # Now we have a dictionary with each kv pair consisting of the jolt voltage and all adapters that can plug into it
    return adapter_tree


def calculate_tree_branch_count(adapter_tree, jolts_list):
    final_jlt = str(max(jolts_list))

    adapter_branch_count = {final_jlt: 1}

    for i in range(len(jolts_list) - 2, -1, -1):
        cur_jlt = str(jolts_list[i])

        cur_cumulative_branch_count = 0

        for branch in adapter_tree[cur_jlt]:
            cur_cumulative_branch_count += adapter_branch_count[str(branch)]

        adapter_branch_count[cur_jlt] = cur_cumulative_branch_count

    # Now adapter_branch_count contains adapters with their cumulative branch count up to that point from the leaf level.
    # Total branches should just be the sum of the first node's branch counts

    return adapter_branch_count['0']


#Day 11 Helper
def get_next_seat_state(seat_map):
    new_seat_map = []
    for row in seat_map:
        new_seat_map.append(row)

    row_max = len(seat_map)
    col_max = len(seat_map[0])

    for i in range(0, row_max):
        for j in range(0, col_max):
            #print('Start: ('+str(i) + ', ' + str(j) + ')')
            cur_seat = seat_map[i][j]
            if cur_seat != '.':
                row_check_range = range(max(0, i-1), min(i+2, row_max))
                col_check_range = range(max(0, j-1), min(j+2, col_max))

                adjacent_occ_count = 0
                for x in row_check_range:
                    for y in col_check_range:
                        check_seat = seat_map[x][y]
                        #print('From (' + str(i) + ', ' + str(j) + ') to (' + str(x) + ', ' + str(y) + ') : ' + check_seat)
                        if not (x == i and y == j) and seat_map[x][y] == '#':
                            adjacent_occ_count += 1

                if cur_seat == 'L' and adjacent_occ_count == 0:
                    new_seat_map[i] = new_seat_map[i][0:j] + '#' + new_seat_map[i][j+1:]
                elif cur_seat == '#' and adjacent_occ_count >= 4:
                    new_seat_map[i] = new_seat_map[i][0:j] + 'L' + new_seat_map[i][j+1:]

    return new_seat_map


def get_next_seat_state_2(seat_map):
    new_seat_map = []
    for row in seat_map:
        new_seat_map.append(row)

    row_max = len(seat_map)
    col_max = len(seat_map[0])

    for i in range(0, row_max):
        for j in range(0, col_max):
            #print('Start: ('+str(i) + ', ' + str(j) + ')')
            cur_seat = seat_map[i][j]
            if cur_seat != '.':

                search_count = search_seat(i, j, -1, -1, seat_map) \
                                + search_seat(i, j, -1, 0, seat_map) \
                                + search_seat(i, j, -1, 1, seat_map) \
                                + search_seat(i, j, 0, -1, seat_map) \
                                + search_seat(i, j, 0, 1, seat_map) \
                                + search_seat(i, j, 1, -1, seat_map) \
                                + search_seat(i, j, 1, 0, seat_map) \
                                + search_seat(i, j, 1, 1, seat_map)

                if cur_seat == 'L' and search_count == 0:
                    new_seat_map[i] = new_seat_map[i][0:j] + '#' + new_seat_map[i][j+1:]
                elif cur_seat == '#' and search_count >= 5:
                    new_seat_map[i] = new_seat_map[i][0:j] + 'L' + new_seat_map[i][j+1:]

    return new_seat_map


def search_seat(x,y, dx, dy, seat_map):
    x += dx
    y += dy

    while(x >= 0 and x < len(seat_map) and y >= 0 and y < len(seat_map[0])):
        if seat_map[x][y] == '#':
            return 1
        if seat_map[x][y] == 'L':
            return 0

        x += dx
        y += dy

    return 0


#Day 12 Helper
def move_ship(ship_state, instruction, val):

    #print(ship_state)
    #print('   ' + instruction + str(val))
    sign = 1

    if instruction == 'S' or instruction == 'W' or instruction == 'R':
        sign = -1

    if instruction == 'E' or instruction == 'W':
        ship_state[0] = ship_state[0] + val*sign

    elif instruction == 'N' or instruction == 'S':
        ship_state[1] = ship_state[1] + val*sign

    elif instruction == 'L' or instruction == 'R':
        ship_state[2] = (ship_state[2] + val*sign) % 360

    elif instruction == 'F':
        angle = math.radians(ship_state[2])
        ship_state[0] = round(ship_state[0] + val*math.cos(angle))
        ship_state[1] = round(ship_state[1] + val*math.sin(angle))

    return ship_state


def move_ship_2(ship_state, waypoint_state, instruction, val):
    sign = 1

    if instruction == 'S' or instruction == 'W' or instruction == 'R':
        sign = -1

    if instruction == 'E' or instruction == 'W':
        waypoint_state[0] = waypoint_state[0] + val*sign

    elif instruction == 'N' or instruction == 'S':
        waypoint_state[1] = waypoint_state[1] + val*sign

    elif instruction == 'L' or instruction == 'R':
        diff = [waypoint_state[0] - ship_state[0], waypoint_state[1] - ship_state[1]]

        r = math.sqrt(diff[0]*diff[0] + diff[1]*diff[1])
        cur_angle = math.atan2(diff[1], diff[0])
        new_angle = cur_angle + math.radians(val*sign)

        waypoint_state[0] = ship_state[0] + r*math.cos(new_angle)
        waypoint_state[1] = ship_state[1] + r * math.sin(new_angle)

    elif instruction == 'F':
        diff = [waypoint_state[0] - ship_state[0], waypoint_state[1] - ship_state[1]]

        for i in range(0, val):
            ship_state[0] += diff[0]
            ship_state[1] += diff[1]

        waypoint_state[0] = ship_state[0] + diff[0]
        waypoint_state[1] = ship_state[1] + diff[1]

    return ship_state


#Day 13 Helper
def is_multiple(a, b):
    #Is a multiple of b?

    return a % b == 0


#Day 14 Helper
def parse_mem_instructions(instr_list_batch):
    instr_list = []

    for i in range(0, len(instr_list_batch)):
        tokens = instr_list_batch[i].strip().split('=')

        instr = ''
        val = ''

        if tokens[0][:3] == 'mas':
            instr = 'mask'
            val = str(tokens[1].strip(' '))
        elif tokens[0][:3] == 'mem':
            instr = 'mem'

            addr = int(tokens[0][4:len(tokens[0])-2])
            val = [addr, int(tokens[1])]

        instr_dict = {instr: val}

        instr_list.append(instr_dict)

    return instr_list


def parse_instr(instr_full, mem, mask):
    [(instr, v)] = instr_full.items()

    if instr == 'mask':
        mask = instr_full['mask']
    elif instr == 'mem':
        addr = instr_full['mem'][0]
        val = instr_full['mem'][1]

        mem[addr] = apply_mask(mask, val)

    #print(mem)
    return mem, mask


def parse_instr_2(instr_full, mem, mask):
    [(instr, v)] = instr_full.items()

    if instr == 'mask':
        mask = instr_full['mask']
    elif instr == 'mem':
        addr = instr_full['mem'][0]
        val = int(instr_full['mem'][1])

        addr_masked = apply_mask_2(mask, addr)
        num_X = addr_masked.count('X')

        mem_list = [0] * int(math.pow(2, num_X))

        for i in range(0, len(mem_list)):
            cur_bin_combo = format(i, '0' + str(num_X) + 'b')
            mem_list[i] = replace_X_with_bin(addr_masked, cur_bin_combo)

        for addr in mem_list:
            mem[addr] = val

    #print(mem)
    return mem, mask


def apply_mask(mask, val):
    mask_bin = '0b'
    val_bin = format(val, '#038b')

    for i in range(0, len(mask)):
        if mask[i] == 'X':
            mask_bin += '0'
        elif mask[i] == '0':
            mask_bin += str(val_bin[i+2])
        elif mask[i] == '1':
            if(val_bin[i+2] == '0'):
                mask_bin += '1'
            else:
                mask_bin += '0'

    mask_int = int(mask_bin, 2)
    val_int = int(val_bin, 2)

    return mask_int ^ val_int


def apply_mask_2(mask, val):
    val_bin = format(val, '036b')
    final_val_str = ''

    for i in range(0, len(mask)):
        if mask[i] == 'X':
            final_val_str += 'X'
        elif mask[i] == '1':
            final_val_str += '1'
        elif mask[i] == '0':
            final_val_str += str(val_bin[i])

    #print(mask, val, val_bin, final_val_str)
    return final_val_str


def replace_X_with_bin(addr_masked, bin_combo):
    X_id = 0
    new_addr = addr_masked

    for i in range(0, len(addr_masked)):
        if addr_masked[i] == 'X':
            new_addr = new_addr[:i] + str(bin_combo[X_id]) + addr_masked[i+1:]
            X_id += 1

    return int(new_addr, 2)