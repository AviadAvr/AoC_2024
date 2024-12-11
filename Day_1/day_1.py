import os

base_path = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(base_path, "../Day_1/day_1.txt")

with open(file_path) as f:
    lines = f.readlines()
    
ls1 = []
ls2 = []

for ln in lines:
    line = ln.split("   ")
    ls1.append(int(line[0]))
    ls2.append(int(line[1]))
    
ls1.sort()
ls2.sort()
    
def part1(ls1, ls2):
        
    diffs=0
    
    for i in range(len(lines)):
        diffs += abs(ls1[i] - ls2[i])
        
    return diffs

def part2(ls1, ls2):
    
    total = 0
    
    for i in range(len(lines)):
        left_num = ls1[i]
        right_count = ls2.count(left_num)
        total += left_num * right_count
        
    return total