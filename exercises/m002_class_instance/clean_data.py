from typing import List
import os 



FILE_PATH : str = '' 


 
def convert_string_to_list(one_line: str , seperate_by: str = None) ->List[str]: 
    pass
#     """
    
    
#     """
    
#     one_line = one_line.split()
#     clean_row = []
#     name = ""
#     for element in one_line:
#         if element.isnumeric():
#             clean_row.append(int(element))
#         else:
#             name = name + " "  + element
            
#     name = name.strip()
#     clean_row.insert(1, name)
#     return clean_row



if __name__ == '__main__':
    # convert_string_to_list(FILE_PATH)
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,r) as f :
            data_rows = 
            
        # loop through each row and turn it into a list of string.  
        
    else: 
        print("file dont exist")