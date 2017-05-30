from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession

import sys
sys.path.append('/Python/ACI-SDK/corba_files/')

apicUrl = 'https://10.8.254.190'
loginSession = LoginSession(apicUrl, 'admin', 'Cisco12345')
moDir = MoDirectory(loginSession)
moDir.login()
# Use the connected moDir queries and configuration...
moDir.logout()
