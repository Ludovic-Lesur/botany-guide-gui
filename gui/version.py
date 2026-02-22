"""
* version.py
*
*  Created on: 22 feb. 2026
*      Author: Ludo & Copilot
"""

import subprocess
import argparse

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

### VERSION classes ###

@dataclass(frozen=True)
class GitVersion:
    
    tag: str
    commits_since_tag: str
    commit_hash: str
    dirty: bool

    def format(self) -> str:
        version = f"{self.tag}.{self.commits_since_tag}"
        if self.dirty:
            version += ".dev"
        version += f" - {self.commit_hash}"
        return version

### VERSION functions ###

def _sh(args: Iterable[str]) -> str:
    return subprocess.check_output(list(args), stderr=subprocess.DEVNULL, text=True).strip()

def get_git_version(tag_pattern: str = "sw*") -> GitVersion:
    tag = _sh(["git", "describe", "--tags", "--match", tag_pattern, "--abbrev=0"])
    commits_since_tag = _sh(["git", "rev-list", "--count", f"{tag}..HEAD"])
    commit_hash = _sh(["git", "rev-parse", "--short", "HEAD"])
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    dirty = bool(status.stdout.strip())
    return GitVersion(tag=tag, commits_since_tag=commits_since_tag, commit_hash=commit_hash, dirty=dirty)

def write_build_version_py(path: str | Path, version_string: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'VERSION = "{version_string}"\n', encoding="utf-8")

def main() -> int:
    parser = argparse.ArgumentParser(description="Compute and optionally embed Git version.")
    parser.add_argument("--tag-pattern", default="sw*", help="Git tag pattern (default: sw*)")
    parser.add_argument("--write", default="", help="Write version file at this path")
    args = parser.parse_args()
    gv = get_git_version(tag_pattern=args.tag_pattern)
    version = gv.format()
    print(version)
    if args.write:
        write_build_version_py(args.write, version)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())