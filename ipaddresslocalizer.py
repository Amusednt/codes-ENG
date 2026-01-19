import socket
import uuid
import re

def get_network_identity():
    """
    Retrieves the local IP address and the physical MAC address of the machine.
    """
    print("--- Network Identity ---")
    
    # Get Local IP Address
    try:
        # Connecting to a public DNS to find the local interface IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"Local IP: {local_ip}")
    except Exception:
        print("Local IP: Could not detect")

    # Get MAC Address
    # uuid.getnode() returns the hardware address as a 48-bit integer
    mac_hex = hex(uuid.getnode())
    # Formatting the hex string into standard MAC format (XX:XX:XX:XX:XX:XX)
    mac_addr = ':'.join(re.findall('..', mac_hex[2:].zfill(12)))
    print(f"MAC Address: {mac_addr.upper()}")

if __name__ == "__main__":
    get_network_identity()
