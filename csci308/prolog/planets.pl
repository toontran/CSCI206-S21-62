% In order to run this example:
% swipl
% ['planets'].
% to quit
% ?- halt.

% The sun and Sirius are two stars
star(sun).
star(sirius).

% The following facts describe the orbits relation.
orbits(mercury,sun).
orbits(venus,sun).
orbits(earth,sun).
orbits(mars,sun).
orbits(jupiter,sun).
orbits(saturn,sun).
orbits(uranus,sun).
orbits(neptune,sun).
orbits(moon,earth).
orbits(phobos, mars).
orbits(titan,saturn).
orbits(rhea,saturn).


% The Horn clause describing what is a planet.
planet(B) :- orbits(B,sun).

% The Horn clause describing what is a satellite.
satellite(X):- orbits(X,P), planet(P).

origin(point(X,Y)) :- X = 0, Y = 0.

inside(point(X,Y), R) :- X*X + Y*Y < R*R.

