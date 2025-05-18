
# Simulating Networks with Mininet

## 📘 Project Overview

This optional warm-up project introduces students to **Mininet**, a network emulator used to simulate realistic computer network topologies. The goal is to help students understand how to:

- Define static and dynamic network topologies using Python
- Run and interpret network simulations (bandwidth, delay, loss)
- Use Mininet CLI tools to inspect and verify topology behavior
- Build a scalable data center topology with user-defined parameters

## 🧰 Technologies Used

- **Mininet** (network simulation)
- **Python 3.8**
- **Ubuntu 20.04** (within the course virtual machine)


## 🛠️ Project Parts

### Part 1: Mininet CLI Commands

Familiarize yourself with commands from the Mininet prompt (`mininet>`):

- `nodes`, `net`, `links`, `dump` – view network components and states
- `ping`, `pingall` – verify connectivity
- `exit` – terminate Mininet

> Clean the environment using `sudo mn -c` after each simulation.

### Part 2: Defining Topologies

- Modify `mntopo.py` to expand the topology to 2 hosts, 3 switches, and 4 links.
- Adjust `delay` in the `linkConfig` to 10ms and `bw` to 50 Mbps.
- Run `sudo ./topology.sh` and generate updated `bwm.txt` and `rate.png`.
- Save all outputs and the updated `mntopo.py` for submission.

### Part 3: Complex Topology Simulation

- Edit `complextopo.py` to create:
  - Hosts: `h1`, `h2`, `h3`
  - Switches: `s1`, `s2`, `s3`, `s4`
- Link types and their characteristics:
  - Ethernet: 25 Mbps, 2 ms delay, 0% loss
  - WiFi: 10 Mbps, 6 ms delay, 3% loss
  - 3G: 3 Mbps, 10 ms delay, 8% loss
- Use `sudo python ./cli.py` to enter the CLI and interact with hosts via `ping`, `pingall`, etc.

### Part 4: Datacenter Topology

- Complete `datacenter.py` to generate a **fan-in** datacenter topology using parameters:
  - `fi`: number of mid-level switches
  - `n`: number of hosts per rack switch
- Launch using:

```bash
sudo python datacenter.py --fi 2 --n 2
```

- Validate with `nodes`, `dump`, and `pingall`.

