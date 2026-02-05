import psutil

def monitor_active_connections():
    """
    Scans and prints all active network connections.
    Shows the local address, status, and the PID of the owner process.
    """
    print(f"{'Local Address':<25} | {'Status':<15} | {'PID'}")
    print("-" * 50)

    # Get a list of all current network connections
    connections = psutil.net_connections()

    for conn in connections:
        # We look for 'LISTEN' or 'ESTABLISHED' status
        if conn.status in ('LISTEN', 'ESTABLISHED'):
            local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
            print(f"{local_addr:<25} | {conn.status:<15} | {conn.pid}")

if __name__ == "__main__":
    monitor_active_connections()
