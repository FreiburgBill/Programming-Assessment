# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:47:39 2021

@author: worth

"""


import ProgAssement
import sys

def run_examples():
    """
    Prints out all of the examples that 
    were given in the Programming Assement 
    by calling the functions that were created.

    Returns
    -------
    None.

    """
    print ('Python Version:' + sys.version)
    print()
    print("\t\t Programming Assessment Examples")
    SECTION_BREAK = '*************************************************************'
    pa = ProgAssement.ProgAssement()
    print(SECTION_BREAK)
    print()
    print('PART 1')
    print('print_grid(1)')   
    pa.print_grid(1)
    print()
       
    print('print_grid(2)')   
    pa.print_grid(2)
    print()
    
    print('print_grid(3)')  
    pa.print_grid(3)
    print()
    
    print(SECTION_BREAK)
    print()
    print('PART 2')   
    print('g = new_grid(5)')
    print('print_grid(g)')
    g = pa.new_grid(5)
    print(g)
    print()

    print('delete_v(g, 2, 3)')
    pa.delete_v(g, 2, 3)
    print()
    
    print('delete_h(g, 4, 3)')
    pa.delete_h(g, 4, 3)
    print()
    
    print(SECTION_BREAK)
    print()
    print('Part 3 (bonus):')
    print('WARNING: ALPHA VERSION HAS AN ACCURACY OF APROX. 50%')
    
    print('path_exists(g, 5, 1, 5, 2) → False')
    exists = pa.path_exists(g, 5, 1, 5, 2)
    print(exists)
    print()
    
    print('path_exists(g, 1, 4, 1, 5) → True')
    exists = pa.path_exists(g, 1, 4, 1, 5) 
    print(exists)
    print()
    
    
    print('path_exists(g, 1, 1, 2, 4) → True')
    exists = pa.path_exists(g, 1, 1, 2, 4) 
    print(exists)
    print()
    
    print('path_exists(g, 1, 1, 3, 5) → False')
    exists = pa.path_exists(g, 1, 1, 3, 5) 
    print(exists)
    print()
    
    print(SECTION_BREAK)
    print('\t\t END OF EXAMPLES')
    
run_examples()