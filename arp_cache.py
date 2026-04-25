hosts = {
    "172.16.0.1": "00:11:22:23:44:55",
    "172.16.0.10": "DE:AD:BE:EF:00:03",
    "172.16.0.12": "00:12:22:23:43:53",
    "172.16.0.13": "00:11:22:23:44:77",
    "172.16.0.40": "00:11:22:23:44:88",
    "172.16.0.254": "00:11:22:23:44:99",
}

print("Welcome to PythonArpCache")
ip_addr = input("Which IP address to look up? ")

mac_addr = hosts.get(ip_addr)

if mac_addr:
    print(f"The host IP address {ip_addr} maps to MAC add {mac_addr}")
else:
    print(f"The host IP address {ip_addr} is not found")
    hosts[ip_addr] = "Incomplete     "

    print("! show ip arp")
    print("Protocol Hardware Addr    Type Address")
    for cached_ip, cached_mac in hosts.items():
        print(f"Internet   {cached_mac}   ARPA   {cached_ip}")