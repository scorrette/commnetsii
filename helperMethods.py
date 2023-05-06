def ipv4_to_int(ipv4_str):
    octets = ipv4_str.split('.')
    if len(octets) != 4:
        raise ValueError("Invalid IPv4 string")

    # Convert each octet to an integer and shift it to its position
    ip_int = 0
    for i in range(4):
        octet_int = int(octets[i])
        if octet_int < 0 or octet_int > 255:
            raise ValueError("Invalid IPv4 string")
        ip_int += octet_int << (24 - 8 * i)

    return ip_int


def int_to_ipv4(ip_int):
    if ip_int < 0 or ip_int > 0xFFFFFFFF:
        raise ValueError("Invalid IP address")

    # Convert the 32-bit integer to four octets
    octets = []
    for i in range(4):
        octet_int = (ip_int >> (24 - 8 * i)) & 0xFF
        octets.append(str(octet_int))

    # Join the octets together with dots to get the IPv4 string
    ipv4_str = ".".join(octets)
    return ipv4_str
