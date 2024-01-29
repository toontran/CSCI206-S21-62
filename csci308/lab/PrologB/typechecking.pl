/* An attempt to implement the typechecking with overloading in Prolog */
%%%%%%% THE JAVA PROGRAM %%%%%%%%%%%%%%%%%%%%

/*
A Java program

public int foo(int w) { ... } 
public int bar(double r) { ... } 
public int bar(string r) { ... } 
public String qux(int x, double y) { ... } 
public void check() { 
    int a = 42; 
    double b = 3.14159; 
    double c; 
    String d; 
}
*/

% the variables
var(a, int).   % a : int 
var(b, dbl).   % b : double 
var(c, dbl).   % c : double 
var(d, str).   % d : string 

% The functions 
fun(foo, [int, int]).        % foo : int -> int
fun(bar, [dbl, int]).        % bar : double -> int 
fun(bar, [str, int]).        % bar : string -> int 
fun(qux, [int, dbl, str]).   % qux : int -> double -> string


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% TYPE COERSION %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%% PROBLEM: IMPLICIT COERSION
% implicit coercions from first type to second type 
implicitCoersion(int, dbl). % int can implicitly coerce to double
implicitCoersion(dbl,str).
implicitCoersion(int,str).

%%%%%%%%%%%%% PROBLEM: PRINT ABOUT COERSION
% Coerce from type to type
 coerce(FromType, ToType) :- write('    COERCE from '), write(FromType), write(' to '),
     write(ToType), write('?'), % Print about the coercion attempt. 
     implicitCoersion(FromType, ToType),      % Try to coerce the types.
     write(' Yes\n').                    % This only prints if coercion succeeds. 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% TYPE EQUIVALENCE %%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%% PROBLEM: THE EQUIV STEP WHEN THE TYPES ARE THE SAME
% Equiv types T1 and T2 directly 
equiv(T1,T2):- write('  EQUIV '), write(T1), write(' and '), write(T2), write('?'),
    T1 == T2, write(' Yes\n').

%%%%%%%%%%%%% PROBLEM: THE EQUIV STEP WHEN THE TYPES CAN BE COERCED
% Equiv types T1 and T2 via coersion 
equiv(T1,T2):- not(T1 == T2), write(' No\n'), coerce(T1,T2).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% TYPE INFERENCE %%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%% PROBLEM: THE INFER STEP FOR VALUES
% Infer the type of a value 
infer(X, Type) :- integer(X), Type = int, write('INFER '),write(X),write(' : '),write(Type), write('\n').
infer(X, Type) :- float(X), Type = dbl, write('INFER '),write(X),write(' : '),write(Type), write('\n').
infer(X, Type) :- string(X), Type = str, write('INFER '),write(X),write(' : '),write(Type), write('\n').

%%%%%%%%%%%%% PROBLEM: THE INFER STEP FOR VARIABLES
% Infer the type of a declared variable 
infer(X, Type) :- var(X,Type), write('INFER '),write(X),write(' : '),write(Type), write('\n').

% Infer the return type of a function call on one argument 
infer(call_1(FunctionName, Arg), ReturnType) :- 
    check(call_1(FunctionName, Arg), ReturnType),
    write('INFER '), write(FunctionName), write(' returns '), write(ReturnType), write('\n'). 

% Infer the return type of a function call on two arguments 
infer(call_2(FunctionName, Arg1, Arg2), ReturnType) :- 
    check(call_2(FunctionName, Arg1, Arg2), ReturnType),
    write('INFER '), write(FunctionName), write(' returns '),   
    write(ReturnType), write('\n'). 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% TYPE CHECK %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% if we find a function candidate, try it
try(FunName,FunType):- fun(FunName,FunType), 
    write('\nCHECK '), write(FunName), write(' : '), write(FunType), write('\n').

% Infer the return type of a function call with one argument
check(call_1(FunctionName, Arg), ReturnType) :-
  infer(Arg,TypeOfArg),            % infer type of argument
  try(FunctionName,TypeOfFunction),  % find a function to check
  TypeOfFunction = [TypeOfParam, FunctionsReturn],
  equiv(TypeOfArg, TypeOfParam),   % equiv arg and param types
  FunctionsReturn = ReturnType.   % if that all suceeded, keep the return type

%%%%%%%%%%%%% PROBLEM: THE ADD FUNCTIONS
% The collection of built-in functions 
fun(add, [int, int,int] ). % you fill in the … with the correct list of types
fun(add, [dbl,dbl,dbl] ).
fun(add, [str,str,str] ).

%%%%%%%%%%%%% PROBLEM: CHECKING FUNCTIONS WITH 2 PARAMETERS
check(call_2(FunctionName, Arg1, Arg2), ReturnType) :- 
  infer(Arg1,TypeOfArg1),            % infer type of argument
  infer(Arg2,TypeOfArg2),            % infer type of argument
  try(FunctionName,TypeOfFunction),  % find a function to check
  TypeOfFunction = [TypeOfParam1, TypeOfParam2, FunctionsReturn],
  equiv(TypeOfArg1, TypeOfParam1),   % equiv arg and param types
  equiv(TypeOfArg2, TypeOfParam2),
  FunctionsReturn = ReturnType. 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% ASSIGNMENT STATEMENTS %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%% PROBLEM: ASSIGNMENT STATEMENTS
% typecheck assignment statement: left = right;
typecheck(assign(Left,Right)) :- infer(Right,TR),
  infer(Left,TL), equiv(TR,TL).