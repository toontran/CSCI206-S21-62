
% Infer type of value
infer(Value, Type) :- integer(Value), write('INFER '), write(Value), write(' : int.'), Type=int.
infer(Value, Type) :- float(Value), write('INFER '), write(Value), write(' : double.'), Type=dbl.
infer(Value, Type) :- string(Value), write('INFER '), write(Value), write(' : string.'), Type=str.


