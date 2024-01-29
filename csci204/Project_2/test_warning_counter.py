from counter import *


def readLimit(prompt):

    v = 0
    while True:
        try:
            v = int(input(prompt))
            if v < LimitedCounter.DEFAULT_MIN:
                raise ValueTooSmallError
            elif v > LimitedCounter.DEFAULT_MAX:
                raise ValueTooLargeError
            break
        except ValueError:
            print('Number error, try again!')
        except ValueTooSmallError:
            print("This value is too small, try again!")
            print()
        except ValueTooLargeError:
            print("This value is too large, try again!")
            print()
    return v

print('Testing WarningCounter...')
my_count = WarningCounter(10, 12)

print('Its min value should be 10 ... It is ' + str(my_count.get_min()))
print('The count value should be at minimum ... ' + str(my_count.is_at_min()))
print('The count value should not be at maximum ... ' + str(my_count.is_at_max()))

my_count.count()
my_count.count()
print('Increment twice, the count value should be 12 now ... ' + str(my_count.get_count_value()))

print('The count value should be at maximum ... ' + str(my_count.is_at_max()))
print('The count value should not be at minimum ... ' + str(my_count.is_at_min()))

'''
print('Increment one more time, result in exception ... ')
my_count.count()
'''

my_count.un_count()
my_count.un_count()
print('The count value should be at minimum ... ' + str(my_count.is_at_min()))
print('The count value should not be at maximum ... ' + str(my_count.is_at_max()))

'''
print('Decrement one more time, result in exception ... ')
my_count.un_count()
'''

lo = LimitedCounter.DEFAULT_MIN
hi = LimitedCounter.DEFAULT_MAX
while True:
    try:
        lo = readLimit('Enter minimum: ')
        hi = readLimit('Enter maximum: ')
        if lo >= hi:
            raise ValueIncorrectError
        break
    except ValueIncorrectError:
        print('The values of ' + str(lo) + ' and ' + str(hi) + ' are wrong.')

print('lo ' + str(lo) + ' hi ' + str(hi))


