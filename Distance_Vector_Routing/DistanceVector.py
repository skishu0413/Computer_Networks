# Distance Vector project for CS 6250: Computer Networks
#
# This defines a DistanceVector (specialization of the Node class)
# that can run the Bellman-Ford algorithm. The TODOs are all related
# to implementing BF. Students should modify this file as necessary,
# guided by the TODO comments and the assignment instructions. This
# is the only file that needs to be modified to complete the project.
#
# Student code should NOT access the following members, otherwise they may violate
# the spirit of the project:
#
# topolink (parameter passed to initialization function)
# self.topology (link to the greater topology structure used for message passing)
#
# Copyright 2017 Michael D. Brown
# Based on prior work by Dave Lillethun, Sean Donovan, Jeffrey Randow, new VM fixes by Jared Scott and James Lohse.

from helpers import *
from Node import *


class DistanceVector(Node):
    
    def __init__(self, name, topolink, outgoing_links, incoming_links):
        """ Constructor. This is run once when the DistanceVector object is
        created at the beginning of the simulation. Initializing data structure(s)
        specific to a DV node is done here."""

        super(DistanceVector, self).__init__(name, topolink, outgoing_links, incoming_links)
        
        # TODO: Create any necessary data structure(s) to contain the Node's internal state / distance vector data
        self.distance_vector = {self.name: 0}
        self.original_distance_vector = self.distance_vector.copy()

    def send_initial_messages(self):
        """ This is run once at the beginning of the simulation, after all
        DistanceVector objects are created and their links to each other are
        established, but before any of the rest of the simulation begins. You
        can have nodes send out their initial DV advertisements here.

        Remember that links points to a list of Neighbor data structure.  Access
        the elements with .name or .weight """

        # TODO - Each node needs to build a message and send it to each of its neighbors
        # HINT: Take a look at the skeleton methods provided for you in Node.py
        self.send_messagess_to_neighbors()

    def process_BF(self):
        """ This is run continuously (repeatedly) during the simulation. DV
        messages from other nodes are received here, processed, and any new DV
        messages that need to be sent to other nodes as a result are sent. """

        # Implement the Bellman-Ford algorithm here.  It must accomplish two tasks below:
        # TODO 1. Process queued messages
        update_status = False
        for msg in self.messages:
            sender_name, received_distance_vector = msg[0], msg[1]

            # Iterate through the received distance vector
            for node_name, distance in received_distance_vector.items():
                if self.name != node_name:

                    # Retrive current distance to the node
                    current_distance = self.distance_vector.get(node_name, float('inf'))

                    # Get the weight of the link to the sender
                    link_weight = self.get_outgoing_neighbor_weight(sender_name)

                    # If distance is -99, mark the node as unreachable
                    if distance <= -99:
                        self.distance_vector[node_name] = -99
                        update_status = True
                    else:
                        #convert link_weight to int, if not, set it to 0
                        try:
                            link_weight = int(link_weight)
                        except ValueError:
                            link_weight = 0

                        new_weight = distance + link_weight

                        # Update the distance if the new weight is smaller
                        if new_weight < current_distance:
                            self.distance_vector[node_name] = new_weight
                            update_status = True
            pass
        
        # Empty queue
        self.messages = []

        # TODO 2. Send neighbors updated distances
        if update_status and self.distance_vector != self.original_distance_vector:
            self.send_messagess_to_neighbors()
            self.original_distance_vector = self.distance_vector.copy()

    def send_messagess_to_neighbors(self):
        message = [self.name, self.distance_vector]
        for neighbor_name in self.neighbor_names:
            self.send_msg(message, neighbor_name)

    def log_distances(self):
        """ This function is called immedately after process_BF each round.  It
        prints distances to the console and the log file in the following format (no whitespace either end):
        
        A:A0,B1,C2
        
        Where:
        A is the node currently doing the logging (self),
        B and C are neighbors, with vector weights 1 and 2 respectively
        NOTE: A0 shows that the distance to self is 0 """
        
        # TODO: Use the provided helper function add_entry() to accomplish this task (see helpers.py).
        # An example call that which prints the format example text above (hardcoded) is provided.
        # add_entry("A", "A0,B1,C2")
        
        formatted_text = []
        for node_name in sorted(self.distance_vector):
            formatted_text.append(node_name + str(self.distance_vector[node_name]))
        formatted_text = ','.join(formatted_text)
        add_entry(self.name, formatted_text)
