""" CSCI204 Stack lab
Last Modified by: Prof. Dancy, Mar-2017
"""
from stack import MyStack

stack = MyStack()

class IllegalExpressionException( BaseException ):
    pass
    
class ParensMismatchException( BaseException ):
    pass

def translate( expression ):
    """ Translates the given simple infix arithmetic expression to postfix
        notation. Returns the result as a string.

        Examine each number and operator in the input.
            If it’s a number, add it to the output.
            Else if its an operator, handle it
            Else it was an error
        Empty the stack onto the output
    """
    output = ""
    empty_stack()
    found_operator = False
    is_in_paren = False
    lack_right_paren = 0

    for ch in expression:
        if is_number( ch ) and not found_operator:
            output = output + ch
        elif is_number( ch ) and found_operator:
            output = output + ' ' + ch
            found_operator = False
        elif is_operator( ch ):
            found_operator = True
            output = output + handle_operator( ch, is_in_paren )
            is_in_paren = False
        elif ch == '(':
            stack.push( '(' )
            is_in_paren = True
            lack_right_paren += 1
        elif ch == ')':
            output = output + handle_right_paren()
            lack_right_paren -= 1
        else:
            print(expression)
            raise IllegalExpressionException()
            
    if lack_right_paren != 0:
        raise ParensMismatchException
        
    output = output + empty_stack()
    print(output)
    output = evaluateExpression( output )
    return output
    
def evaluateExpression( postfix ):
    if len(postfix) == 1:
        return postfix

    temp = ''
    for ch in postfix:
        #print(ch, temp)
        if ch == ' ' and temp != '':
            stack.push(temp)
            temp = ''
        elif ch == ' ':
            continue
        elif is_number( ch ):
            temp += ch
        else:
            result = 0                
            right_op = stack.pop()
            left_op = stack.pop()
            if ch == '+':
                result = int(left_op) + int(right_op)
            elif ch == '-':
                result = int(left_op) - int(right_op)
            elif ch == '*':
                result = int(left_op) * int(right_op)
            elif ch == '/':
                result = int(left_op) / int(right_op)
            stack.push(result)
            
    return str(stack.pop())

def empty_stack():
    """ Empties the stack while collecting each element as it is removed.
        Returns the collected elements. """
    elements = ""
    while not stack.is_empty():
        elements += ' ' + stack.pop()
    return elements

def is_number( ch ):
    """ Is the given character a number? """
    return (ch >= '0' and ch <= '9')

def is_operator( ch ):
    """ Is the given character an operator? """
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'

def handle_operator( operator, is_in_paren ):
    """ Pops all operators of the same or greater precedence as the given
	operator from the stack and then pushes the given operator. """
    elements = pop_higher_precedence_ops( operator, is_in_paren )
    stack.push( operator )
    return elements
    
def handle_right_paren():
    elements = ''
    while stack.top() != '(':
        if len(stack) == 0:
            raise ParensMismatchException()
        elements += ' ' + stack.pop()
    stack.pop() # The '('
    return elements

def pop_higher_precedence_ops( operator, is_in_paren ):
    """ Pops operators that have precedence >= the given operator. """
    elements = ""
    while (not stack.is_empty()) and is_top_higher_precedence( operator ) and \
          (not is_in_paren):
        elements += ' ' + stack.pop()
    return elements

def is_top_higher_precedence( operator ):
    """ Does the operator on the stack top have precedence >= to the
        given operator?

        Convert operators into levels of precedence.
        Lower levels indicate lower precedence.
        Additive operators (+ -) are level 0.
        Multiplicative operators (* /) are level 1.
        Then compare the level
    """
    top = stack.top()
    
    if top == '(':
        return False

    if operator == '+' or operator == '-':
        op_level = 0
    else:
        op_level = 1

    if top == '+' or top == '-':
        top_level = 0
    else:
        top_level = 1

    return top_level >= op_level


def main():
    print( "Hit Enter to end this program." )
    infix = input( "Enter a simple arithmetic expression: " )
    while not infix == "":
        postfix = translate( infix )
        print( infix + " ==> " + postfix )
        infix = input( "Enter a simple arithmetic expression: " )

main()
