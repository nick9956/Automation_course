import re
import  socket

def check_ip_re(ip_address):
    pattern = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(pattern) and all(map(lambda n: 0 <= int(n) <= 255, pattern.groups()))

def check_ip_inet_pton(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  #
        return False

    return True