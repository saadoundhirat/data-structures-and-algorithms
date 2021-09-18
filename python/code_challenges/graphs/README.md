# Graphs Code challenge35
<!-- Short summary or background information -->
building a graph class that includes the following methods:

- add_node
- add_edge
- get_nodes
- get_edges
- get_neighbors
- breadth_first_search
- depth_first_search

## Challenge
<!-- Description of the challenge -->
building a graph class that includes the following methods:

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Using a dictionary to store the nodes and edges.

## API
<!-- Description of each method publicly available in your Graph -->
- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

# Code challenge 36

## Breadth First Traversal On a Graph Implementation

## Challenge Summary

- Write the following method for the Graph class:
  - breadth first.
  - Arguments: Node.
  - Return: A collection of nodes in the order they were visited.
  - Display the collection.

## Approach & Efficiency

  [breadth-first-traversal-white-Board](https://docs.google.com/document/d/1909T0vptnvTf7tn8nBFmsQptelrWWZUdOv47uUDmQWk/edit?usp=sharing)

- Big O:
  - Time: O(n)
  - Space: O(n)

# Code challenge 37

## Business Trip Itinerary

## Challenge Summary

- Write a function called business trip.
        - Arguments: graph, array of city names.
        - Return: cost or null.

- Determine whether the trip is possible with direct flights, and how much it would cost.

## Approach & Efficiency

  ![business-trip-itinerary]()

- Big O:
  - Time: O(n)
  - Space: O(1)

## Tasks

- [x] Top-level README “Table of Contents” is updated.
- [x] Feature tasks for this challenge are completed.
- [x] Unit tests written and passing.
- [x] Edge Case (if applicable/obvious).
- [x] README for this challenge is complete.
- [x] Description, Approach & Efficiency, Solution.
- [x] Link to code.

---
