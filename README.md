# Markdown Renamer

This is a simple Python script designed to help you migrate exported Notion daily journal entries into [Obsidian](https://obsidian.md)'s **Daily Notes** format.
Notion often exports journal files with filenames like:
```
20230710 abcdef123456.md
```
This script renames them to Obsidian's expected Daily Notes format:
```
2023-07-10.md
```
## 📝 Use Case
If you've exported your diary or daily notes from Notion as markdown files and want to import them into Obsidian, you may find that Notion adds a long string after the date. Obsidian's Daily Notes plugin expects filenames like `YYYY-MM-DD.md`.
This script automates that filename conversion for **batch processing**.

## 📁 What It Does

- Scans all `.md` files in the directory where the script is located.
- Renames any file that matches the pattern `YYYYMMDD somehash.md` to `YYYY-MM-DD.md`.
- Skips files that don't match the pattern.
- Prevents overwriting if the target filename already exists.

## 🖥️ How to Use (macOS)

1. Place the `rename_md_files.py` file into the folder containing your `.md` files.

2. Open **Terminal** and navigate to the folder:
    ```bash
    cd /path/to/your/folder
    ```

3. Run the script:
    ```bash
    python3 rename_md_files.py
    ```
    Or, if you made it executable:
    ```bash
    ./rename_md_files.py
    ```

4. The script will show which files were renamed.

🛠 Example
Before:
```
20230710 c2d480aa3dd84a13b84902fbf954ee48.md
20230711 abcdefabcdefabcdefabcdefabcdefab.md
```
After:

```
2023-07-10.md
2023-07-11.md
```

⚠️ Notes
Only `.md` files with the correct pattern are renamed.
If `2023-07-10.md` already exists, it will not be overwritten.
Make sure your filenames follow the `YYYYMMDD somestring.md` format.

