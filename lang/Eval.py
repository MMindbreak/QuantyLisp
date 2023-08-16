from .Types import Exp, Symbol, Number
from .Env import global_env, Env


class Procedure:
    def __init__(self, params, body, env):
        self.params, self.body, self.env = params, body, env

    def __call__(self, *args):
        new_env = Env(self.params, args, self.env)
        return quanty_lisp_eval(self.body, new_env)


def quanty_lisp_eval(x: Exp, env=global_env) -> Exp:
    """Evaluate an expression in an environment."""
    if isinstance(x, Symbol):  # variable reference
        return env.find(x)[x]
    elif isinstance(x, Number):  # constant number
        return x
    op, *args = x
    if op == 'quote':
        (_, exp) = x
        return exp
    elif op == 'if':  # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if quanty_lisp_eval(test, env) else alt)
        return quanty_lisp_eval(exp, env)
    elif op == 'define':  # definition
        (_, symbol, exp) = x
        env[symbol] = quanty_lisp_eval(exp, env)
    elif op == 'set!':
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif op == "lambda":
        (params, body) = args
        return Procedure(params, body, env)
    else:  # procedure call
        proc = quanty_lisp_eval(x[0], env)
        args = [quanty_lisp_eval(arg, env) for arg in x[1:]]
        return proc(*args)
