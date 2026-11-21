"""Runs every solution file; each file asserts its own test cases."""
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
files = sorted(p for p in root.rglob("*.py")
               if p.name not in ("run_all.py", "_TEMPLATE.py"))
failed = 0
for f in files:
    r = subprocess.run([sys.executable, str(f)], capture_output=True, text=True)
    ok = r.returncode == 0
    failed += not ok
    print(("PASS" if ok else "FAIL"), f.relative_to(root))
    if not ok:
        print(r.stderr)
print(f"\n{len(files) - failed}/{len(files)} passed")
sys.exit(1 if failed else 0)
