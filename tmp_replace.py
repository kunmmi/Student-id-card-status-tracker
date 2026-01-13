from pathlib import Path

replacements = [
    ("LASU ID Card Tracker", "University of Ibadan ID Card Tracker"),
    ("LASU ID card", "University of Ibadan ID card"),
    ("LASU", "University of Ibadan"),
]

count = 0
for path in Path(".").rglob("*"):
    if path.is_file() and path.suffix not in {".pyc", ".pyo"}:
        if path.name == "tmp_replace.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        original = text
        for old, new in replacements:
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            count += 1

print("Updated", count, "files")

