#!/usr/bin/python
"""
it is used to conut number of multispheres inside the system, count by the number of lines of post file
run as ' python Count_particle_number_inside.py dump*.local'
dump*.local are the post files

"""


try:
    import numpy as np
    oldnumeric = False
except:
    import Numeric as np
    oldnumeric = True

import sys, os
import glob

filename = sys.argv[1:]

inputpath = os.path.abspath(filename[0])
inputdir = os.path.split(inputpath)[0]

# create a sub-directory for the output .vtu files
outputdir = os.path.join(inputdir,'number_of_particles')

try:
    os.mkdir(outputdir)
except:
    pass

#create a dictionary to sort the filename list
filenamedict={}
for each in filename:
    fileserialnum=int(each.split('.')[0][4:])
    filenamedict[fileserialnum]=each
ks=list(filenamedict.keys())
ks.sort()
filename=[]
for key in ks:
    filename.append(filenamedict[key])   #regenerate a sequential filename list

fileLineNumber=[]
   
for fname in filename:
    if not os.path.isfile(fname):
        sys.exit('File ' + fname + ' does not exist!')

    splitname = fname.split('.')

    if len(splitname) == 2 and splitname[0].lower() == 'dump':
        fileprefix = splitname[1]
    else:
        fileprefix = splitname[0]

    lineCount=0
    thefile=open(fname,'rb')

    while True:
	buffer=thefile.read(1024*8192)
	if not buffer:
	    break
	lineCount+=buffer.count('\n')
    thefile.close()
    print "timestep handling is", splitname[0][4:], ", system contains ", lineCount-9, "particles" 

    fileLineNumber.append([lineCount-9,splitname[0][4:]])
    
# write unique contact num information to a txt files
filePositionAndName=os.path.join(outputdir,'number_of_particles')
f = open(filePositionAndName,'w')
f.write('timestep number'+'\r\n')
for each in fileLineNumber:
	f.write(str(each[1])+' '+str(each[0])+'\r\n')
f.close()      







