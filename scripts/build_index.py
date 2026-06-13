#!/usr/bin/env python3
"""Build registry/index.json from styles/*/style.yaml.

Flattens every style entry into a single file an API can serve directly.
Run from anywhere: python scripts/build_index.py
"""
import json
import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
STYLES = ROOT / "styles"
OUT = ROOT / "registry" / "index.json"

SUMMARY_FIELDS = (
    "id", "name", "family", "status", "version",
    "density_rating", "default_aspect_ratio",
    "depth_mechanism", "best_for", "tags",
)


def main() -> None:
    styles = []
    for path in sorted(STYLES.glob("*/style.yaml")):
        data = yaml.safe_load(path.read_text())
        styles.append({k: data.get(k) for k in SUMMARY_FIELDS})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"version": "1.0.0", "styles": styles}, indent=2) + "\n")
    print(f"Wrote {len(styles)} styles to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
