import sys
import pkg_resources
import base64

path=pkg_resources.resource_filename('v2ray_util','')
sys.path.insert(0, path)
from util_core.loader import Loader
profile=Loader().profile

allLinks=''
for group in profile.group_list:
    for node in group.node_list:
        str=node.link(group.ip, int(group.port), group.tls)
        str=str[5:-4]
        allLinks+=str+'\n'

code=base64.b64encode(allLinks.encode('utf-8'))
code=code.decode('utf-8')
print(code)


