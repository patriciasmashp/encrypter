import numpy as np
from math import ceil, floor, sqrt



config = {
    'size':{
        'height': 10,
        'width': 13,
        'tail' : 4
        },
    'idents': 2,
    'transfers': 2
    }
    

text = "VLADIMIR_KOTELNIKOV,_SOVIET_SCIENTIST,_INVENTED_THE_UNIQUE_SECRET_EQUIPMENT_SOBOL-P._IT_WAS_NOT_DECRYPTED_DURING_THE_SECOND_WORLD_WAR"

def encrypt_square(text, config):

    square = np.empty((config['size']['height'],config['size']['width']),dtype=str)
    square = np.append(square, np.empty(4,dtype=str),1)

    for row in square:
        _start_row = text[0: ceil((config['size']['width'] - config['transfers'])/(config['idents']))]
        text = text[len(_start_row)::]
        _start_slice = slice(0,config['size']['width'] - config['transfers'],config['idents'])
        row[_start_slice] = list(_start_row)
    
    for row in square:
        _start_row = text[0:len(row[np.where(row=='')])]
        text = text[len(_start_row)::]
        _start_row = _start_row.ljust(len(row[np.where(row=='')]), ' ')
            
        row[np.where(row=='')] = list(_start_row)
    print(square)
    return square
# encrypt(text, config)

def encrypt(text, config):
    q_symb = len(text)
    square = []
    for num_row in range(0,config['size']['height']):
        row = np.empty(config['size']['width'],dtype=str)
        square.append(row)
    square.append(np.empty(config['size']['tail'],dtype=str))
    
    
    for row in square:
        if len(row)<config['size']['width']:
            _start_row = text[0: ceil((len(row)/config['idents']))]
            _start_slice = slice(0,len(row) ,config['idents'])
        else:
            _start_row = text[0: ceil((len(row) - config['transfers'])/(config['idents']))]
            _start_slice = slice(0,len(row) - config['transfers'],config['idents'])
        text = text[len(_start_row)::]
       
        row[_start_slice] = list(_start_row)
    
    for row in square:
        _start_row = text[0:len(row[np.where(row=='')])]
        text = text[len(_start_row)::]
        _start_row = _start_row.ljust(len(row[np.where(row=='')]), ' ')
            
        row[np.where(row=='')] = list(_start_row)
    return square
    
    

