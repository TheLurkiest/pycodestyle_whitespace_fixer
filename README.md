# pycodestyle_whitespace_fixer


For right now the python code module we're adding will just function like a way to add spaces around +-*= signs.

However, for the time being this will only work properly if you commit to NOT using pycodestyle in this manner;
if you normally put in spaces anyway then there will be TWO spaces around these arithmetic operators instead of
just one.  I am working on a fix for this-- but for the time being you'll only find this worth while if you DONT use
pycodestyle.


Running this module is just a matter of entering this into the terminal:

sudo python final_space_adder.py




...You'll need to plug in the values you want to use for input and output.  The default input and ouput are:

in_file2.py is the input (the final that you want to add whitespace to according to pycodestyle conventions)

...and out_file3.txt is the output (where you can see what changes have been made to conform to pycodestyle conventions)

