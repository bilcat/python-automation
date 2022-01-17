import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open('switches.txt')

for IP in f:
    IP = IP.strip()
    print("Get running config from Switch " + IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    # setting terminal length to 0 will help to get the config at once, instead of pressing more to see each page
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readOutput = tn.read_all()
    saveOutput = open("switch" + HOST, "w")
    saveOutput.write(readOutput.decode('ascii'))
    saveOutput.write("\n")
    saveOutput.close()
    print(tn.read_all().decode('ascii'))
