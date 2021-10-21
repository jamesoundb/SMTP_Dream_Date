#! /usr/bin/env python3

import os
import glob

tf_files = glob.glob('/Users/jameswurbel/SMTP_Dream_Date/*.tfstate')
dd_files = glob.glob('/Users/jameswurbel/SMTP_Dream_Date/tfanimal.txt')

for f in tf_files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % ('f', 'e.strerror'))

for f in dd_files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % ('f', 'e.strerror'))
