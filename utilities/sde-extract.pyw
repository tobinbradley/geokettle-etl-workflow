# Drag data kicking and screaming out of SDE.
# Arg 1: The sde connection name, as found in D:/etl/sde_connections
# Arc 2: The sde file name, like user.layer

import arcpy, os, glob, sys

# get command line arguments and make into file in and out
db = sys.argv[1]
fc = sys.argv[2]
fin = "D:/etl/sde_connections/" + db + "/" + fc
fout = fc.split(".")[-1] + ".shp"

# remove shapefile if it exists
path = "D:/etl/shapefiles/" + fc.split(".")[-1] + ".*"
for fname in glob.glob(path):
    os.remove(fname)

# extract data
arcpy.FeatureClassToFeatureClass_conversion(in_features=fin, out_path="D:/etl/shapefiles/", out_name=fout)  

