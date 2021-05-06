ECHO_LINE_LEN = 32

def bin_to_hex(buf: bytes) -> str:
    out = ""
    for val in buf:
        out += "\\\\x{:02x}".format(val)
    return out


def generate_echo(input_file: str, output_file: str):
    first_line = True
    with open(input_file, "rb") as file:
        while(buf := file.read(ECHO_LINE_LEN)):
            cmd = "echo -n -e "+bin_to_hex(buf)+" >"
            if not first_line:
                cmd += ">"
            first_line = False
            yield cmd+output_file+";echo status:$?:end\n"


for i in generate_echo("test.jpg", "aaa"):
    print(i)
    