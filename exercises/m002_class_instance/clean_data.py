from typing import List
import os 

from config import FILE_PATH


 
def convert_string_to_list(one_line: str , seperate_by: str = None) ->List[str]: 
    """
    Chuyển dòng từ file text thành 1 list của string.
    Example:
    Input:
    one_line = 'FP001,Gao thom ST25,18000,120' , seperate_by = ','
    Output:
    ['FP001','Gao thom ST25','18000','120']

    
    """
    
    
    # clean_row = []
    # name = ""
    # for element in one_line:
    #     if element.isnumeric():
    #         clean_row.append(int(element))
    #     else:
    #         name = name + " "  + element
            
    # name = name.strip()
    # clean_row.insert(1, name)
    # return clean_row
    return [x.strip() for x in one_row.split(seperate_by)]


if __name__ == '__main__':
    # convert_string_to_list(FILE_PATH)
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,'r') as f :
            data_rows = f.readlines()
        one_row = data_rows[2]
        print(convert_string_to_list(one_row,','))
        clean_list = []
        for i in data_rows:
            if i
            print(i)     
        # print(one_row)
        # loop through each row and turn it into a list of string.  
        
    else: 
        print("file dont exist")