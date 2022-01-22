import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.10', 'bilal', 'bilal')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(iosvl2, indent=4))
