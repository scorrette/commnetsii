#!/usr/bin/python3
import struct

# Hello Packet
# Type 1
PKT_TYPE = 1
PACK_FORMAT = "BBBL"

def create_packet(seq, ttl, src):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1),  src(4)
    header = struct.pack(PACK_FORMAT, PKT_TYPE, seq, ttl, src)
    return header


def read_header(pkt):
    header = pkt[0:struct.calcsize(PACK_FORMAT)]
    pkttype, seq, ttl, src = struct.unpack(PACK_FORMAT, header)
    return pkttype, seq, ttl, src
