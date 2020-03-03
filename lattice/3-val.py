#!/usr/bin/env python3
"""
Generate a visualization for 3-values models for the following logic program:
c <- 
a <- c, u
b <- b, u

Where u is fixed as undefined
"""

from itertools import product, count
from frozendict import frozendict
from graphviz import Digraph
from string import ascii_lowercase
import networkx as nx

degrees_of_truth = ("t", "u", "f")

def variable_namer():
    for i in count(0):
        yield from map(lambda c: c + "'" * i, ascii_lowercase)

def possible_interpretations():
    pass

variables = "abc"

class Interpretation(frozendict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.T = { var for var, value in self.items() if value == "t" }
        self.F = { var for var, value in self.items() if value == "f" }
        self.U = set(variables) - (self.T | self.F)
        
    def __le__(self, other):
        pass

possible_interpretations = {
    frozendict({
        "a": a,
        "b": b,
        "c": c,
    }) for a, b, c in product(degrees_of_truth, repeat=3)
}
assert len(possible_interpretations) == 27

g = nx.Graph()
g.add_nodes_from(possible_interpretations)

g.ad

graph = Digraph()