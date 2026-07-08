import pprint

deep_data = {'level1': {'level2': {'level3': {'level4': 'secret'}}}}
pprint.pprint(deep_data, depth=2)
