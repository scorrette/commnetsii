#!/usr/bin/python3
import struct

# Hello Packet
# Type 4
PKT_TYPE = 4
PACK_FORMAT = "BBBLL"

def create_packet(seq, ttl, src, dest, data):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1),  src(4), dest(4)
    header = struct.pack(PACK_FORMAT, PKT_TYPE, seq, ttl, src, dest)
    return header + bytes(data, "utf-8")


def read_header(pkt):
    # TODO check numbers
    header = pkt[0:struct.calcsize(PACK_FORMAT)]
    # pktFormat = "BBBLL"
    pkttype, seq, ttl, src, dest = struct.unpack(PACK_FORMAT, header)
    return pkttype, seq, ttl, src, dest


def read_content(pkt):
    return pkt[struct.calcsize(PACK_FORMAT):]
