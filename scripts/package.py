#!/usr/bin/env python3
"""Package the existing applet without a compilation step."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent.parent
uuid = "taskbar-menu@cornelishaferkamp"
source = root / "src" / uuid
metadata = json.loads((source / "metadata.json").read_text())
assert metadata["uuid"] == uuid
output = root / "dist" / f"taskbar-menu-{metadata['version']}.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob("*")):
        if path.is_file():
            archive.write(path, Path(uuid) / path.relative_to(source))
    archive.write(root / "LICENSE", Path(uuid) / "LICENSE")
    archive.writestr("README.md", (root / "README.md").read_text().replace("src/taskbar-menu@cornelishaferkamp/icon.png", "taskbar-menu@cornelishaferkamp/icon.png"))
    archive.write(root / "docs" / "original-overview.png", "docs/original-overview.png")
    archive.write(root / "LICENSE", "LICENSE")
print(output)
