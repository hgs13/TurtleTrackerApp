#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Hannah Smith (hgs13@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#create a file object from the file
file_object = open(file_name, 'r')

#read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

#create two empty dictionary objects
date_dict = {}
coord_dict = {}

#interate through all lines in the lineList
for lineString in line_list:
    if lineString[0] in ("#", "u"): continue

    #split the string into a list of data items
    lineData = lineString.split()
    
    #extract items in list into variable
    record_id = lineData[0]
    obs_date= lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ("1", "2", "3"):
       # continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #print the location of Sara if lc is 1, 2, or 3
    if obs_lc in ("1", "2", "3"):
        print(f'Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}.')
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat, obs_lon)
    