# -*- coding: utf-8 -*-

"""

Created on Mon Apr 21 21:42:25 2014

@author: RDT

"""

#!/usr/bin/env python

"""This script should be executed from the command line with the following format:

python <script_name> <directory> <file_endings> <barcodefile>

Example: python rename_barcodes_final.py './' '*.fq' 'barcodes.txt'

Type 'module load pylauncher' before running this script.
"""



import glob

import sys

import csv

import pylauncher

csv.field_size_limit(sys.maxsize)



def find_files(directory,file_ending):

    path='%s/*%s' %(directory,file_ending)

    files=glob.glob(path)

    return files





def read_file(tabbed_file):

    with open(tabbed_file,'rU') as f:

        reader=csv.reader(f,delimiter='\t')

        barcodes=list(reader)
        print barcodes
    return barcodes

def make_dict(barcodes):

    mydict={}

    for rows in barcodes:

        k=rows[1]

        v=rows[0]

        mydict[k]=v

    return mydict

    



def namer(dictionary,files,directory):
    for i in range(len(files)):
        
        for key in dictionary:
            if key in files[i]:

                print '%s is in %s' %(key,files[i])

                location=files[i].index('_')

                newname=dictionary[key]+files[i][location:]

                print 'New filename is %s' %newname

                path=directory+'/'+newname
                with open(files[i],'rU') as f:

                    reader=csv.reader(f)
		    with open(path, 'w') as g:

                        for line in reader:
			    line = str(line) 

                            g.write(line + '\n' )





if __name__ == '__main__':

    directory=sys.argv[1]

    file_ending=sys.argv[2]

    tabbed_file=sys.argv[3]

    files=find_files(directory,file_ending)

    barcodes=read_file(tabbed_file)

    dictionary=make_dict(barcodes)

    namer(dictionary,files,directory)

    

    
