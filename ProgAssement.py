# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:43:16 2021

@author: worth

You have 60 minutes to complete the exercise below. At the end of the allotted
 time, please return your code and answers via email attachment or
 GitHub/GitLab/Bitbucket link. The focus for your code should be on its
 clarity which can be accomplished via formatting, comments, and docstrings
 where appropriate. Partial solutions and solution ideas will be accepted.
 Please note that this is not the only metric that matters during the
 assessment process. Try to have fun!
You may complete the exercises in the programming language of your choice;
 the recommendation is to pick the one you are most comfortable with.
 
 @HISTORY:
   20.May.2021 - First version, was not completed in the allocated time of 1 hour
   27.May.2022 - Second version, functions are now functioning 
   
 Use RunExamples() to create the examples given in assignment.  
 
"""

import random

class ProgAssement():
    
    #  Constant declarations:
    SPACE = ' '
    HEADER_ROW_INDENTATION = SPACE*3
    ROW_INDENTATION = SPACE*2
    NUMBER_SPACING =  SPACE*2
    HORIZONTAL_SEPERATOR = '--+'
    VERTICAL_SEPERATOR     = '  |'
    MIN_GRID_SIZE = 1
    MAX_GRID_SIZE = 9
    CRLF = '\n'
    ERROR_MESSAGE = "ERROR: Values must be greater than 0 and less than 10!"
    
    def print_grid(self, n):
        """
        Part 1
        Consider a discrete grid of size 𝑛×𝑛. 
        Write a function print_grid(n) to print a grid of size 𝒏×𝒏.

        if the possed in parameter is not an integer 
        greater than 0 and less than 9, an error message
        will be printed.
        If the passed in parameter is a correct value
        then a nXn size grid will be printed.
        
        Parameters
        ----------
        n : int 
            must be greater than zero and less than ten
            n X n size of grid to print

        Returns
        -------
        none

        """
        # Check that passed in parameter is of correct value
        if (type(n) is not int or n < self.MIN_GRID_SIZE or n > self.MAX_GRID_SIZE) :
            print(self.ERROR_MESSAGE)
        else:    
            # First print the columns numeric values as a header row
            header_row = self.HEADER_ROW_INDENTATION
            header_row += self.NUMBER_SPACING.join([str(item) for item in range(1, n+1) ])  
            print(header_row)
            
            second_row = self.ROW_INDENTATION + '+' + self.HORIZONTAL_SEPERATOR * n
            print(second_row)
            
            # Now print the vertical and horizontal lines for the n rows
            for i in range(1, n + 1):
                vertical_line = str(i) + ' |' + self.VERTICAL_SEPERATOR * n     
                print(vertical_line)  
                   
                horizontal_line = self.ROW_INDENTATION + '+'   +  self.HORIZONTAL_SEPERATOR * n
                print(horizontal_line) 
                
            
        
 ##   ******************************************************************
 ##                  Part 2
 ##    Inside the grid, we may now delete horizontal or vertical borders.
 ##    For this, we implementthree operations as follows.        
 ##   *******************************************************************  
    
    def new_grid(self,n):
        """
        (1) Initialization:

        if the possed in parameter is not an integer 
        greater than 0 and less than 9, an error message
        will be printed.
        If the passed in parameter is a correct value
        then a nXn size grid will be created and 
        returned as a string object.
        
        Parameters
        ----------
        n : int
            must be greater than zero and less than 10
            n X n size of grid to be returned

        Returns
        -------
        a string representation which is initialized
        with a complete grid of size n with all borders present.



        """
        
                # Check that passed in parameter is of correct value
        if (type(n) is not int or n < 1 or n > 9) :
            print(self.ERROR_MESSAGE)
        else:   
            header_row = self.HEADER_ROW_INDENTATION
            header_row += self.NUMBER_SPACING.join([str(item) for item in range(1, n+1) ])  
            second_row = self.ROW_INDENTATION + '+' + self.HORIZONTAL_SEPERATOR * n
            
           
            rows = header_row + self.CRLF + second_row + self.CRLF
            
            for i in range(1, n + 1):
                vertical_line = str(i) + ' |' + self.VERTICAL_SEPERATOR * n     
                horizontal_line = self.ROW_INDENTATION + '+'   +  self.HORIZONTAL_SEPERATOR * n
                rows += vertical_line + self.CRLF + horizontal_line + self.CRLF
            
        return rows

    
        
    def  delete_v (self, g, i, j):
        """
        (2) Vertical:
    
        Parameters
        ----------
        g : grid_type
            a grid that was created with new_grid()
        i : int
            row
        j : int
           column
            
        in grid g, remove border to the right of row i and column j    
    
        Returns
        -------
        a data structure / representation of the modified grid
    
        """
        # split the past in grid string into 
        # a list of individual lines
        myrows = g.splitlines()

        # calculate the desired row position in the list of lines
        rowpos = i *2
        # calculate the desired column positiom
        colpos = 2 + 3*j
        
        # now get the first lines that are not to 
        # to be modified
        firstrows = self.CRLF.join(myrows[0:rowpos])
        
        # for the row being modified creeate a new line by replacing the vertical 
        # seperator with a space 
        newrow = myrows[rowpos][0:colpos] + self.SPACE + myrows[rowpos][colpos+1:] 
        
        # the first unmodified lines, the new modified line
        # and the lines after that can now be joined together and printed.
        print(firstrows +    self.CRLF + newrow  + self.CRLF + self.CRLF.join(myrows[rowpos+1:]))
        
    def delete_h (self, g, i, j):
        """
        (3) Horizontal:
            
         in grid g, remove border below row i and column j   
     
        Parameters
        ----------
        g : grid_type
              a grid that was created with new_grid() 
        i : int
            row
        j : TYPE
            column
     
        Returns
        -------
         a data structure / representation of the modified grid
     
        """

        # split the past in grid string into 
        # a list of individual lines
        myrows = g.splitlines()

        # calculate the desired row position in the list of lines
        rowpos = i *2 + 1
        # calculate the desired column positiom
        colpos = 3 + 2*j
        
        # now get the first lines that are not to 
        # to be modified
        firstrows = self.CRLF.join(myrows[0:rowpos])
        
        # for the row being modified creeate a new line by replacing the vertical 
        # seperator with a space 
        newrow = myrows[rowpos][0:colpos] + self.SPACE*2 + myrows[rowpos][colpos+2:] 
        
        # the first unmodified lines, the new modified line
        # and the lines after that can now be joined together and printed.
        print(firstrows +    self.CRLF + newrow  + self.CRLF + self.CRLF.join(myrows[rowpos+1:]))
        

##     **************************************************************
##            Part 3 Bonus
##     *************************************************************


    def path_exists(self, g, i1, j1, i2, j2):
        """
        
        Implement a function path_exists(g, i1, j1, i2, j2), which for a 
        given pair of (row, column) locations a = (i1, j1), b = (i2, j2) 
        returns whether a path between a and b exists. Some illustrations 
        are shown below. Note the function only needs to return True or False,
        not print the path.
        
        Parameters
        ----------
        g : sting of array to be tested
        i1 : row from first pair
        j1 : column from first pair
        i2 : row from second pair
        j2 : column from second pair

        Returns
        -------
        Returns true if a path between a and b exists, 
        if a path does not exist it returns false.
        
        WARNING: ALPHA VERSION HAS AN ACCURACY OF APROX. 50%

        """
        
        #WARNING: ALPHA VERSION HAS AN ACCURACY OF APROX. 50%
        return bool(random.getrandbits(1))
    

