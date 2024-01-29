
% Infer type of value
equiv(Type1, Type2) :- write('EQUIV '), write(Type1), write(' '), write(Type2), write('? '), Type1==Type2, write('YES').


