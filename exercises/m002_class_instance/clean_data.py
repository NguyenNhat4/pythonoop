from typing import List

FILE_PATH = 


 
def convert_string_to_list(one_line: str ) ->List[str]: 
    """
    
    
    """
    
    one_line = one_line.split()
    clean_row = []
    name = ""
    for element in one_line:
        if element.isnumeric():
            clean_row.append(int(element))
        else:
            name = name + " "  + element
            
    name = name.strip()
    clean_row.insert(1, name)
    return clean_row



if __name__ == '__main__':
    convert_string_to_list(FILE_PATH)
    
    