#!/bin/bash
V1="radno-vreme-10"
V2="radni-dani"
egrep "$V1|$V2" node.1.data.txt
