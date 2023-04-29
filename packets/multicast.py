#!/usr/bin/python3
import struct

# multicast Packet
# Type 3
PKT_TYPE = 3
PACK_FORMAT_1 = 'BBBBL'
PACK_FORMAT_2 = 'BBBBBL'
PACK_FORMAT_3 = 'BBBBBBL'

def create_packet(seq, ttl, src, dests, data):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1), kval(1), dest1-3(4-12), data()
    if len(dests) == 1:
        header = struct.pack(PACK_FORMAT_1, PKT_TYPE, seq, ttl, 1, dests[0])
    elif len(dests) == 2:
        header = struct.pack(PACK_FORMAT_2, PKT_TYPE, seq, ttl, 2, dests[0], dests[1])
    elif len(dests) == 3:
        header = struct.pack(PACK_FORMAT_3, PKT_TYPE, seq, ttl, 3, dests[0], dests[1], dests[2])
    return header + bytes(data,"utf-8")


def read_header(pkt):
    header = pkt[0:32]
    # pktFormat = "BBBLL"
    pkttype, seq, ttl, kval, dest1, dest2, dest3 = struct.unpack(PACK_FORMAT_3, header)
    if kval == 1:
        dests = [dest1]
    elif kval == 2:
        dests = [dest1,dest2]
    elif kval == 3:
        dests = [dest1,dest2,dest3]

    return pkttype, seq, ttl, kval, dests

def read_data(pkt):
    #TODO
    pass
