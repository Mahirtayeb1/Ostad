from sys import argv
script, inp_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
def prnt_a_line(line_count, f):
    print(line_count, f.readline())

curr_file = open(inp_file)
print("============")
print_all(curr_file)
print("============")
rewind(curr_file)
print("lets print 3 lines: ")
curr_line = 1
prnt_a_line(curr_line, curr_file)
curr_line+=1
prnt_a_line(curr_line, curr_file)
curr_line+=1
prnt_a_line(curr_line, curr_file)


