import random
import string

from typing import Any
from pydantic import BaseModel

def generate_str(l: int) -> str:
    '''Generates a random string of length `l`.'''
    p = r"""!#$%&()*+,-./:<=>?@[]^_`{|}~"""
    all = string.ascii_letters + string.digits + p
    return "".join([random.choice(p) for i in range(l)])

def get_letter() -> str:
    '''Generates a character of length 1 corresponding to a random ASCII letter'''
    return random.choice(string.ascii_letters)

def get_letters(l: int) -> str:
    '''Generates a random string of *only* ASCII letters of length `l`.'''
    return "".join([random.choice(string.ascii_letters) for i in range(l)])

def get_li(amt: int) -> str:
    '''Returns "lI" repeated `l` times.'''
    return "lI"*amt

def obfuscate_str(s: str, secret: int) -> str:
    return ";".join(bytes(str(ord(i)*secret).encode()).hex() for i in s)

class Token(BaseModel):
    key: int
    name: str
    type: str
    value: Any = ""
    isUseful: bool = False # Represents users source code or is just a blob of useless code


    def generate_source(self) -> str:
        match self.type:
            case "int":
                self.value = random.randint(0, 10_000_000)
            case "str":
                self.value = f"fluoride_lIlIlIlIlIlIlIlIlIlIlI(\"{obfuscate_str(get_letters(random.randint(1, 50)), self.key)}\",{self.key})"
            case "list":
                self.value = "[]"
            case "tuple":
                self.value = "()"
            case "set":
                self.value = "set()"
            case "bool":
                self.value = str(random.choice([True, False]))
            case "none":
                self.value = None
            case "useful":
                ...
            case _:
                self.value = None
        if self.isUseful:
            return f"fluoride_lIlIlIlIlIlIlIlIlIlIlIlI=exec;{self.name}=fluoride_lIlIlIlIlIlIlIlIlIlIlIlI(fluoride_lIlIlIlIlIlIlIlIlIlIlI(\"{obfuscate_str(self.value, self.key)}\",{self.key}));"
        return f"fluoride_{self.name}={self.value};"