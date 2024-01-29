% gender & parents
male('Fred').
male('Barny').
male('Bamm-bamm').
female('Wilma').
female('Betty').
female('Pebbles').
nonBinary('Acid Storm').
parent('Fred', 'Pebbles').
parent('Wilma', 'Pebbles').
parent('Barny', 'Bamm-bamm'). % Yes, Bamm-bamm is adopted. He still has parents...
parent('Betty', 'Bamm-bamm').
parent('Pebbles', 'Acid Storm').
parent('Bamm-bamm', 'Acid Storm').

% relationships
father(Dad, Child) :- male(Dad), parent(Dad, Child).
mother(TheMom, TheChild) :- female(TheMom), parent(TheMom, TheChild).
son(TheMaleChild, TheParent) :- male(TheMaleChild), parent(TheParent, TheMaleChild).
daughter(TheFemaleChild, TheParent) :- female(TheFemaleChild), parent(TheParent, TheFemaleChild).
child(TheChild, TheParent) :- parent(TheParent, TheChild).
grandparent(TheGrandparent, TheGrandchild) :- parent(TheGrandparent, Parent), parent(Parent, TheGrandchild).
sibling(ThePerson, TheirSibling) :- parent(Parent, ThePerson), parent(Parent, TheirSibling), ThePerson \= TheirSibling.
aunt(TheAunt, TheChild) :- female(TheAunt), parent(Parent, TheChild), sibling(Parent, TheAunt).
uncle(TheUncle, TheChild) :- male(TheUncle), parent(Parent, TheChild), sibling(Parent, TheUncle).
cousin(ThePerson, TheirCousin) :- parent(Parent1, ThePerson), parent(Parent2, TheirCousin), sibling(Parent1, Parent2), not(sibling(ThePerson, TheirCousin)).
ancestor(TheAncestor, TheDescendant) :- parent(TheAncestor, TheDescendant).
ancestor(TheAncestor, TheDescendant) :- parent(TheAncestor, SomePerson), ancestor(SomePerson, TheDescendant).