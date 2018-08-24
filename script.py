############################################
#Author Maaz Kabir
############################################
#Script to Download and Setup Python Dependencies Stored in Dependencies.JSON file in pip
############################################

import json
from setuptools.command import easy_install
import subprocess

#Importing the json file
f = open('dependency.json','r')

#Converting JSON file to  Dictionary
r = json.loads(f.read())

#Initializing Passed and Failed Dictionaries to Hold PAckage Names and Versions
passed={ }
failed={ }

############################################################
#This is another way of installing dependencies using the easy_install python module 
def install_with_easyinstall(package):
   for key, value in package.items(): 
      easy_install.main([key+'=='+value])

#Uncomment the below line to execute the above easy_install script
#install_with_easyinstall(r['Dependencies'])
#############################################################


###### PIP Install Script ######

#Iterating through all the dependencies key=PackageName and value=Version

for key, value in r['Dependencies'].items():
#Using a shell to install this using pip
#Using try so that the process continues
 try:
    output = subprocess.run("pip install {0}=={1} ".format(key,value), shell=True, stderr=subprocess.PIPE,stdout=subprocess.PIPE, 
              universal_newlines=True)
    #printing script output
    print(output.stdout,flush=True)
    print(output.stderr,flush=True)
    #Checking if the output contains any Errors and Still Continuing the process
    if output.stderr!='':
       failed[key]=value
    else:
       passed[key]=value
 except Exception as e:
      pass

#Failed Packages
if failed!={}:
   print("The Following Packages Failed To Install \n {0}".format(failed))
#Passed Packages
if passed!={}:
   print("The Following Packages Were Successfully Installed \n {0}".format(passed))

################################################