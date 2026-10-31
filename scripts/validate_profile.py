"""Validate local assets and core presentation requirements of the GitHub profile."""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SVG_NAMESPACE = "{http://www.w3.org/2000/svg}"


def main() -> int:
    errors: list[str] = []
    content = README.read_text(encoding="utf-8")

    images = re.findall(r"<img\b[^>]*>", content, flags=re.IGNORECASE)
    if not images:
        errors.append("README.md has no image elements.")

    for tag in images:
        alt = re.search(r'\balt\s*=\s*"([^"]*)"', tag, flags=re.IGNORECASE)
        src = re.search(r'\bsrc\s*=\s*"([^"]*)"', tag, flags=re.IGNORECASE)
        if not alt or not alt.group(1).strip():
            errors.append(f"Missing image alt text: {tag[:100]}")
        if not src:
            errors.append(f"Missing image source: {tag[:100]}")
            continue
        value = src.group(1)
        if value.startswith("./"):
            target = ROOT / value[2:]
            if not target.is_file():
                errors.append(f"Missing local image: {value}")

    svg_files = sorted((ROOT / "assets").glob("*.svg"))
    if len(svg_files) < 3:
        errors.append("Expected at least three profile SVG assets.")

    for path in svg_files:
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            if root.tag != f"{SVG_NAMESPACE}svg":
                errors.append(f"{path.name}: SVG namespace is missing.")
            if not root.attrib.get("viewBox"):
                errors.append(f"{path.name}: viewBox is missing.")
            if root.find(f"{SVG_NAMESPACE}title") is None:
                errors.append(f"{path.name}: accessible title is missing.")
            if root.find(f"{SVG_NAMESPACE}desc") is None:
                errors.append(f"{path.name}: accessible description is missing.")
        except ET.ParseError as error:
            errors.append(f"{path.name}: malformed SVG XML: {error}")

    if errors:
        print("Profile validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Profile validation passed: {len(images)} images, {len(svg_files)} SVG assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
