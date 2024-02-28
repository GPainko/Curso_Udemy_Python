import subprocess
import sys

print(sys.platform)

cmd = ['ls -lah /'] #['ping','127.0.0.1' ,'-c','4']
encodig = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping','127.0.0.1']
    encodig = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True,encoding=encodig,
    shell=True,
)

print()
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)