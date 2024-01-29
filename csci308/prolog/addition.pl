
% Infer type of value
add(Value1, Value2, Answer) :- integer(Value1), Answer is Value1+Value2.
add(Value1, Value2, Answer) :- float(Value1), Answer is Value1+Value2.
add(Value1, Value2, Answer) :- string(Value1), string_concat(Value1,Value2,Answer).


