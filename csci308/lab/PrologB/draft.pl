% color facts go here
color(red).
color(blue).
color(green).
color(yellow).

% coloring(L) goes here
coloring([]).
coloring([[A, B]|Tail]) :- color(A), color(B), coloring(Tail).  

% queries so you can cut/paste to test them instead of typing them in
% coloring( [ [Switz, France], [Switz, Italy], [Switz, Germany], [Switz, Austria], [Germany, France], [Germany, Austria], [France, Italy] ]).
% coloring( [ [Penn,Maryland], [Penn, Delaware], [Penn, NewJersey], [Penn, NewYork], [Penn, Ohio], [Penn, WestVirginia], [Ohio, WestVirginia], [WestVirginia, Maryland], [Maryland, Delaware], [Delaware, NewJersey], [NewJersey, NewYork], [Virginia, WestVirginia], [Virginia, Maryland], [Virginia, Kentucky], [Kentucky, Ohio], [Kentucky, Indiana], [Indiana, Ohio] ]).
