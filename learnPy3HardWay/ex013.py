from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

run_cmd = '''
python3.7 ex013.py first 2nd 3rd
'''

out_put = '''
The script is called: ex013.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
'''
