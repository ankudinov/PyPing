import PyPing

ip_list = [
    '8.8.8.8',
    '2.2.2.2',
    '3.3.3.3',
    '127.0.0.1',
    '72.163.4.161',
    '192.30.252.128',
]

reachable, unreachable = PyPing.check_if_pingable(ip_list)

print('Reachable:')
for ip in reachable:
    print(ip)

print()
print('Unreachable:')
for ip in unreachable:
    print(ip)
