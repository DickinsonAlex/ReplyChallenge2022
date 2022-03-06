import functions as funcs
from typing import List
import re

    
# def format_output(data: {type}) -> List[str]:
#     output_list = []
#     for i, num in enumerate(data):
#         line_output = f"Case #{i + 1}: {num}"
#         output_list.append(line_output)
        
#     return output_list

def main():
    folder_name = "{name}"
    input_path = funcs.get_input_path(folder_name)
    lines = funcs.get_file(input_path)
    output = []

    
    for _ in range(int(lines.pop(0))):
        pass # Code goes here
    
    
       
    
    
    
    
    result = re.search(f"input-{folder_name}-(.*).txt",input_path)
    output_path = result.group(1)
    
    funcs.write_file(f"{folder_name}\outputs\output-{output_path}.txt", format_output(output))

if __name__ == '__main__':
    main()