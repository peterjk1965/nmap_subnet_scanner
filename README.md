# nmap_subnet_scanner
python script to scan subnet and common ports using nmap

Prerequisites

    Install Nmap: Ensure that nmap is installed on your system. You can install it using your package manager. For example:
        On Ubuntu/Debian:

bash

sudo apt-get install nmap

On macOS (using Homebrew):

bash

brew install nmap

________________________________________

How It Works:

    Common Ports: The script defines a string of common ports to scan.
    Nmap Command: It constructs the nmap command using a list, which includes the -p option to specify the ports and the subnet to scan.
    Subprocess Execution: The script uses subprocess.run() to execute the nmap command and captures the output.
    Output: The results of the scan are printed to the console.

Usage:

    Save the script to a file, e.g., nmap_subnet_scanner.py.
    Run the script using Python 3:

bash

python3 nmap_subnet_scanner.py
