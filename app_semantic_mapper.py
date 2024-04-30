#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:49:42 2024

@author: maximeb
"""

import streamlit as st
from rdflib import Graph
from ontology_flatter import flattened_ontology
from schema_extractor import columns

st.title('Eona-X Semantic Mapper')

flattened_ontology.keys()

option = st.selectbox(
    'Columns of CSV dataset',
    (columns))

st.write('You selected:', option)