# 🌐 Python Network Emulator Suite
### Built by Richard | Aspiring Network Automation & AI Agentic Specialist

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Richard--Tech101-black)](https://github.com/Richard-Tech101)

---

## 📌 Overview

# This is constantly updated and revised - Any credit will be provided to the source if applicable. This serves as a learning journal for educational purposes only.
A Python-based network protocol emulation suite built from first principles — implementing Layer 1 through Layer 3 forwarding logic in code. Each module replicates the core behavior of real enterprise network devices (Cisco, Arista) demonstrating deep understanding of switching, routing and ARP fundamentals that underpin modern network automation.

This project bridges the gap between network engineering and software development — proving that understanding how networks work at the code level is the foundation of building autonomous, agentic network systems.

---

## 🎯 Why This Project Exists

Most network engineers understand *what* a MAC table does.  
Few can explain *how* it works in code.

This suite encodes core networking intelligence into Python — the same logic used in:
- GNS3 / EVE-NG virtual network emulators
- Cisco and Arista network operating systems
- SDN controller forwarding decisions
- AI agent tool libraries for agentic network operations

---

## 📁 Project Structure

```
network-emulators/
│
├── ethernet_hub.py          # Layer 1/2 — Hub with port flooding
├── arp_cache.py             # Layer 2/3 — ARP cache simulation
├── ethernet_switch.py       # Layer 2 — MAC learning and forwarding
├── interface_counters.py    # Telemetry — In/out frames and bytes
├── routing_table.py         # Layer 3 — RIB/FIB with OOP Router class
├── ipv4_forwarding.py       # Layer 3 — IPv4 longest prefix match
├── router_benchmark.py      # Performance — Forwarding benchmarking
└── README.md
```

---

## 🔧 Modules

### 1. `ethernet_hub.py` — Layer 1/2 Hub Emulator
Simulates a network hub with port flooding behavior.

**Concepts demonstrated:**
- Ingress port identification
- Broadcast flooding to all ports except ingress
- Why hubs were replaced by switches (security/efficiency)

**Real world equivalent:** Physical hub — all devices see all traffic

```python
# Example usage
incoming_signal("Ethernet0/1", frame_data)
# Floods to Ethernet0/2, 0/3, 0/4 automatically
```

---

### 2. `arp_cache.py` — ARP Cache Simulation
Replicates Address Resolution Protocol cache lookup and storage.

**Concepts demonstrated:**
- IP to MAC address mapping
- Cache hit vs cache miss behavior
- Incomplete entry handling
- Cisco `show ip arp` output format

**Real world equivalent:** `show ip arp` on Cisco/Arista

```python
# Example usage
lookup_arp("172.16.0.1")
# Returns: 00:11:22:23:44:55
```

---

### 3. `ethernet_switch.py` — Layer 2 Switch with MAC Learning
Full Layer 2 switch emulation with dynamic MAC address learning.

**Concepts demonstrated:**
- MAC address table population
- Unicast forwarding vs unknown unicast flooding
- Broadcast handling (FF:FF:FF:FF:FF:FF)
- MAC move detection
- Cisco `show mac address-table` output format

**Real world equivalent:** Cisco Catalyst / Arista EOS switching ASIC

```python
# Example usage
incoming_frame("00:11:22:33:44:55", "DE:AD:BE:EF:00:01", "Ethernet0/1", 64)
# Learns source MAC, forwards or floods based on destination
```

---

### 4. `interface_counters.py` — Interface Telemetry
Tracks per-interface packet and byte counters for ingress and egress traffic.

**Concepts demonstrated:**
- Stateful counter tracking
- Ingress vs egress separation
- Cisco `show interfaces` output format
- Foundation of network telemetry and monitoring

**Real world equivalent:** `show interfaces` counters on any network device

---

### 5. `routing_table.py` — Router with RIB and FIB (OOP)
Object-oriented Router class implementing Routing Information Base and Forwarding Information Base.

**Concepts demonstrated:**
- RIB vs FIB separation (exactly as real routers implement)
- IPv4Network and IPv4Address using Python ipaddress module
- Longest prefix match forwarding algorithm
- Route types (Static, OSPF, BGP, Connected)
- Arista EOS `show ip route` output format

**Real world equivalent:** Control plane (RIB) and data plane (FIB) on Cisco/Arista

```python
# Example usage
router = Router("core-01")
router.add_route("10.5.16.0", 23, "192.0.2.1", "O")
router.forward_packet("10.5.16.50")
# Longest prefix match → via 192.0.2.1
```

---

### 6. `ipv4_forwarding.py` — IPv4 Packet Forwarding *(coming soon)*
Pure IPv4 forwarding logic with longest prefix match at packet level.

---

### 7. `router_benchmark.py` — Router Performance Benchmarking *(coming soon)*
Measures packets per second forwarding performance of the emulated router.

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.10+
```

### Installation
```bash
git clone https://github.com/Richard-Tech101/network-emulators.git
cd network-emulators
```

### Run Any Module
```bash
python ethernet_hub.py
python arp_cache.py
python ethernet_switch.py
python interface_counters.py
python routing_table.py
```

---

## 📊 OSI Layer Coverage

| Module | OSI Layer | Concept |
|--------|-----------|---------|
| `ethernet_hub.py` | L1 / L2 | Physical flooding |
| `arp_cache.py` | L2 / L3 | Address resolution |
| `ethernet_switch.py` | L2 | MAC learning |
| `interface_counters.py` | L1 / L2 | Telemetry |
| `routing_table.py` | L3 | IP forwarding |
| `ipv4_forwarding.py` | L3 | Packet forwarding |
| `router_benchmark.py` | L3 | Performance |

---

## 🔗 Real World Validation

Each module output mirrors real Cisco/Arista CLI commands:

| Module | Equivalent CLI Command |
|--------|----------------------|
| `arp_cache.py` | `show ip arp` |
| `ethernet_switch.py` | `show mac address-table` |
| `interface_counters.py` | `show interfaces` |
| `routing_table.py` | `show ip route` |

---

## 🧠 Learning Path Context

This project is part of a broader network automation journey:

```
Network Emulator (this repo)
        ↓
Device Automation (Netmiko + Ansible)
        ↓
Container Platform (Docker + Kubernetes)
        ↓
CI/CD Pipeline (Jenkins + GitHub)
        ↓
AI Agent Layer (LangChain + Python)
        ↓
Agentic Network Operations (Syntrevo NetAgent)
```

---

## 📜 Credits & Inspiration

This project was built as part of my network automation learning journey.

**Primary inspiration and learning source:**
- [ ] Source 1: `[Author/Course Name] — [URL or platform]`
- [ ] Source 2: `[Author/Course Name] — [URL or platform]`
- [ ] Source 3: `[Book/Resource Name] — [Author]`

**Technical references:**
- [ ] Cisco IOS documentation — [cisco.com/c/en/us/support](https://cisco.com/c/en/us/support)
- [ ] Arista EOS documentation — [arista.com/en/support](https://arista.com/en/support)
- [ ] Python ipaddress module — [docs.python.org/3/library/ipaddress.html](https://docs.python.org/3/library/ipaddress.html)
- [ ] RFC 791 — IPv4 — [tools.ietf.org/html/rfc791](https://tools.ietf.org/html/rfc791)
- [ ] RFC 826 — ARP — [tools.ietf.org/html/rfc826](https://tools.ietf.org/html/rfc826)
- [ ] RFC 4271 — BGP — [tools.ietf.org/html/rfc4271](https://tools.ietf.org/html/rfc4271)

**All code was written and modified independently as part of my personal learning and professional development.**

---

## 👤 About

**Richard**  
 

- 🏢 Disney NOC — Arista/Cisco enterprise production
- 🎓 CCNA | Linux LPI | CompTIA A+
- 🔄 CCNP Enterprise | DevNet Professional (in progress)
- ☁️ AWS Cloud Practitioner (in progress)
- 🐍 Python network automation
- 🤖 Building agentic network operations platform

**Connect:**
- [ ] LinkedIn: `[your LinkedIn URL]`
- [ ] GitHub: [github.com/Richard-Tech101](https://github.com/Richard-Tech101)
- [ ] Company: 

---

## 📄 License

MIT License — feel free to use, modify and distribute with attribution.

---

## 🗺️ Roadmap

- [x] ethernet_hub.py
- [x] arp_cache.py  
- [x] ethernet_switch.py
- [x] interface_counters.py
- [x] routing_table.py
- [ ] ipv4_forwarding.py
- [ ] router_benchmark.py
- [ ] Netmiko integration — connect emulator to real devices
- [ ] Docker containerization
- [ ] LangChain agent tools — emulator as AI agent library
- [ ] Syntrevo NetAgent v1 integration
- [ ] Multi provisioning of  Arista configurations pushed by python

---

*Built with purpose — understanding networks at the code level is the foundation of building networks that run themselves.*

