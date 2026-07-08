from icecream import ic
import subprocess

subprocess.run(["cp", "important.txt", "backup.txt"])

ic("Backup completed!")