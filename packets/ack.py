#!/usr/bin/python3
import struct

# ACK Packet
# Type 5
PKT_TYPE = 5
PACK_FORMAT = "BBLL"

def create_packet(seq, src, dest):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1),  src(4), dest(4)
    header = struct.pack(PACK_FORMAT, PKT_TYPE, seq, src, dest)

    return header

def read_header(pkt):
    # TODO check numbers
    header = pkt[0:struct.calcsize(PACK_FORMAT)]
    # pktFormat = "BBBLL"
    pkttype, seq, src, dest = struct.unpack(PACK_FORMAT, header)
    return pkttype, seq, src, dest

