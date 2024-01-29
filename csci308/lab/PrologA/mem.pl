
mem(X, [LastMem]) :- X == LastMem.
mem(X, [FirstMem | _]) :- X == FirstMem.
mem(X, [_ | TheRest]) :- mem(X, TheRest).