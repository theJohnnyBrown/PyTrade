# Decleration of constant variables.
#

import sys

try:
    import config
except:
    print "config.py is missing. You may create it by copying config-default.py as config.py. New config.py should be edited as well."
    sys.exit(-1)

from os.path import join


#################################################################
# reading variables from config.py
#################################################################
try:
    base_dir = config.BASE_DIR
except AttributeError:
    print "'BASE_DIR' needs to be defined in config.py"
    sys.exit(-1)

try:
    data_dir = config.DATA_DIR
    
except AttributeError:
    print "'DATA_DIR' needs to be defined in config.py"
    sys.exit(-1)


