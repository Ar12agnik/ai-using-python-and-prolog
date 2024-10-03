Sum of list: 
sum_l([], 0).
sum_l([Head|Tail], Res) :-
    sum_l(Tail, Prev_res),
    Res is Head + Prev_res.
factorial:

fact(0,1).
fact(N,Res):-
N>0,
Prev is N-1,
fact(Prev,Prev_result),
Res is N * Prev_result.