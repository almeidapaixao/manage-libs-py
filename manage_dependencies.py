import os
import subprocess
from datetime import datetime
from pathlib import Path
import sys
import shutil

BASE_DIR = Path(__file__).parent
REQUIREMENTS_IN = BASE_DIR / "requirements.in"
REQUIREMENTS_TXT = BASE_DIR / "requirements.txt"
VENV_DIR = BASE_DIR / ".venv"
PYTHON_EXEC = VENV_DIR / "Scripts/python.exe" if os.name == "nt" else VENV_DIR / "bin/python"

def run(cmd, check=True):
    print(f"\n🔧 Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=check)

def ensure_tools_installed():
    try:
        import piptools
        import pip_audit
    except ImportError:
        print("📦 Installing pip-tools and pip-audit...")
        run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        run([sys.executable, "-m", "pip", "install", "pip-tools", "pip-audit"])

def backup_requirements():
    if REQUIREMENTS_TXT.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BASE_DIR / f"requirements.bak.{timestamp}.txt"
        shutil.copy(REQUIREMENTS_TXT, backup_path)
        print(f"🗃️  Backup created: {backup_path.name}")

def compile_requirements():
    if not REQUIREMENTS_IN.exists():
        print("❌ requirements.in not found.")
        sys.exit(1)
    run(["pip-compile", "--upgrade", "requirements.in"])

def setup_virtualenv():
    if not VENV_DIR.exists():
        print("📁 Creating virtual environment...")
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    print("📥 Installing dependencies...")
    run([str(PYTHON_EXEC), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(PYTHON_EXEC), "-m", "pip", "install", "-r", str(REQUIREMENTS_TXT)])

def run_audit():
    print("\n🔍 Running pip-audit...")
    try:
        run([str(PYTHON_EXEC), "-m", "pip_audit"], check=False)
    except subprocess.CalledProcessError:
        print("⚠️  Vulnerabilities found (see above). Review and fix.")


def main():
    ensure_tools_installed()
    backup_requirements()
    compile_requirements()
    setup_virtualenv()
    run_audit()
    print("\n✅ Dependência gerenciada com sucesso!")

if __name__ == "__main__":
    main()
