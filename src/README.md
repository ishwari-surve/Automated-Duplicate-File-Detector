# Source Code

This directory contains the core implementation of the Automated-Duplicate-File-Detector system.

---

## Contents 

| File | Description |
|---|---|
| `automated_duplicate_file_detector.py` | Main Python script responsible for detecting and removing duplicate files using MD5 hashing. |

---

## Responsibilities

The main script performs the following operations:

- **Scan directories recursively** - Traverses all folders and subfolders using `os.walk()`
- **Generate MD5 checksums** - Creates unique fingerprints for each file using `hashlib.md5()`
- **Detect duplicate files** - Groups files by checksum and identifies duplicates
- **Display duplicate information** - Shows all duplicate files before deletion
- **Remove redundant copies** - Automatically deletes files with " - Copy" pattern in filename
- **Report deleted files** - Displays count of successfully deleted files

---

## File Functions

### **CalculateCheckSum(FileName)**
- Calculates MD5 checksum of a file
- Reads file in 1KB chunks for memory efficiency
- Returns hexadecimal checksum string

### **FindDuplicate(DirectoryName="Data")**
- Scans target directory recursively
- Groups files by their MD5 checksums
- Returns dictionary with checksums as keys and file lists as values

### **DisplayResult(MyDict)**
- Displays all duplicate file groups
- Shows count of duplicates in each group
- No files are deleted at this stage

### **DeleteDuplicate(Path="Data")**
- Identifies files with " - Copy" pattern
- Removes only detected duplicate copies
- Preserves original files
- Reports total deleted count

### **main()**
- Orchestrates the complete duplicate detection and deletion workflow
- Calls FindDuplicate, DisplayResult, and DeleteDuplicate functions

---

## Default Directory

**Default directory:** `"Data"` folder

To scan a different directory, modify the function calls:

```python
FindDuplicate("your_directory_path")
DeleteDuplicate("your_directory_path")
```

---

## Requirements

- **Python Version:** 3.6 or higher
- **Dependencies:** None (uses only standard library)
  - `hashlib` - MD5 checksum generation
  - `os` - Directory and file operations

---

## Execution

Run from project root directory:

```bash
python src/automated_duplicate_file_detector.py
```

---

## Note

This folder contains only the application source code. Refer to the main repository [README.md](../README.md) for:
- Installation instructions
- Project overview and features
- Complete usage guide
- Examples and use cases
- Future enhancements
- License information

---

*Part of Automated-Duplicate-File-Detector project*
