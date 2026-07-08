from pprint import pprint
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
pprint(result.stdout, indent=4)