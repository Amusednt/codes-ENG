import cpuinfo # Library to get detailed CPU info
import platform
import psutil

def get_system_specs():
    """
    Collects and prints hardware specifications of the current machine.
    Useful for system diagnostic tools.
    """
    print("--- System Information ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Hostname: {platform.node()}")

    print("\n--- CPU Information ---")
    # Using cpuinfo to get the actual marketing name of the processor
    info = cpuinfo.get_cpu_info()
    print(f"Processor: {info['brand_raw']}")
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Threads: {psutil.cpu_count(logical=True)}")

    print("\n--- Memory Information ---")
    virtual_mem = psutil.virtual_memory()
    # Convert bytes to Gigabytes for readability
    print(f"Total RAM: {virtual_mem.total / (1024**3):.2f} GB")

if __name__ == "__main__":
    get_system_specs()
