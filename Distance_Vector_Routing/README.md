
# Distance Vector Routing Simulator

## 📘 Project Overview

This project is part of the CS 6250: Computer Networking course at Georgia Tech. The goal is to simulate a Distance Vector (DV) routing protocol using the distributed Bellman-Ford algorithm. Students implement the DV algorithm in Python to route traffic based on hop counts and link weights, including the ability to handle negative link costs and detect negative weight cycles.

## 🎯 Project Goals

- Implement a **distributed routing protocol** based on the Bellman-Ford algorithm.
- Simulate how routers update distance vectors using only local knowledge and neighbor communication.
- Handle diverse topologies, including directed graphs, negative weights, and negative cycles.
- Detect and mark infinite-cost paths (`-99`) when negative cycles are encountered.

## 🧩 Implementation Highlights

### Distance Vector Logic

- Each node maintains a **local distance vector** mapping destinations to path costs.
- Initially, each node knows:
  - Itself at distance 0.
  - Its directly connected neighbors with known link weights.
- Nodes periodically exchange distance vectors and update their own based on:
  - Received neighbor distances + link weight.
  - Lower costs take precedence; tie-breaking is not needed since all nodes are unique.
- Distance vectors are advertised only to upstream neighbors.

### Negative Cycle Handling

- If a node detects a route to a destination via a **negative weight cycle**, it must mark the destination with a cost of **-99**, representing "negative infinity".
- A node **must never advertise a negative cost to itself**.

### Logging

Log the final distance vector per node using this format:
```
Node:Destination1Distance,Destination2Distance,...
```
Example:
```
A:A0,B2,C5
```

Use the `add_entry` method in `DistanceVector.py` to record log entries. Logs should be written per round and validated using `output_validator.py`.

## 🧪 Running the Simulation

Run your implementation on a topology using:

```bash
./run.sh SimpleTopo
```

> Do not include the `.txt` extension when specifying the topology file.

This generates a `SimpleTopo.log` file containing the round-by-round distance vectors.

## 🔍 Topology Variants for Testing

Expect your code to be tested against topologies that include:

- Simple and complex routing loops
- Directed and weighted links (including weights between -50 and 50)
- Negative cycles
- Nodes with only incoming or only outgoing links
- Node names with more than one character

## 📌 Key Assumptions

- Path weights are integers; lowest valid weight is `-99`
- Distance to self is always 0 and never negative
- No multi-graphs or disconnected components in tested topologies
- Implementation must terminate naturally (no infinite loops)

## 🔗 References

- [Bellman-Ford Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- Kurose & Ross – *Computer Networking: A Top-Down Approach*, Ch. 5
- [Negative Weight Cycles (Udacity)](https://classroom.udacity.com/courses/ud401/lessons/10046800612/)
