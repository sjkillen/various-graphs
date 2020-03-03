#!/usr/bin/env python3
"""
Generate a visualization for 3-values models for the following logic program:
c <- 
a <- c, u
b <- b, u

Where u is fixed as undefined
"""

from itertools import product
from frozendict import frozendict
from graphviz import Digraph

possible_interpretations = {
    frozendict({
        "a": a,
        "b": b,
        "c": c,
    }) for a, b, c in product(("t", "u", "f"), repeat=3)
}

assert len(possible_interpretations) == 27

graph = Digraph()