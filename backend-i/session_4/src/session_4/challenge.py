def read_lines(file_content):

    
    for index, line in enumerate(file_content):
        stripped_line = line.strip()
        if stripped_line:  
            yield index + 1, stripped_line 

file_content = [
    "  Benfica nº1  ",
    "  ",  
    "   Eticalgarve",
    "  ",  
    " Ronaldo é o GOAT GG",
]


for line_number, line in read_lines(file_content):
    print(f"Line {line_number}: {line}")
