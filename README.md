# Goal

The goal is to align two different bus trips datasets to one common ontology, and to generate an RDF version of each, in order to ease the manipulation of their geographical data. 


# How-to

Copy the following commands:

    java -jar ./rmlmapper-java/target/rmlmapper-6.5.1-r373-all.jar ./datasets/paris_bus.csv -c ./config/paris_bus.properties

    java -jar ./rmlmapper-java/target/rmlmapper-6.5.1-r373-all.jar ./datasets/lyon_bus.csv -c ./config/lyon_bus.properties


Link to RMLMapper: https://github.com/RMLio/rmlmapper-java

Take a look at the results in the folder **results**.
