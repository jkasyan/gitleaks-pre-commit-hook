#!/usr/bin/python3

import subprocess
import sys
import platform
from pathlib import Path

home = str(Path.home())
op_system = platform.system()
git_url = "https://github.com/gitleaks/gitleaks.git"
gitleaks_folder = ""
move_cmd = ""

if op_system == "Windows":
    gitleaks_folder = home + "\\Downloads\\gitleaks"
    move_cmd = f"move {gitleaks_folder}\\gitleaks.exe \"C:\\Windows\\System32\\gitleaks.exe\""
else:
    gitleaks_folder = home + "/Downloads/gitleaks"
    f"mv {gitleaks_folder}/gitleaks.exe /usr/local/bin"

print("os :", op_system)


def gitleaks_enabled():
    """Determine if the pre-commit hook for gitleaks is enabled."""
    out = subprocess.getoutput("git config --bool hooks.gitleaks")
    if out == "false":
        return False
    return True


def is_installed():
    return run_subprocess("gitleaks --version").returncode == 0


def run_subprocess(command):
    return subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )


if not gitleaks_enabled():
    print("gitleaks disabled")
    sys.exit(0)


if not is_installed():
    print("gitleaks is not installed")
    commands = [
        f"git clone {git_url} {gitleaks_folder}",
        f"make -C {gitleaks_folder} build",
        move_cmd,
        f"rm -rf {gitleaks_folder}"
    ]

    for c in commands:
        res = run_subprocess(c)
        if res.returncode != 0:
            print("error: ", res.stderr, ", for cmd: ", c)
            sys.exit(res.returncode)
    print("successfully installed gitleaks")

res = run_subprocess("gitleaks detect --report-path=leaks-report.json --report-format=json")
print(res.stderr)
if res.returncode != 0:
    sys.exit(res.returncode)
