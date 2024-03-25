Goal

The goal is to align two different bus trips datasets to one common ontology, and to generate an RDF version of each, in order to ease the manipulation of their geographical data. 


Tools Used 

API connection is made with requests Python library. 

Python data manipulation librairies were used such as pandas and json. 

Most importantly, RML language4 was used to define the rules to create RDF triples from the datasets files. It was executed by the CLI Java program RMLMappe5r in order to generate the RDF triples. 

Link to RMLMapper: https://github.com/RMLio/rmlmapper-java
