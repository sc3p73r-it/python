import socket
import whois

def get_ip_info(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        host_name = "Unknown"
        
    try:
        whois_info = whois.whois(ip_address)
    except Exception as e:
        whois_info = str(e)

    return (host_name, whois_info)

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    host_name, whois_info = get_ip_info(ip_address)
    print("Host name:", host_name)
    print("WHOIS information:", whois_info)
