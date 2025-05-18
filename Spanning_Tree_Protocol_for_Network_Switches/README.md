
Spanning Tree Protocol (STP) Simulator
======================================

 Project Overview
-------------------
This project is part of the CS 6250: Computer Networking course at Georgia Tech. It involves implementing a simplified, distributed version of the Spanning Tree Protocol (STP) in Python. The goal is to simulate how Layer 2 network switches use message passing to build a loop-free spanning tree topology.

 Project Goals
----------------
- Understand and implement a **distributed network algorithm**.
- Simulate the Spanning Tree Protocol without global topology knowledge.
- Handle dynamic topology changes such as node drops and TTL-limited messages.
- Ensure simulation correctness through conforming to strict output format.


 Implementation Details
-------------------------
### Core Functionality
- Track each switchs **view of the root switch**, **distance to the root**, and **active forwarding links**.
- Use message passing to update switch state and topology view.
- Log the final spanning tree in the specified format (e.g., `1 - 2, 2 - 4`).

### Message Format
```python
msg = Message(claimedRoot, distanceToRoot, originID, destinationID, pathThrough, ttl)
```

### Active Link Decision Rules
- Switch updates path if a lower root is seen or a shorter path is discovered.
- Use neighbor ID as a tie-breaker for equal path lengths.
- TTL is decremented on every message relay to avoid infinite propagation.

 Running the Simulation
-------------------------
Run the simulation using the following command:
```bash
python run.py SimpleLoopTopo
```
This will simulate the STP on `SimpleLoopTopo.py` and print the final spanning tree.

 Logging Format
-----------------
Spanning tree links must be logged in **sorted format** as:
```
1 - 2, 1 - 3, 2 - 4
```
Incorrect formats (e.g., unordered links) may lead to **point deductions**.

 Key Assumptions
------------------
- Switch IDs are distinct positive integers.
- Only one path is used per switch to reach the root.
- A single connected spanning tree must result.
- Switches adapt to topology changes and dropped nodes.

 References
-------------
- https://en.wikipedia.org/wiki/Spanning_Tree_Protocol
- https://docs.python.org/3/tutorial/datastructures.html
