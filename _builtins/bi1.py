import pprint
import logging

data = {'status': 'error', 'details': {'code': 500, 'message': 'Timeout'}}
msg = pprint.pformat(data, indent=4)
logging.error(f"Error: {msg}")