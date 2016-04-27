# Eurycea Genomics Project

Find a phylogenetics-focused workshop using these data [here](https://github.com/wrightaprilm/BodegaBayWorkshop)  
Find a data matrix assembly-focused workshop [here](https://github.com/wrightaprilm/ISU-01-06 )


Files for eurycea project. Descriptions follow:

+ JA14300popmap, JA14785popmap and total_popmap: Barcodes sorted by individual, for each
sequencing run separately, and both combined. For more information on why these barcode 
files are need it, please see [this](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037135)
paper on ddRAD sequencing.

+ Converter.py: short script using the [dendropy 3.x](https://pythonhosted.org/DendroPy/) 
library to convert between file formats. Usage:

```python
python converter.py 'path to files' 'extension of files' 'format of input files' 'format you'd like exported'
```
Example
```python converter.py ./ .nex nexus DNAphylip

+ Populations, cstacks, sstacks, ustacks, process_rad: Scripts for the [Stacks](http://catchenlab.life.illinois.edu/stacks/)
pipeline

+ relabel_str.py: Relabeling script, as Stacks outputs files with their numerical names, 
rather than their locality data. Would be smart to change this to take an input file of 
names, rather than having them hardcoded, but I never got around to it.

+ Rename.py: modification of script from Becca Tarvin to rename files output from process_rad,
which are named for their barcodes. Could combine this and relabelstr.py to add in the 
locality data earlier.

+ Renexus.py: This is actually the same script as relabelstr.py. I should delete one of
them, but it feels ... dishonest?


