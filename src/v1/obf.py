def get_source_from_file(fileName: str) -> str:
    with open(fileName, mode="r") as f:
        return f.read()

def obfuscate(code: str, secret: int) -> str:
    return ",".join(bytes(str(ord(i)*secret).encode()).hex() for i in code)

def deobfuscate(o: str, secret: int) -> str:
    return "".join(chr(int(int(bytes.fromhex(token))/secret)) for token in o.split(","))

def create_py(o: str, secret: int) -> str:
    return f"""def d(o,s):return "".join(chr(int(int(bytes.fromhex(t))/s)) for t in o.split(","))
exec(d("{o}",{secret}))"""