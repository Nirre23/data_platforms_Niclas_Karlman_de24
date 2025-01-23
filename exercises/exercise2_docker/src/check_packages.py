import subprocess
import sys

# Skriv ut Python-versionen
print("Python version:", sys.version)

# Skriv ut installerade paket och deras versioner
try:
    installed_packages = subprocess.run(
        [sys.executable, "-m", "pip", "list"],
        text=True,
        capture_output=True,
        check=True
    )
    print(installed_packages.stdout)
except subprocess.CalledProcessError as e:
    print("Error occurred while fetching installed packages:", e)
