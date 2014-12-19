##############################################################
##
##  Weekly postgres ETL jobs - SDE data
##
##############################################################

import os

geokettlepath = "D:\\geokettle"
scriptpath = "D:\\etl\\"

# Change to geokettle directory
os.chdir(geokettlepath)

# roads
os.system("kitchen.bat /file:" + scriptpath + "sde-monthly.kjb /level:Basic /logfile:" + scriptpath + "sde-monthly.kjb.log")

