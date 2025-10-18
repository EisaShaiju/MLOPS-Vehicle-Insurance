from pathlib import Path


def from_root(*paths: str) -> str:
    """Return an absolute path inside the project root.

    Place this file at the repository root so importing `from_root` works from anywhere
    when running code with the repository root on sys.path (typical when running from repo
    root) or after installing the package in editable mode.

    Usage:
        from from_root import from_root
        log_dir = from_root('logs')

    The function joins any supplied path parts to the repo root and returns a string path.
    """
    root = Path(__file__).resolve().parent
    if paths:
        return str(root.joinpath(*paths))
    return str(root)
