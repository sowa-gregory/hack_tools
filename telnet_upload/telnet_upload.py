import os
import math
import getpass
import telnetlib
import argparse
ECHO_LINE_LEN = 256
HOST = "pc-server"

'''
telnet_login
Login to remote server using telnet protocol
'''


def telnet_login(host: str, user: str, password: str) -> telnetlib.Telnet:
    telnet = telnetlib.Telnet(host)
    telnet.read_until(b"login: ")
    print('asdf')
    telnet.write(user.encode('ascii') + b"\n")
    if password:
        telnet.read_until(b"Password: ")
        telnet.write(password.encode('ascii') + b"\n")

    out = telnet.expect([b".*Last login:.*", b".*Login incorrect.*"], 10)
    if out[0] == 0:
        return telnet
    return None


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


def upload_file(telnet: telnetlib.Telnet, input_file: str, output_file: str):
    curr_line = 1
    num_lines = math.ceil(os.path.getsize(input_file)/ECHO_LINE_LEN)
    prev_percent = -1

    for line in generate_echo(input_file, output_file):
        percent = math.floor(curr_line/num_lines*100)
        if percent > prev_percent:
            print("progress:", percent)
            prev_percent = percent
        curr_line += 1
        telnet.write(bytes(line, 'ascii'))
        status = telnet.expect([b"status:0:end.?\n"], 1)
        if status[0] == -1:
            raise Exception("upload error")


def main():
    user = input("Enter your remote account: ")
    password = getpass.getpass()

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--user', type=str,
                        help='user name for telnet session')
    parser.add_argument('file', type=str,
                        help='file to transfer - use format {local_path}:{remote_path}')

    args = parser.parse_args()
    files = args.file.split(":")
    if len(files) != 2:
        raise Exception("invalid format of file argument")
    input_file, output_file = files

    telnet = telnet_login(HOST, user, password)
    if not telnet:
        print("invalid credentials")
        exit(1)
    else:
        print("logon ok")

    upload_file(telnet, input_file, output_file)
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))


main()
