import os

base_path = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(base_path, "../Day_2/day_2.txt")

with open(file_path) as f:
    lines = f.readlines()
    

def line_test(line):
    line_ok = False
    
    forward_check = all(0 < int(line[i]) - int(line[i+1]) < 4 for i in range(len(line) - 1))
    reverse_check = all(0 < int(line[i]) - int(line[i-1]) < 4 for i in range(len(line) - 1, 0, -1))
    
    if forward_check or reverse_check:
        line_ok = True
    
    return line_ok


def part1(lines):
    safe_lines = 0
    for ln in lines:
        line = ln.split(' ')
    
        if line_test(line):
            safe_lines += 1
            
    return safe_lines


def part2(lines):
    safe_lines = 0
    for ln in lines:
        line = ln.split(' ')
        
        if line_test(line):
            safe_lines +=1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]
                if line_test(new_line):
                    safe_lines += 1
                    break
                
    return safe_lines