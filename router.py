import ipaddress

class Router:
    RIB = []
    FIB = []

    def __init__(self, hostname):
        self.hostname = hostname
        print(f"Router {self.hostname} is booting...")

    def add_route(self, network, prefix_length, next_hop):
        new_route = {
            "network": network,
            "prefix_length": prefix_length,
            "next_hop": next_hop
        }
        self.RIB.append(new_route)
        self.calculate_fib()

    def calculate_fib(self):
        print(f"!! Calculating FIB for router {self.hostname}")
        print(" !X Clearing existing FIB")
        self.FIB = []
        for route in self.RIB:
            new_fib_entry = {
                "prefix": ipaddress.IPv4Network(f"{route['network']}/{route
                ['prefix_length']}"),
                "next_hop": ipaddress.IPv4Address(route["next_hop"])
            }
            print(f" !Populating FIB entry: {new_fib_entry}")

    def show_ip_route(self):
        sh_ip_route_banner = """
Codes:  C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, O3 - OSPFv3, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route
"""
        print(sh_ip_route_banner)
        for route in self.RIB:
            print(f"    {route['network']}/{route['prefix_length']} via {route['next_hop']}")
       

corerouter = Router("core-01")

corerouter.add_route("10.5.16.0", 23, "192.0.2.1")
corerouter.add_route("10.5.17.64", 28, "192.0.2.3")
corerouter.add_route("10.5.0.0", 16, "192.0.2.4")
corerouter.add_route("10.10.20.0", 24, "192.0.2.1")

corerouter.show_ip_route()
