import subprocess

commands = [
'echo -e "\033[32m"',
'PS1="🕹️ GAME> "',
'git pull',
'clear',
'python users.py'
]

for cmd in commands:
    subprocess.run(cmd, shell=True)
