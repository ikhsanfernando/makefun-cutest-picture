"""Entry for the make.fun competition.

Writes entry.png to the output directory.
"""
#!/usr/bin/env python3
import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output_dir / source.name)


if __name__ == "__main__":
    main()
