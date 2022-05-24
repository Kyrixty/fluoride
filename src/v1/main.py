import binascii
from obf import create_py, deobfuscate, get_source_from_file, obfuscate

def do_obf(secret: int, fileName: str, outFile: str) -> None:
    fileSrc = get_source_from_file(fileName)
    o = obfuscate(fileSrc, secret)
    d = deobfuscate(o, secret)
    src = create_py(o, secret)
    with open(outFile, mode="w") as f:
        f.write(src)

def main() -> None:
    secret = int(input("Secret: "))
    fileName = input("File name: ")
    out = input("Output file name: ")
    iters = int(input("Iterations: "))
    for i in range(iters):
        if not i:
            do_obf(secret, fileName, out)
        else:
            do_obf(secret, out, out)

if __name__ == "__main__":
    main()