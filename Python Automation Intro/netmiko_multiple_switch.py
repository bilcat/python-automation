from netmiko import ConnectHandler

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'bilal',
    'password': 'bilal'
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.22',
    'username': 'bilal',
    'password': 'bilal'
}
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.23',
    'username': 'bilal',
    'password': 'bilal'
}

all_devices = [iosv_l2_s2, iosv_l2_s3, iosv_l2_s4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range(2, 21):
        print("Creating Vlan " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
