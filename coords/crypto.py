import re
import numpy as np

def algo(config, text):
    def encrypt(coords_array):
        c_coord_array = []
        for  coord in coords_array:
            coord = coord.replace('.','')
            square = np.empty(len(coord), dtype=str)

            sl = slice(0,len(coord), config['idents']) 
            square[sl] = list(coord[0:len(square[sl])])
            coord = coord[len(square[sl])::]
            square[np.where(square=='')] = list(coord)
            if config['regex'] == r'\d\d.\d\d\d\d':
                coord = ''.join(square[:2]) + '.' + ''.join(square[2:])
            else:
                coord = ''.join(square)
            c_coord_array.append(coord)

        return c_coord_array
    
    coords_array = re.findall(config['regex'], text, re.MULTILINE)

    for n, coord in enumerate(encrypt(coords_array)):
        text = text.replace(coords_array[n], coord)

    
    return text

