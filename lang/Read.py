from .Types import *


def tokenize(chars: str) -> list[str]:
    return chars.replace("(", " ( ").replace(")", " ) ").split()


def read_from_tokens(tokens: list) -> Exp:
    """Read an expression from a sequence of tokens."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L: list[Atom] = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token: str) -> Atom:
    """Numbers become numbers; every other token is a symbol."""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def quanty_lisp_parse(program: str) -> Exp:
    """Read a Scheme expression from a string."""
    return read_from_tokens(tokenize(program))
