def sorting(inp, start):
    sorted_dict = {} # Big sorted dict of patterns by start location
    for loc in start: # For every start location
        f = open(inp, "r+")
        print(loc) 
        patterns = [] # List of patterns for for start location
        for line in f: 
            if list(line)[0] == loc: # If line starts at [start location]
                patterns.append(line)
        patterns = sorted(patterns, key=len) # Sort by size
        sorted_dict[loc] = patterns 
    return sorted_dict

def dict_processing(inp, start):
    w = open("output", "a+")
    sorted_dict = sorting(inp, start)
    big_list = [] # Huge list of patterns
    for key in sorted_dict: 
        for item in sorted_dict[key]:
            big_list.append(item)
    list_len_sort = sorted(big_list, key=len) # Sort by length
    for pattern in list_len_sort:
        w.write(pattern)

# Start locations in order of most to least frequent
# 1, 3 and 7 constitutes 73% of patterns
# 44% of patterns start at 1
start = ['1', '3', '7', '2', '4', '5', '9', '7', '6']
dict_processing("full_pattern_list.txt", start)
