'''
Created on 2016. 11. 24.

@author: Hye-Churn Jang
'''

import os
import re

if __name__ == '__main__':
    if os.path.exists('./src/binpack.py'): os.remove('./src/binpack.py')
    try:
        with open('./packages.txt') as fd: packages = fd.readlines()
        span = []
        for p in packages: span.append(re.match('(?P<package>\w+)', p).group('package'))
        packages = span
        with open('./src/binpack.py', 'w') as fd:
            for p in packages: fd.write('import %s\n' % p)
            fd.write('\ndef PackageList__():\n')
            for p in packages: fd.write("\tprint(' - %s')\n" % p)
    except Exception as e:
        print 'Build Failed with', type(e), str(e)
        exit(1)
    if os.system('pyinstaller --onefile --console ./src/pylon.py') == 0: print '\nDone!'
    else: print '\nFailed!'
    