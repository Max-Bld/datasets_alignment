#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:05:48 2024

@author: maximeb
"""

from rdflib import Graph

#%% load

g = Graph()

ontology_url = "https://raw.githubusercontent.com/Max-Bld/eonax_ontology_prototype/main/eona_semantics_test.ttl"

g.parse(f'{ontology_url}', format='ttl')

#%% query classes

prefixes = """PREFIX : <https://raw.githubusercontent.com/Max-Bld/eonax_ontology_prototype/main/eona_semantics_test.ttl#> 
PREFIX dc: <http://purl.org/dc/terms> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX eona: <https://www.eona-x.eu/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
BASE <https://raw.githubusercontent.com/Max-Bld/eonax_ontology_prototype/main/eona_semantics_test.ttl#> 
"""

q1 = " SELECT DISTINCT ?class WHERE { ?class a owl:Class }"
q2 = " SELECT DISTINCT ?object_property WHERE { ?object_property a owl:ObjectProperty }"
q3 = " SELECT DISTINCT ?datatype_property WHERE { ?datatype_property a owl:DatatypeProperty }"

query_classes = prefixes + q1
query_object_properties = prefixes + q2
query_datatype_properties = prefixes + q3

#%% results

path = "/home/maximeb/github/demo_federated_query/Turismo Profesional de Espana"

class_file = "classes_turismo.txt"
object_properties_file = "object_properties_turismo.txt"
datatype_properties_file = "datatype_properties_turismo.txt"


with open(f"{path}/{class_file}", "w") as f:
    for r in g.query(query_classes):
        f.write(r['class'])
        f.write("\n")
        
with open(f"{path}/{object_properties_file}", "w") as f:
    for r in g.query(query_object_properties):
        f.write(r['object_property'])
        f.write("\n")
        
with open(f"{path}/{datatype_properties_file}", "w") as f:
    for r in g.query(query_datatype_properties):
        f.write(r['datatype_property'])
        f.write("\n")