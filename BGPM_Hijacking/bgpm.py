#!/usr/bin/env python3

import pybgpstream
from collections import defaultdict

"""
CS 6250 BGP Measurements Project

Notes:
- Edit this file according to the project description and the docstrings provided for each function
- Do not change the existing function names or arguments
- You may add additional functions but they must be contained entirely in this file
"""


# Task 1A: Unique Advertised Prefixes Over Time
def unique_prefixes_by_snapshot(cache_files):
    """
    Retrieve the number of unique IP prefixes from each of the input BGP data files.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list containing the number of unique IP prefixes for each input file.
        For example: [2, 5]
    """
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    unique_prefixes_by_snapshot = []

    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here

        unique_IP_Prefixes = set()
        for elem in stream:
            prefix = elem.fields['prefix']
            unique_IP_Prefixes.add(prefix)
        unique_prefixes_by_snapshot.append(len(unique_IP_Prefixes))

    return unique_prefixes_by_snapshot


# Task 1B: Unique Autonomous Systems Over Time
def unique_ases_by_snapshot(cache_files):
    """
    Retrieve the number of unique ASes from each of the input BGP data files.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list containing the number of unique ASes for each input file.
        For example: [2, 5]
    """
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    unique_ases_by_snapshot = []

    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here

        unique_ases = set()
        for rec in stream.records():
            for elem in rec:
                ases = elem.fields["as-path"].split()
                if ases:
                    unique_ases.update(ases)
        
        unique_ases_by_snapshot.append(len(unique_ases))

    return unique_ases_by_snapshot


# Task 1C: Top-10 Origin AS by Prefix Growth
def top_10_ases_by_prefix_growth(cache_files):
    """
    Compute the top 10 origin ASes ordered by percentage increase of advertised prefixes (smallest to largest)

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A list of the top 10 origin ASes ordered by percentage increase of advertised prefixes (smallest to largest)
        AS numbers are represented as strings.

        For example: ["777", "1", "6"]
          corresponds to AS "777" as having the smallest percentage increase (of the top ten) and AS "6" having the
          highest percentage increase (of the top ten).
    """
    # the required return type is 'list' - you are welcome to define additional data structures, if needed
    top_10_ases_by_prefix_growth = []
    as_prefixes = defaultdict(dict)


    for ndx, fpath in enumerate(cache_files):
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution here

        for elem in stream:
            if "prefix" in elem.fields:
                pfx = elem.fields["prefix"]
            else:
                continue

            ases = elem.fields['as-path'].split(" ")
            origin = ases[-1]

            if origin in as_prefixes and ndx in as_prefixes[origin]:
                as_prefixes[origin][ndx].add(pfx)
            else:
                as_prefixes[origin][ndx] = set([pfx])

    prefix_growth = []
    for origin, prefixes in as_prefixes.items():
        try:
            first_prefix_count = len(prefixes[min(prefixes)])
            last_prefix_count = len(prefixes[max(prefixes)])

            if first_prefix_count == 0:
                continue 

            growth_percent = ((last_prefix_count- first_prefix_count) / first_prefix_count) * 100
            prefix_growth.append((origin, growth_percent))
        except keyError:
            continue

    sorted_prefix_growth = sorted(prefix_growth, key = lambda x: x[1], reverse=True)[:10][::-1]
    top_10_ases_by_prefix_growth = [x[0] for x in  sorted_prefix_growth]

    return top_10_ases_by_prefix_growth


# Task 2: Routing Table Growth: AS-Path Length Evolution Over Time
def shortest_path_by_origin_by_snapshot(cache_files):
    """
    Compute the shortest AS path length for every origin AS from input BGP data files.

    Retrieves the shortest AS path length for every origin AS for every input file.

    Your code should return a dictionary where every key is a string representing an AS name and every value is a list
    of the shortest path lengths for that AS.

    Note: If a given AS is not present in an input file, the corresponding entry for that AS and file should be zero (0)
    Every list value in the dictionary should have the same length.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A dictionary where every key is a string representing an AS name and every value is a list, containing one entry
        per file, of the shortest path lengths for that AS
        AS numbers are represented as strings.

        Example:
        Given three cache files (also called "snapshots"), the results {"455": [4, 2, 3], "533": [4, 10, 2]}
        mean that AS 455 has a shortest path length of 4 in the first cache file, a shortest path length of 2 in the second
        cache file, and a shortest path of 3 in the third cache file. Similarly, AS 533 has shortest path lengths of 4, 10, and 2.
    """
    # the required return type is 'dict' - you are welcome to define additional data structures, if needed
    shortest_path_by_origin_by_snapshot = {}

    for ndx, fpath in enumerate(cache_files):
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "rib-file", fpath)

        # implement your solution

        origin_paths = {}
        for elem in stream:
            if elem.fields['as-path'] == "":
                continue
            
            ases = elem.fields['as-path'].split()
            origin = ases[-1]
            unique_as_set = set(ases)
            if len(unique_as_set) == 1:
                continue
            
            path_length = len(unique_as_set)
            if origin not in origin_paths:
                origin_paths[origin] = path_length
            else:
                if path_length < origin_paths[origin]:
                    origin_paths[origin] = path_length

        for origin, shortest_path in origin_paths.items():
            if origin not in shortest_path_by_origin_by_snapshot:
                shortest_path_by_origin_by_snapshot[origin] = [0] * ndx
            shortest_path_by_origin_by_snapshot[origin].append(shortest_path)

        for origin in shortest_path_by_origin_by_snapshot:
            if len(shortest_path_by_origin_by_snapshot[origin]) != ndx + 1:
                shortest_path_by_origin_by_snapshot[origin].append(0) 

    return shortest_path_by_origin_by_snapshot


