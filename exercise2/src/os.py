import importlib.metadata
import sys as s

pandas_version = importlib.metadata.version("pandas")
print(f"pandas == {pandas_version}")

matplotlib_version = importlib.metadata.version("matplotlib")
print(f"matplotlib == {matplotlib_version}")

print(f"Python version: {s.version.split()[0]}")
