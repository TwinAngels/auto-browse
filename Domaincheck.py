import socket

def is_domain_valid(line):
    try:
        socket.gethostbyname(line)
        return True
    except socket.error:
        return False

# check if a domain is valid
domain = open("urls-validated.txt", "r")
file = open("domain_validation_outcome.txt", "w")
with open("urls.txt") as f:
    for line in f:       
        if is_domain_valid(line):
            print(f"{line} is a valid domain")
        else:
            print(line)
            