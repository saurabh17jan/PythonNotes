print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


print("How old are you?")
age1 = int(input())
print("How tall are you?")
height1 = input()
print("How much do you weigh?")
weight1 = input()

print(f"So, you're {age1} old, {height1} tall and {weight1} heavy.")

output = '''
--------------------------------------------------------------------------------
How old are you? 30
How tall are you? 182
How much do you weigh? 79
So, you're 30 old, 182 tall and 79 heavy.
How old are you?
31
How tall are you?
182
How much do you weigh?
77
So, you're 31 old, 182 tall and 77 heavy.
--------------------------------------------------------------------------------
'''

v_warning = '''
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Warning!

We put an end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
