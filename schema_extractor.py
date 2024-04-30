#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:47:21 2024

@author: maximeb
"""

path = "/home/maximeb/github/demo_federated_query/Turismo Profesional de Espana"

file_name = "turismo_employees.csv"

separator = ";"

with open(f"{path}/{file_name}", "r") as f:
    first_line = f.readline().strip("\n").split(f"{separator}")
    with open(f"{path}/columns_turismo.txt", "w") as f:
        for col in first_line:
            f.write(col)
            f.write("\n")