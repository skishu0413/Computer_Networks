
# SDN Firewall with POX

## 📘 Project Overview

This project introduces students to **Software Defined Networking (SDN)** using the POX controller. The primary goal is to implement an externally configurable firewall using OpenFlow rules that filter traffic based on MAC/IP addresses, protocols, ports, and subnet ranges. You'll use Python and the Mininet network simulator to define the rules and test traffic behavior across various network topologies.

## 🎯 Project Objectives

- Understand SDN principles using the POX controller.
- Implement firewall rules via OpenFlow in Python.
- Analyze packets using **Wireshark** to design accurate match criteria.
- Apply traffic filtering rules using `configure.pol`.
- Deploy and test the firewall using Mininet-based simulation.

## 🧰 Technologies Used

- **Mininet** (network emulator)
- **POX Controller** (SDN platform)
- **Python 3**
- **Wireshark/tshark** (packet inspection)


## 🧩 Implementation Tasks

### 🔹 Phase 1: Wireshark Packet Capture

- Use `tshark` or `Wireshark` to inspect headers for ICMP, TCP, and UDP.
- Save packet output as `packetcapture.pcap`.
- Identify fields (IP, MAC, port, protocol) needed to craft effective rules.

### 🔹 Phase 2: `configure.pol` Firewall Rules

Define your rule list in the following CSV format:

```
Rule#,Action,MAC-src,MAC-dst,IP-src,IP-dst,Protocol,Port-src,Port-dst,Comment
```

Use `-` for wildcards. All fields are strings.

### 🔹 Phase 3: Implement `sdn-firewall.py`

- Translate rules from `configure.pol` into OpenFlow flow mod objects.
- Use POX `of.ofp_match()` to match fields and apply actions.
- Ensure correct priority for `Allow` (higher) and `Block` (lower) rules.
- Use `of.OFPP_NORMAL` as default forwarding action.

## 🚦 Run and Test the Firewall

### Manual Testing Steps

```bash
./start-firewall.sh configure.pol     # Launch firewall controller
./start-topology.sh                   # Launch Mininet topology
```

### Automated Testing:
```bash
cd test-suite/
cp ../sdn-firewall.py ../configure.pol .
./start-firewall.sh configure.pol
sudo python test_all.py
```
