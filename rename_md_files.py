import os
import re
import sys


def convert_filename(filename):
    match = re.match(r"^(\d{4})(\d{2})(\d{2})\s.*\.md$", filename)
    if match:
        yyyy, mm, dd = match.groups()
        return f"{yyyy}-{mm}-{dd}.md"
    return None


def main():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)

    for filename in os.listdir(script_dir):
        if not filename.endswith(".md"):
            continue

        new_name = convert_filename(filename)
        if new_name and filename != new_name:
            if not os.path.exists(new_name):
                os.rename(filename, new_name)
                print(f"✅ Renamed: {filename} → {new_name}")
            else:
                print(f"⚠️ Skipped (already exists): {new_name}")

    input("\nProcessing complete. Press Enter to exit.")


if __name__ == "__main__":
    main()
