from google.appengine.ext import vendor

vendor.add("lib")

import os
import sys


# On windows we will get an error about msvcrt not being installed. easy fix by overriding some system variables
if os.name == 'nt':
    os.name = None
    sys.platform = ''
