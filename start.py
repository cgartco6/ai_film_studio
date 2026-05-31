import os
import sys
import platform
import subprocess
import webbrowser
from pathlib import Path


ROOT = Path(__file__).parent.resolve()


def print_banner():

    print("=" * 60)
    print("AI FILM STUDIO")
    print("=" * 60)
    print(f"OS: {platform.system()}")
    print(f"Python: {sys.version}")
    print("=" * 60)


def run(cmd):

    print(f"\n[RUN] {' '.join(cmd)}\n")

    result = subprocess.run(cmd)

    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}"
        )


def detect_python():

    return sys.executable


def create_directories():

    dirs = [
        "storage",
        "storage/assets",
        "storage/renders",
        "outputs",
        "models_cache",
        "logs"
    ]

    for d in dirs:
        os.makedirs(d, exist_ok=True)


def create_venv():

    venv_path = ROOT / ".venv"

    if venv_path.exists():
        return

    print("Creating virtual environment...")

    run([
        sys.executable,
        "-m",
        "venv",
        str(venv_path)
    ])


def get_venv_python():

    if platform.system() == "Windows":

        return str(
            ROOT /
            ".venv" /
            "Scripts" /
            "python.exe"
        )

    return str(
        ROOT /
        ".venv" /
        "bin" /
        "python"
    )


def install_requirements():

    py = get_venv_python()

    run([
        py,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip"
    ])

    run([
        py,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])


def start_api():

    py = get_venv_python()

    cmd = [
        py,
        "-m",
        "uvicorn",
        "api.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
        "--reload"
    ]

    print("\nStarting API...\n")

    webbrowser.open(
        "http://127.0.0.1:8000/docs"
    )

    subprocess.call(cmd)


def main():

    print_banner()

    create_directories()

    create_venv()

    install_requirements()

    start_api()


if __name__ == "__main__":
    main()
