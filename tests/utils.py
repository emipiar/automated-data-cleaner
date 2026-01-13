import subprocess
import sys


def run_cli(args):
    """
    Helper to run the CLI as a subprocess.
    Returns CompletedProcess.
    """
    return subprocess.run(
        [sys.executable, "-m", "src.cli"] + args,
        capture_output=True,
        text=True,
    )
