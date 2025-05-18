
# BGP Measurements (BGPM) Project

## 📘 Project Overview

This project introduces students to **Internet Measurements** using the BGP protocol. You’ll analyze real-world routing data using **PyBGPStream**, a Python interface for interacting with **BGPStream**—a powerful toolkit used by researchers and engineers to study routing behavior, growth trends, and anomalies in BGP (Border Gateway Protocol). The project is entirely data-driven and relies on **pre-cached historical BGP data**.

## 🎯 Project Objectives

- Explore how BGP route tables grow over time.
- Analyze changes in prefix advertisement and AS-path lengths.
- Identify and measure announcement-withdrawal and blackholing event durations.
- Gain experience with PyBGPStream for offline data analysis.

## 🧰 Technologies Used

- **Python 3**
- **PyBGPStream**
- **BGPStream**
- **RIB** and **Update cache files** (provided)

---

## 🧩 Tasks Breakdown

### ✅ Task 1: Routing Table Growth

- **1A:** `unique_prefixes_by_snapshot()`  
  Count unique advertised prefixes per RIB snapshot.

- **1B:** `unique_ases_by_snapshot()`  
  Count unique AS numbers (in full AS-paths) per snapshot.

- **1C:** `top_10_ases_by_prefix_growth()`  
  Compute prefix growth % for each origin AS across all snapshots.

### ✅ Task 2: AS Path Length Evolution

- `shortest_path_by_origin_by_snapshot()`  
  Calculate shortest AS-path length per origin AS across time.  
  Deduplicate repeated ASes in paths. Ignore paths of length 1.

### ✅ Task 3: Announcement-Withdrawal (AW) Durations

- `aw_event_durations()`  
  Measure how long a prefix is advertised before it is explicitly withdrawn for a peerIP/prefix pair.  
  Only explicit A → W pairs count as AW events.

### ✅ Task 4: Remote Triggered Blackholing (RTBH)

- `rtbh_event_durations()`  
  Identify announcements tagged with RTBH community attributes and measure duration until withdrawal.  
  Only explicit W following latest RTBH A is considered.

---

## 🧪 Running the Tests

Use the provided harness:
```bash
python check_solution.py
```

> Make sure your final code passes all tests using the **unmodified** `check_solution.py`.

---

## 📎 References & Resources

- [PyBGPStream Docs](https://bgpstream.caida.org/docs/api/pybgpstream)
- [PyBGPStream GitHub](https://github.com/CAIDA/pybgpstream)
- [RFC 4271: BGP-4](https://www.rfc-editor.org/rfc/rfc4271.txt)
- [IMC Conference](https://conferences.sigcomm.org/imc/2022/)
