Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict
Quasiquote = Symbol  # for `
Unquote = Symbol  # for ,
UnquoteSplicing = Symbol  # for ,@