# Task 3: Announcement-Withdrawal Event Durations
def aw_event_durations(cache_files):
    """
    Identify Announcement and Withdrawal events and compute the duration of all explicit AW events in the input BGP data

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A dictionary where each key is a string representing the address of a peer (peerIP) and each value is a
        dictionary with keys that are strings representing a prefix and values that are the list of explicit AW event
        durations (in seconds) for that peerIP and prefix pair.

        For example: {"127.0.0.1": {"12.13.14.0/24": [4.0, 1.0, 3.0]}}
        corresponds to the peerIP "127.0.0.1", the prefix "12.13.14.0/24" and event durations of 4.0, 1.0 and 3.0.
    """
    # the required return type is 'dict' - you are welcome to define additional data structures, if needed
    aw_event_durations = {}
    aw_event = defaultdict(dict)


    for ndx, fpath in enumerate(cache_files):
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "upd-file", fpath)

        # implement your solution here

        for elem in stream:
            peer_ip = elem.peer_address
            if "prefix" in elem.fields:
                pfx = elem.fields["prefix"]
            else:
                continue

            if elem.type == "A":
                aw_event[peer_ip][pfx] = elem.time
            
            if elem.type == "W":
                if peer_ip in aw_event and pfx in aw_event[peer_ip]:
                    announce_time = aw_event[peer_ip][pfx]
                    withdrawal_time = elem.time
                    aw_duration = withdrawal_time - announce_time
                    if aw_duration > 0:
                        if peer_ip not in aw_event_durations:
                            aw_event_durations[peer_ip] = {}
                        if pfx not in aw_event_durations[peer_ip]:
                            aw_event_durations[peer_ip][pfx] = []
                        aw_event_durations[peer_ip][pfx].append(aw_duration)
                    try:
                        del aw_event[peer_ip][pfx]
                    except keyError:
                        pass
        
    return aw_event_durations


# Task 4: RTBH Event Durations
def rtbh_event_durations(cache_files):
    """
    Identify blackholing events and compute the duration of all RTBH events from the input BGP data

    Identify events where the prefixes are tagged with at least one Remote Triggered Blackholing (RTBH) community.

    Args:
        cache_files: A chronologically sorted list of absolute (also called "fully qualified") path names

    Returns:
        A dictionary where each key is a string representing the address of a peer (peerIP) and each value is a
        dictionary with keys that are strings representing a prefix and values that are the list of explicit RTBH event
        durations (in seconds) for that peerIP and prefix pair.

        For example: {"127.0.0.1": {"12.13.14.0/24": [4.0, 1.0, 3.0]}}
        corresponds to the peerIP "127.0.0.1", the prefix "12.13.14.0/24" and event durations of 4.0, 1.0 and 3.0.
    """
    # the required return type is 'dict' - you are welcome to define additional data structures, if needed
    rtbh_event_durations = {}
    rtbh_event = defaultdict(dict)

    for fpath in cache_files:
        stream = pybgpstream.BGPStream(data_interface="singlefile")
        stream.set_data_interface_option("singlefile", "upd-file", fpath)

        # implement your solution here

        for elem in stream:
            peer_ip = elem.peer_address
            if "prefix" in elem.fields:
                pfx = elem.fields["prefix"]
            else:
                continue

            if elem.type == "A":
                communities = elem.fields.get("communities", [])
                for community in communities:
                    if community.endswith(":666"):
                        rtbh_event[peer_ip][pfx] = elem.time
                        break
                else:
                    if pfx in rtbh_event[peer_ip]:
                        del rtbh_event[peer_ip][pfx]

            if (elem.type == "W"):
                if peer_ip in rtbh_event and pfx in rtbh_event[peer_ip]:
                    announce_time = rtbh_event[peer_ip][pfx]
                    withdrawal_time = elem.time
                    rtbh_duration = withdrawal_time - announce_time
                    if (rtbh_duration > 0):
                        if peer_ip not in rtbh_event_durations:
                                rtbh_event_durations[peer_ip] = {}
                        if pfx not in rtbh_event_durations[peer_ip]:
                                rtbh_event_durations[peer_ip][pfx] = []
                        rtbh_event_durations[peer_ip][pfx].append(rtbh_duration)
                    try:
                        del rtbh_event[peer_ip][pfx]
                    except keyError:
                        pass

    return rtbh_event_durations
