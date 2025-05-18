
# BGP Hijacking Attack Simulation

## 📘 Project Overview

This project explores the **vulnerability of the Border Gateway Protocol (BGP)** to hijacking attacks. Using Mininet and Quagga routing software, students simulate real-world cyberattacks where malicious Autonomous Systems (ASes) reroute traffic by advertising false BGP routes. Through hands-on emulation, students gain practical knowledge of how routing attacks are launched and how Internet traffic can be misdirected or intercepted.

## 🎯 Project Objectives

- Understand the BGP routing protocol and its trust-based vulnerabilities
- Simulate a prefix hijacking attack where a rogue AS steals traffic via false advertisements
- Configure and analyze routing behavior using Quagga (bgpd/zebra)
- Build and document a custom attack topology based on real-world examples

## 🧰 Technologies Used

- **Mininet** for network emulation
- **Quagga** (bgpd and zebra) for router configuration
- **Python** for automation and interaction scripts
- **Linux CLI** tools for diagnostics

---

## 🧪 Project Tasks

### 🔹 Part 1: Background & Setup

- Read the overview of BGP hijacking attacks.
- Review provided Quagga configs and routing commands.
- Understand how path length and prefix specificity affect BGP behavior.

### 🔹 Part 2: Demo Simulation

1. Start the Mininet topology:
   ```bash
   sudo python bgp.py
   ```
2. In a second terminal, connect to router R1:
   ```bash
   ./connect.sh
   ```
   Enter password: `en`  
   View BGP table:
   ```bash
   sh ip bgp
   ```

3. In a third terminal, simulate traffic:
   ```bash
   ./website.sh
   ```

4. In a fourth terminal, launch the hijack:
   ```bash
   ./start_rogue.sh
   ```

5. Observe hijack behavior in website.sh output and BGP routing tables.

6. Stop the attack:
   ```bash
   ./stop_rogue.sh
   ```

---

### 🔹 Part 3: Custom Attack Topology

- Draw and submit `fig2_topo.pdf` based on the referenced academic paper (Fig 2).
- Modify demo code to create a new topology with 6 ASes (AS1 to AS6).
- Assign IP prefixes per AS (e.g., AS1: 11.0.0.0/8, AS2: 12.0.0.0/8, etc.).
- Recreate the hijack scenario using the new topology.
- Demonstrate behavior similar to the original simulation:
  - Observe normal routing
  - Launch rogue AS hijack
  - Observe hijack behavior
  - Stop the attack and observe recovery

> ⚠️ The Mininet `pingall` command may not work reliably — use `website.sh` for validation.
