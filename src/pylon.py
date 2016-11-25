'''
Created on 2016. 11. 24.

@author: Hye-Churn Jang
'''

from binpack import *

if __name__ == '__main__':

    print('''

:::::::::  :::   ::: ::::::::::: :::    :::  ::::::::  ::::    :::   
:+:    :+: :+:   :+:     :+:     :+:    :+: :+:    :+: :+:+:   :+:   
+:+    +:+  +:+ +:+      +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+   
+#++:++#+    +#++:       +#+     +#++:++#++ +#+    +:+ +#+ +:+ +#+   
+#+           +#+        +#+     +#+    +#+ +#+    +#+ +#+  +#+#+#   
#+#           #+#        #+#     #+#    #+# #+#    #+# #+#   #+#+#   
###           ###        ###     ###    ###  ########  ###    ####   
:::        ::::::::: :::     ::: ::::::::::  ::::::::  ::::    ::: 
:+:           :+:    :+:     :+: :+:        :+:    :+: :+:+:   :+: 
+:+           +:+    +:+     +:+ +:+        +:+    +:+ :+:+:+  +:+ 
+#+           +#+    +#+     +:+ +#++:++#   +#+    +:+ +#+ +:+ +#+ 
+#+           +#+     +#+   +#+  +#+        +#+    +#+ +#+  +#+#+# 
#+#           #+#      #+#+#+#   #+#        #+#    #+# #+#   #+#+# 
########## #########     ###     ##########  ########  ###    #### 

Author : Hyechurn Jang
Email : hyjang@cisco.com
''')
    
    print('Imported Packages');
    loadPackageToGlobals___()
    print('')
    
    while True:
        raw_input('Press "Enter" To Execute, "Ctrl + C" To Exit >>')
        try:
            with open('./maincode.py') as fd:
                code = fd.read()
                print('')
                try: exec(code, globals())
                except Exception as e:
                    print('PyLauncher Exception')
                    print(' - Exception Type : %s' % type(e))
                    print(' - Exception Info : %s' % str(e))
                print('')
        except: print('File Not Found : maincode.py\n')
