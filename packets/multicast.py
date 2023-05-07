#!/usr/bin/python3
import struct

# multicast Packet
# Type 3
PKT_TYPE = 3
PACK_FORMAT = 'BBBBLLL'


def create_packet(seq, ttl, kval, dests, data):
    """Create a new packet based on given id"""
    # pktType(1),  seq(1), ttl(1), kval(1), dest1-3(4-12), data()
    header = struct.pack(PACK_FORMAT, PKT_TYPE, seq, ttl, kval, dests[0], dests[1], dests[2])

    if type(data) is str:
        data = bytes(data, "utf-8")
    return header + data


def read_header(pkt):
    header = pkt[0:struct.calcsize(PACK_FORMAT)]
    # pktFormat = "BBBLL"
    pkttype, seq, ttl, kval, dest1, dest2, dest3 = struct.unpack(PACK_FORMAT, header)
    dests = [dest1, dest2, dest3]

    return pkttype, seq, ttl, kval, dests


def read_data(pkt):
    # TODO
    pass
