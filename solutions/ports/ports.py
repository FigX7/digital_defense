import itertools

def intervals_extract(iterable):

    iterable = sorted(set(iterable))
    for key, group in itertools.groupby(enumerate(iterable),
        lambda t: t[1] - t[0]):
        group = list(group)
        yield [group[0][1], group[-1][1]]



def print_ports(include_ports, exclude_ports):
    ports_result = []
    for inc_port in include_ports:
        for exc_port in exclude_ports:
            if inc_port[0] <= exc_port[0] <= inc_port[1]:
                inc_range = list(range(inc_port[0], inc_port[1]+1))
                exc_range = list(range(exc_port[0], exc_port[1]+1))

                set_difference = set(inc_range) - set(exc_range)
                list_difference = list(set_difference)
                ports_result.append(list_difference)
            else:
                ports_result.append(list(inc_port))

    ports_result = set(item for pair in ports_result for item in pair)
    ports_result = sorted(ports_result)

    for data in intervals_extract(ports_result):
        print(data)

# CASE:1 PASS

include_ports = [[80, 80], [22, 23], [8000, 9000]]
exclude_ports = [[8080, 8080], [1024, 1024]]

print('CASE -1')
print_ports(include_ports, exclude_ports)
print('-----------------------------------')

# CASE:2 PASS

include_ports = [[8000, 9000], [80, 80], [22, 23]]
exclude_ports = [[1024, 1024], [8080, 8080]]

print('CASE -2')
print_ports(include_ports, exclude_ports)
print('-----------------------------------')

# CASE:3 Fail

include_ports = [[1, 65535]]
exclude_ports = [[1000, 2000], [500, 2500]]

print('CASE -3')
print_ports(include_ports, exclude_ports)
print('-----------------------------------')

# CASE:4 Fail

include_ports = [[1,1], [3, 65535], [2, 2]]
exclude_ports = [[1000, 2000], [500, 2500]]

print('CASE -4')
print_ports(include_ports, exclude_ports)
print('-----------------------------------')

# CASE:5 Fail

include_ports = []
exclude_ports = [[8080, 8080]]


print('CASE -5')
print_ports(include_ports, exclude_ports)
print('-----------------------------------')