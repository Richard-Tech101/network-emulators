interface_names = [
    "Ethernet0/1",
    "Ethernet0/2",
    "Ethernet0/3",
    "Ethernet0/4",
    "Ethernet0/5",
    "Ethernet0/6",
    "Ethernet0/7",
    "Ethernet0/8",
]


mac_table = {}

def forward_frame(dst_mac, egress_port):
    print(f" ! Frame with destination {dst_mac} forwarding out of {egress_port}")

def flood_frame(dst_mac, ingress_port):
    print(f" Flooding to all other ports")
    for egress_port in interface_names:
        if egress_port != ingress_port:
            forward_frame(dst_mac, egress_port)

def incoming_frame(src_mac, dst_mac, ingress_port):
    print(f"!!!Received frame on {ingress_port} from {src_mac} to {dst_mac}")
    mac_table[src_mac] = ingress_port
    if dst_mac in mac_table:
        egress_port = mac_table[dst_mac]
        print(f" !!xx!! Address {dst_mac} found in MAC table on {egress_port}")
        forward_frame(dst_mac, egress_port)
    elif dst_mac == "FF:FF:FF:FF:FF:FF":
        print(f"  !!xx!! Destination is broadcast")
        flood_frame(dst_mac, ingress_port)
    else:
        print(f" XXXXX Address {dst_mac} NOT found in MAC table")
        flood_frame(dst_mac, ingress_port)


def show_mac_address_table():
    sh_mac_addr_banner = """
! show mac address-table

    Mac Address Table
-----------------------------------

Mac Adress          Type         Ports
----------          --------     -----
"""
    print(sh_mac_addr_banner)
    for mac_addr, intf_name in sorted(mac_table.items()):
        print(f"{mac_addr}   DYNAMIC      {intf_name}")


incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/1")
incoming_frame(src_mac="DE:AD:BF:BE:11:02", dst_mac="00:00:11:33:44:77", ingress_port="Ethernet0/2")
incoming_frame("66:77:88:99:AA:01", "FF:FF:FF:FF:FF:FF", "Ethernet0/1")
incoming_frame("12:34:56:78:9A:04", "AA:BB:CC:DD:EE:02", "Ethernet0/8")
incoming_frame("00:11:22:33:44:55", "DE:AD:BF:BE:11:02", "Ethernet0/4")
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/7")
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/5")
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/7")
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/8")
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/2")
incoming_frame("00:00:11:33:44:77", "00:11:22:33:44:55", "Ethernet0/1")


show_mac_address_table()
