"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

import os

with open(f"{os.getcwd()}/src/foo.txt", "r") as f:
    content = f.read()
    print(content)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open(f"{os.getcwd()}/src/bar.txt", "w") as f:
    f.write('Hello python\n')
    f.write('Lets build amazing things together\n')
    f.write('You are simple yet powerful\n')

# Open up and read the contents of bar.txt
with open(f"{os.getcwd()}/src/bar.txt", "r") as f:
    content = f.read()
    print("The contents of bar.txt is:\n", content)
