import requests
import time

def check_sites(url_list):
    """
    Checks the status and response time of multiple websites.
    :param url_list: List of website URLs (including http/https).
    """
    print(f"{'URL':<30} | {'STATUS':<10} | {'RESPONSE TIME':<15}")
    print("-" * 60)

    for url in url_list:
        try:
            start_time = time.time()
            # Send a GET request with a 5-second timeout
            response = requests.get(url, timeout=5)
            end_time = time.time()
            
            elapsed = f"{end_time - start_time:.2f}s"
            status = "ONLINE" if response.status_code == 200 else f"CODE {response.status_code}"
            
            print(f"{url:<30} | {status:<10} | {elapsed:<15}")
            
        except requests.exceptions.RequestException:
            print(f"{url:<30} | {'OFFLINE':<10} | {'N/A':<15}")

# Test with common domains
sites = ["https://www.google.com", "https://www.github.com", "https://site-that-doesnt-exist.xyz"]
check_sites(sites)
