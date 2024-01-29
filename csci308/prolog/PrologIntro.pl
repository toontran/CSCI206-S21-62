
% Food
food(sushi).
food(tiramisu).
food(creamPuff).
food(pho).
food(fish).

% When
breakfast(pho).
lunch(pho).
lunch(tiramisu).
lunch(sushi).
dinner(pho).
dinner(creamPuff).
dinner(sushi).

% Favorite food
favorite(wittie, sushi).
favorite(tung, pho).
favorite(tung, tiramisu).

meal(N, F) :- favorite(N, F), breakfast(F), write('Take '), write(N), write(' out for a '), write(F), write(' breakfast.').
meal(N, F) :- favorite(N, F), lunch(F), write('Take '), write(N), write(' out for a '), write(F), write(' lunch.').
meal(N, F) :- favorite(N, F), dinner(F), write('Take '), write(N), write(' out for a '), write(F), write(' dinner.').

