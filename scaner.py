def scan(hosts_input):
    import socket
    import sys
    mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1234, 1433, 1500, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 8800, 10000, 20000]

    host = hosts_input
    mas = []
    for port in mas:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            s.close
            mas.append(str(port))
    return mas
