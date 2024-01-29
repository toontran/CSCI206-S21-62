
numberOfLeaves(leaf(_), N) :- N is 1.
numberOfLeaves(node(T1, T2), N) :- numberOfLeaves(T1, N1), numberOfLeaves(T2, N2), N is N1 + N2. 

%position(leaf(V), L, N) :- leaf(V) == L, N is 1.
position(leaf(L), L, N) :- N is 1.
% position(leaf(M), L, N) :- M \= L, N is 0.
position(node(T1, _), L, N) :- position(T1, L, N).
position(node(T1, T2), L, N) :- numberOfLeaves(T1, N1), position(T2, L, N2), N is N2 + N1. 

