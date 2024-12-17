import psutil
import time
import subprocess

def get_mac_address(interface="wlan0"):
    """Get the MAC address of the given network interface."""
    try:
        # Get the MAC address using psutil
        addrs = psutil.net_if_addrs()
        if interface in addrs:
            for addr in addrs[interface]:
                if addr.family == psutil.AF_LINK:
                    return addr.address
    except Exception as e:
        print(f"Error getting MAC address: {e}")
    return None

def monitor_mac_address():
    """Monitor the MAC address and alert if it changes."""
    print("Monitoring MAC address...")
    
    # Get initial MAC address
    current_mac = get_mac_address()
    if current_mac:
        print(f"Initial MAC address: {current_mac}")
    else:
        print("Failed to get MAC address.")
        return
    
    while True:
        time.sleep(5)  # Check every 5 seconds
        new_mac = get_mac_address()
        
        if new_mac != current_mac:
            print(f"Warning: MAC address has changed! New MAC: {new_mac}")
            current_mac = new_mac  # Update the current MAC to the new one

if __name__ == "__main__":
    monitor_mac_address()
