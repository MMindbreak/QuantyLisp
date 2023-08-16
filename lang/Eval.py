from .Types import *
from .Env import global_env


def quanty_lisp_eval(x: Exp, env=global_env) -> Exp:
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):  # variable reference
        return env[x]
    elif isinstance(x, Number):  # constant number
        return x
    elif x[0] == 'if':  # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if quanty_lisp_eval(test, env) else alt)
        return quanty_lisp_eval(exp, env)
    elif x[0] == 'define':  # definition
        (_, symbol, exp) = x
        env[symbol] = quanty_lisp_eval(exp, env)
    else:  # procedure call
        proc = quanty_lisp_eval(x[0], env)
        args = [quanty_lisp_eval(arg, env) for arg in x[1:]]
        return proc(*args)
