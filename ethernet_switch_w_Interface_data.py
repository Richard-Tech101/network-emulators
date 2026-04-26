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

interfaces = {
    "Ethernet0/1":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/2":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/3":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/4":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/5":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/6":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/7":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    },
    "Ethernet0/8":{
        "in_frames": 0,
        "in_bytes": 0,
        "out_frames": 0,
        "out_bytes": 0
    }
}

mac_table = {}

def forward_frame(dst_mac, egress_port, size):
    print(f" ! Frame with destination {dst_mac} forwarding out of {egress_port}")
    interfaces[egress_port]["out_frames"] += 1
    interfaces[egress_port]["out_bytes"] += size

def flood_frame(dst_mac, ingress_port, size):
    print(f" Flooding to all other ports")
    for egress_port in interface_names:
        if egress_port != ingress_port:
            forward_frame(dst_mac, egress_port, size)

def incoming_frame(src_mac, dst_mac, ingress_port, size):
    print(f"!!!Received frame on {ingress_port} from {src_mac} to {dst_mac}")
    interfaces[ingress_port]["in_frames"] += 1
    interfaces[ingress_port]["in_bytes"] += size
    mac_table[src_mac] = ingress_port
    if dst_mac in mac_table:
        egress_port = mac_table[dst_mac]
        print(f" !!xx!! Address {dst_mac} found in MAC table on {egress_port}")
        forward_frame(dst_mac, egress_port, size)
    elif dst_mac == "FF:FF:FF:FF:FF:FF":
        print(f"  !!xx!! Destination is broadcast")
        flood_frame(dst_mac, ingress_port, size)
    else:
        print(f" XXXXX Address {dst_mac} NOT found in MAC table")
        flood_frame(dst_mac, ingress_port, size)

def show_interfaces():
    print("! show interfaces")
    for intf_name, counters in interfaces.items():
        print(intf_name)
        print(f" {counters['in_frames']} frames input, {counters['in_bytes']} bytes")
        print(f" {counters['out_frames']} frames output, {counters['out_bytes']} bytes")
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
        short_name = intf_name[:3] + intf_name[-3:]
        print(f"{mac_addr}   DYNAMIC      {short_name}")


incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/1", 64)
incoming_frame("DE:AD:BF:BE:11:02", "00:00:11:33:44:77", "Ethernet0/2", 200)
incoming_frame("66:77:88:99:AA:01", "FF:FF:FF:FF:FF:FF", "Ethernet0/1", 1500)
incoming_frame("12:34:56:78:9A:04", "AA:BB:CC:DD:EE:02", "Ethernet0/8", 84)
incoming_frame("00:11:22:33:44:55", "DE:AD:BF:BE:11:02", "Ethernet0/4", 860)
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/7", 901)
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/5", 800)
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/7", 1496)
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/8", 700)
incoming_frame("00:00:11:33:44:77", "DE:AD:BF:BE:11:02", "Ethernet0/2", 1200)
incoming_frame("00:00:11:33:44:77", "00:11:22:33:44:55", "Ethernet0/1", 1300)


show_mac_address_table()
show_interfaces()
