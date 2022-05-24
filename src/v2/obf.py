import random
import sys

from types import ModuleType
from typing import Callable, Set
from inspect import getmembers, getsource, isfunction
from models.token import Token, get_li


def registerToken(token: str, registry: set) -> set:
    """Returns a new registry"""
    registry.add(token)
    return registry


def createTokens(amt: int, uid: int,  fs: str) -> list[Token]:
    all_types = [
        "set",
        "list",
        "list",
        "list",
        "list",
        "list",
        "list",
        "tuple",
        "dict",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "str",
        "bool",
        "none",
    ]
    tokens = []

    for i in range(amt):
        if i == uid:
            tokens.append(
                Token(
                    key=random.randint(0, 999_999_999),
                    type="useful",
                    name=f"fluoride_{get_li(random.randint(1, 10))}",
                    isUseful=True,
                    value=fs,
                )
            )
        else:
            tokens.append(Token(
                key=random.randint(0, 999_999_999),
                type=all_types[random.randint(0, len(all_types) - 1)],
                name=get_li(random.randint(1, 10)),
            ))
    return tokens

def getSource(moduleOrCallable: ModuleType | Callable):
    return getsource(moduleOrCallable)


def getFuncsFromModule(m: ModuleType):
    return getmembers(m, isfunction)


def getMembers(m: ModuleType):
    ignore = [
        "__builtins__",
        "__cached__",
        "__doc__",
        "__spec__",
        "__loader__",
        "__name__",
        "__package__",
        "__file__",
    ]
    members = [member for member in getmembers(m) if not member[0] in ignore]
    return members
