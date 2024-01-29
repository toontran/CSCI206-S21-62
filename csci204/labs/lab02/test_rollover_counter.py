from counter import *

print('Testing RollOverCounter...')
my_count = RollOverCounter(10, 12)

print('Its min value should be 10 ... It is ' + str(my_count.get_min()))
print('The count value should be at minimum ... ' + str(my_count.is_at_min()))
print('The count value should not be at maximum ... ' + str(my_count.is_at_max()))

my_count.count()
my_count.count()
print('Increment twice, the count value should be 12 now ... ' + str(my_count.get_count_value()))

print('The count value should be at maximum ... ' + str(my_count.is_at_max()))
print('The count value should not be at minimum ... ' + str(my_count.is_at_min()))

my_count.count()
print('Increment one more time, the count value should rollover to 10 ... ' + str(my_count.get_count_value()))

my_count.un_count()
print('Decrement three times, the cout value should rollover to 12 ... ' + str(my_count.get_count_value()))
