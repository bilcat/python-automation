import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.10', 'bilal', 'bilal')
iosvl2.open()

ios_output_macTable = iosvl2.ping('google.com')
print(json.dumps(ios_output_macTable, indent=4))
