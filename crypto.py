import numpy as np
from math import ceil, floor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import os


# config = {
#     'size':{
#         'height': 12,
#         'width': 12
#         },
#     'idents': 2,
#     'transfers': 2
#     }
    

# text = "VLADIMIR_KOTELNIKOV,_SOVIET_SCIENTIST,_INVENTED_THE_UNIQUE_SECRET_EQUIPMENT_SOBOL-P._IT_WAS_NOT_DECRYPTED_DURING_THE_SECOND_WORLD_WAR"

def encrypt(text, config):

    square = np.empty((config['size']['height'],config['size']['width']),dtype=str)

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

    return square
