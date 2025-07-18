# Markdown Renamer

This is a simple Python script that renames `.md` files with names like:
```
20230710 abcdef123456.md
```
to:
```
2023-07-10.md
```

## 📁 What It Does

- Scans all `.md` files in the directory where the script is located.
- Renames any file that matches the pattern `YYYYMMDD somehash.md` to `YYYY-MM-DD.md`.
- Skips files that don't match the pattern.
- Prevents overwriting if the target filename already exists.

## 🖥️ How to Use (macOS)

1. Place the `rename.py` file into the folder containing your `.md` files.

2. Open **Terminal** and navigate to the folder:
    ```bash
    cd /path/to/your/folder
    ```

3. Run the script:
    ```bash
    python3 rename.py
    ```
    Or, if you made it executable:
    ```bash
    ./rename.py
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
2023-07-10.md
2023-07-11.md
```

⚠️ Notes
Only `.md` files with the correct pattern are renamed.
If `2023-07-10.md` already exists, it will not be overwritten.
Make sure your filenames follow the `YYYYMMDD somestring.md` format.

