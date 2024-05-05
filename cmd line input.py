import sys
print(f"Script Name: {sys.argv[0]}")
arguments = sys.argv[1:]
num_arguments = len(arguments)
print(f"Number of Arguments: {len(arguments)}")
for arg in arguments:
    print(f"Argument: {arg}")
