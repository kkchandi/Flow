# Flow

This problem is a part of CS 330, a computer science course at Duke University titled Design and Analysis of Algorithms. 

**Problem Statement**

You are a city planner trying to optimize traffic flow in the city’s transportation network. Imagine a city with a complex network of roads and highways but with only one entry point s and one exit point t. You are asked to increase the traffic capacity driving from s to t but are only allotted with the money to widen one road such that its capacity would increase.

Assume now the city road map is converted into a directed graph (not necessarily acyclic) with nodes labeled as integers and with non-negative integer capacities on the edges. Your function will take in two parallel lists edges and capacities, where each edge is a tuple. For example, (2, 4) is an edge that goes from starting node 2 to destination node 4. You are also given the label of a source vertex and a target vertex.

We say that an edge is a priority edge for routing traffic flow from source s to target t if increasing the capacity on that edge by 1 (with no other changes to the graph) would increase the value of the maximum flow from s to t.

Given the above inputs, you should design and implement an algorithm that returns a list of all priority edges in the graph (or an empty list if there are none). The list can be in any order. For full credit, your solution will need to have an empirical runtime that is within constant factors of an O(nm2) reference solution where n is the number of vertices and m is the number of edges.

**Language-specific Details** 
[Python]

def find_edges(edges:[(u:int,v:int)], capacities:[int], s:int, t:int) and returns a list of tuples (u,v) that are priority edges or an empty list []
