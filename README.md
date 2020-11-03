# swiss_calculator

This tool consists in an program used to solve sign table for any function in its factorial form

Use:
  Start the signtable.py file and enjoy!

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

