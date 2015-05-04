#!/usr/bin/env python
import dendropy
from dendropy import Tree, TaxonSet
from dendropy.utility.fileutils import find_files
import os
import sys
#Usage: python converter.py 'path to files' 'extension of files' 'format of input files' 'format you'd like exported'
o_file = sys.argv[1]

data = dendropy.DnaCharacterMatrix.get_from_path(o_file, sys.argv[2], preserve_underscores=True) 
data.write_to_path(sys.argv[3], sys.argv[4], space_to_underscores=True,force_unique_taxon_labels=False) 

