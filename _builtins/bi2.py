import pprint

config = {'database': {'host': 'localhost', 'port': 5432}, 'debug': True, 'allowed_hosts': ['*']}
pprint.pprint(config, indent=2)