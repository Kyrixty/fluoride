import hashlib
import random

from misc import source
from obf import createTokens


def main() -> None:
    global source
    tokenSize = 20000
    sourceFile = f"{input('Source File (no extension): ')}.py"
    outFile = f"{input('Output File Name (no extension): ')}.fl.py"
    with open(sourceFile, mode="r") as f:
        fileSrc = f.read()
    tokens = createTokens(tokenSize, random.randint(0, tokenSize-1), fileSrc)
    for i, token in enumerate(tokens):
        source += token.generate_source()
    source = source.replace("$SOURCE_HASH$", hashlib.sha256(source.encode()).hexdigest())
    with open(outFile, mode="w") as f:
        f.write(source)

if __name__ == "__main__":
    main()
