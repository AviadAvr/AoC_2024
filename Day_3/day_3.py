import os
import re

base_path = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(base_path, "../Day_3/day_3.txt")

with open(file_path) as f:
    input_str = f.read()


def part1(input_str):

    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", input_str)
    
    total = 0
    for mul in muls:
        nums = re.findall("\d{1,3}", mul)
        total += int(nums[0]) * int(nums[1])
        
    return total

def part2(input_str):

    do_ends_indices = [i.start(0) for i in re.finditer("do\(\)", input_str)]    
    dont_end_indices = [i.start(0) for i in re.finditer("don't\(\)", input_str)]
        
    muls = re.finditer("mul\(\d{1,3},\d{1,3}\)", input_str)
    
    mul_indices = []
    mul_dic = {}
    for mul in muls:
        mul_indices.append(mul.start())
        mul_dic[mul.start()] = mul.group()
    
    all_indices = do_ends_indices + dont_end_indices + mul_indices
    all_indices.sort()
    
    total = 0
    do = True
    do_nums = []
    for i in all_indices:
        if i in do_ends_indices:
            do = True
        elif i in dont_end_indices:
            do = False
            
        if i in mul_dic:
            if do:
                nums = re.findall("\d{1,3}", mul_dic[i])
                do_nums.append(nums)
                total += int(nums[0]) * int(nums[1])
            
    return total