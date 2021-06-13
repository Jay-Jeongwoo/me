"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will print "what", "does", "this", "line", "do", "?" in separate lines.
for word in some_words:
    print(word)
# I guess this will make a loop(iteration) since we use 'for'. 
# Therefore, it will print all the componants from ['what' 'does' 'this' 'line' 'do' '?']

for x in some_words:
    print(x)
# This will print exact same result with the upper one.

print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')
# I think this will print 'some_words contatins more than 3 words' since it meet the requirement.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
# I think it will print user interface of my computer.
usefulFunction()
