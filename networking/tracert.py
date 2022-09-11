# references:
#   Learning by doing: Writing your own traceroute in 8 easy steps (Ksplice Blog)
#   https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your

import sys
import socket

def traceroute(dest_addr, max_hops=30, timeout=0.2):
    proto_icmp = socket.getprotobyname('icmp')
    proto_udp = socket.getprotobyname('udp')
    port = 33434

    for ttl in range(1, max_hops+1):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        msg = ''.encode("utf-8")
        rx.bind((msg, port))
        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto(msg, (dest_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = None
        finally:
            rx.close()
            tx.close()

        yield curr_addr

        if curr_addr == dest_addr:
            break

if __name__ == "__main__":
    dest_name = sys.argv[1]
    dest_addr = socket.gethostbyname(dest_name)
    print("traceroute to %s (%s)" % (dest_name, dest_addr))
    for i, v in enumerate(traceroute(dest_addr)):
        print("%d\t%s" % (i+1, v))
