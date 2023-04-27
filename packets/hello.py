# /usr/bin/python
import struct

# Hello Packet
# Type 1
PKT_TYPE = 1


def create_packet(seq, ttl, src):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1),  src(4)
    header = struct.pack('BBBL', PKT_TYPE, seq, ttl, src)
    return header


def read_header(pkt):
    header = pkt[0:32]
    # pktFormat = "BBBL"
    pkttype, seq, ttl, src = struct.unpack("BBBL", header)
    return pkttype, seq, ttl, src
