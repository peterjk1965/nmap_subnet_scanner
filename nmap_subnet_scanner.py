import subprocess

def scan_subnet(subnet):
    """Scan the specified subnet for common open ports using nmap."""
    # Define the common ports to scan
    common_ports = "21,22,23,25,53,80,110,143,443,3306,8080"
    
    # Construct the nmap command
    command = ["nmap", "-p", common_ports, subnet]
    
    try:
        # Run the nmap command
        print(f"Scanning subnet: {subnet} for common ports...")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the output of the nmap command
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while scanning: {e}")

if __name__ == "__main__":
    subnet_input = "192.168.2.0/24"  # Define the subnet to scan
    scan_subnet(subnet_input)
