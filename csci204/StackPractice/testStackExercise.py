from StackExercise import *

mah_stack = Stack()
print(mah_stack.is_empty())
mah_stack.push(1)
print(mah_stack.peek())
print(mah_stack.pop())
[mah_stack.push(x) for x in range(10)]
print(len(mah_stack))
