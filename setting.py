

import os
import platform
import socket

import subprocess
import re

global app_port
global basic_url
global fram_width
global fram_height
global transmit_ip
transmit_ip=''
global limit_fps
global save_fps_period

app_port=5005
basic_url='100.94.180.13'
limit_fps=50
limit_report_table=100
save_fps_period=10
waiting_running_phase=60*5
waiting_transmit_phase=60*5
is_docker=True

fram_width=1000
fram_height=500


def set_trabsmit_ip(ip,host_name):
    global transmit_ip
    transmit_ip=get_ip_by_name(host_name)
    return transmit_ip
 
    # if '192.168' in ip:
    #     transmit_ip=get_ip_address()   
    # elif '100.' in ip:
    #     transmit_ip=get_tailscale_ip()          
    

import subprocess


def get_tailscale_ip():
    #return '100.94.180.13'
    try:
        # Run the 'tailscale ip' command and capture its output
        result = subprocess.run(['tailscale', 'ip'], capture_output=True, text=True, check=True)
        # Extract the IPv4 address from the command output using regex
        ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', result.stdout)
        # Return the first IPv4 address found
        if ip_addresses:
            return ip_addresses[0]
        else:
            return None
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur when running the command
        print(f"Error: {e}")
        return None
# Get the Tailscale IP address
# tailscale_ip = get_tailscale_ip()
# if tailscale_ip:
#     print(f"Tailscale IP address: {tailscale_ip}")
# else:
#     print("Failed to retrieve Tailscale IP address.")
         
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This connects to Google's public DNS server to get your IP address
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    finally:
        s.close()
    return 'host.docker.internal'
def get_host_name():
    #print('start get_host_name')
    hostname = socket.gethostname()
   # print('end get_host_name',hostname)
    return hostname
# def get_host_name():
#     # Get the hostname from the environment variable, if not set, use the container's hostname
#     hostname = os.getenv('HOST_NAME', socket.gethostname())
#     print(f'Hostname: {hostname}')
#     return hostname
def get_docker_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f'Container IP Address: {ip_address}')
    return ip_address

def get_ip_by_name(host_name):
    #ip_address='100.74.149.25'
    if(is_docker):
        ip_address =  '172.17.0.2'
    else:    
        if host_name=='Halduns-MacBook-Pro.local':
            ip_address='100.94.180.13'
        # ip_address='192.168.214.200' 
            #ip_address='192.168.214.200'
        elif host_name=='inas':
            ip_address='100.125.217.38'
        elif host_name=='mainsight-desktop':
            ip_address='100.103.105.34'
        elif host_name=='anas-desktop':
            ip_address='100.74.149.25' 
        elif host_name=='gama':
            ip_address='100.66.253.61'
        elif host_name=='ubuntu':
            ip_address='100.83.167.45'
        else:
            ip_address =  '172.17.0.2'
            container_ip = 'host.docker.internal'

        
        #ip_address=get_ip_address()   
        global basic_url
        basic_url=ip_address 

        return ip_address



# def get_tailscale_ipv4_address():
#     try:
#         # Run the ipconfig command and capture its output
#         output = subprocess.check_output(['ipconfig']).decode('utf-8')
#         # Use regular expressions to find the Tailscale adapter section
#         tailscale_pattern = r'Unknown adapter Tailscale:(.*?)Wireless LAN adapter'
#         match = re.search(tailscale_pattern, output, re.DOTALL)
#         if match:
#             tailscale_section = match.group(1)
#             # Within the Tailscale adapter section, search for the IPv4 address
#             ipv4_pattern = r'IPv4 Address\. . . . . . . . . . . : (\d+\.\d+\.\d+\.\d+)'
#             ipv4_match = re.search(ipv4_pattern, tailscale_section)
#             if ipv4_match:
#                 ipv4_address = ipv4_match.group(1)
#                 return ipv4_address
#         return None
#     except Exception as e:
#         print("An error occurred:", e)
#         return None
def get_tailscale_ipv4_address():
    try:
        # Detect the operating system
        operating_system = platform.system()

        # Execute the appropriate command based on the operating system
        if operating_system == 'Windows':
            output = subprocess.check_output(['ipconfig']).decode('utf-8')
            # Use regular expressions to find the Tailscale adapter section
            tailscale_pattern = r'Unknown adapter Tailscale:(.*?)Wireless LAN adapter'
            match = re.search(tailscale_pattern, output, re.DOTALL)
            if match:
                tailscale_section = match.group(1)
                # Within the Tailscale adapter section, search for the IPv4 address
                ipv4_pattern = r'IPv4 Address\. . . . . . . . . . . : (\d+\.\d+\.\d+\.\d+)'
                ipv4_match = re.search(ipv4_pattern, tailscale_section)
                if ipv4_match:
                    ipv4_address = ipv4_match.group(1)
                    return ipv4_address
        elif operating_system in ['Linux', 'Darwin']:
            output = subprocess.check_output(['ifconfig']).decode('utf-8')
            tailscale_pattern = r'utun\d: flags=\d+<.*?> mtu (\d+)\n\s+inet (\d+\.\d+\.\d+\.\d+) '
            match = re.search(tailscale_pattern, output)
            if match:
                ipv4_address = match.group(2)
                return ipv4_address
        else:
            print("Unsupported operating system:", operating_system)
            return None

        # Use regular expressions to find the Tailscale adapter section
       
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname) 


# local=True
# # print("con Your Computer Name is:" + hostname)
# # print("  con  Computer IP Address is:" + IPAddr)
# interstedArea=[[(0,0),(0,500),(1000,500),(1000,0) ]]
# frameSize=(1000, 500)
# basic_url='100.103.105.34'
# basic_url='192.168.1.117'
# basic_url='100.94.180.13'
# basic_url='100.103.105.34'
# basic_url='100.94.180.13'
# #100.125.217.38
# if local :
# #if IPAddr=='127.0.0.1':
#     basic_url='127.0.0.1'
#     basic_url='100.94.180.13'
#     # basic_url='100.125.217.38'
#     basic_url='100.125.217.38'
   
  
   

       
    
    

    
   
    
    #basic_url='100.98.164.136'
    #basic_url='100.74.149.25'

