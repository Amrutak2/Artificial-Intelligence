move(state(middle,onbox,middle,hasnot),

grasp,state(middle,onbox,middle,has)).

move(state(P,onfloor,P,hasnot),climb,

state(P,onbox,P,hasnot)).

move(state(P,onfloor,P,hasnot),push,

state(P1,onfloor,P1,hasnot)).

move(state(P1,onfloor,B,hasnot),walk(P1, P2),

state(P2,onfloor,B,hasnot)).



canget(state(_,_,_,has)).

canget(State1) :-

move(State1,_,State2),

canget(State2).
