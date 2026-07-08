import subprocess

process = subprocess.Popen(
    ['ls', '-la'],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate()

print(f"Normal output: {stdout}\nErrors (if any): {stderr}\nProcess returned: {process.returncode}")
