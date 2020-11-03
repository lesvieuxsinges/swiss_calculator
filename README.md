# swiss_calculator

This tool consists in an program used to solve sign table for any function in its factorial form

Use:
  Start the newsigntable.py file and enjoy!

  Input:
  
    (first degree factor)(other first degree facotr)etc...
    
  Output:
  
    x           -∞             factor      factor             +∞           
    factor                  -     0     +     |     +   
    factor                  -     |     -     0     +   
    product                 +     0     -     0     +   

Example:
  Input:

    (-x+4)(2x+4x-2+4)(-3x+6)

  Output:

    x               -∞                 -1/3         6/3          4                   +∞              
    2x+4x-2+4                      -     0     +     |     +     |     +   
    -3x+6                          +     |     +     0     -     |     -   
    -x+4                           +     |     +     |     +     0     -   
    (-x+4)(2x+4x-2+4)(-3x+6)       -     0     +     0     -     0     +   


Details about how this works:
  There are 6 files:
  
    cut.py: it takes in input a string, and returns a list
    
    eqsolve.py: takes in input a string (passes by cut.py), and returns a tuple
    
    fraction.py: creates a class for fraction type, and all operations associated
    
    functions.py & libs.py: both defines functions that are pretty useful (not every functions are used here) (for a future version, we'll merge those files together)
    
    newsigntable.py: uses all those files, it takes in input a string, and returns a list of strings, printed in command line, and that is the sign table!
    
  Schema in working...
  
  This was created by Gaetan and Louis, contactable at Gaëtan#3104 and Raincod#5016
