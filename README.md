# About File Type Identifier

A simple yet powerful Blue Team security tool that identifies real file types by analyzing magic bytes (file signatures) instead of just trusting file extensions. Perfect for security analysis, digital forensics, and malware detection.

##  Features

- Accurate Detection: Uses `python-magic` library (same as Linux `file` command)
- Security Focused: Detects malicious files with fake extensions
- Easy to Use: Interactive interface - just run and enter filename
- Detailed Analysis: Shows MIME types, descriptions, and hex dumps
- Cross-Platform: Works on Windows, Linux, and macOS
- Fast: Analyzes files in milliseconds
- Two Methods**: Uses python-magic library or built-in signature database

##  Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/bakrmohamed/file-type-identifier.git
cd file-type-identifier

# Install python-magic for best accuracy (optional but recommended)
pip install python-magic

```
# Usage

```bash
# Run the program
python file_identifier.py

# When prompted, enter any filename:
Enter filename (or 'quit' to exit): yourfile.ext
```
# Examples
```bash
# Analyze a single file
Enter filename: image.jpg

# Analyze multiple files  
Enter filename: document.pdf archive.zip music.mp3

# Use full paths
Enter filename: /home/user/documents/report.pdf
Enter filename: C:\Users\Name\Downloads\file.exe

# Analyze all files in current directory
Enter filename: *
```
 <h1>What It Detects</h1>

   <h3>Security Threats</h3>

   
-  Disguised Executables: `.exe` files renamed as `.pdf`, `.jpg`, `.doc`
-  Malware Delivery: Files with double extensions like `invoice.pdf.exe`
-  Spoofed Files: Files pretending to be something they're not
- Unknown Binary Files: Unrecognized or suspicious file types


 <h3>File Information</h3> 
 
- Real File Type: Actual format determined by magic bytes
- MIME Type: Internet media type (e.g., image/jpeg)
- File Description: Detailed information about the file
- Extension Match: Whether file extension matches actual content
- Security Status: Flag suspicious files with warnings

## Example Output
## Normal File Analysis

---

## File Analysis Results

### File Information
| Field     | Value           |
|-----------|-----------------|
| Name      | photo.jpg       |
| Size      | 1,245,678 bytes |
| Extension | .jpg            |

---

### Identification Results
| Field       | Value                                 |
|-------------|---------------------------------------|
| Type        | JPEG Image                            |
| MIME Type   | image/jpeg                            |
| Description | JPEG image data, JFIF standard 1.01   |
| Method      | python-magic                          |
| Confidence  | High                                  |

---

### Validation
| Status | Details                               |
|--------|----------------------------------------|
| OK     | File extension matches detected type   |

---

### First 32 Bytes (HEX)
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 00 00 01

## Suspicious File Detection

---

## File Analysis Results

### File Information
| Field       | Value            |
|-------------|------------------|
| Name        | invoice.pdf.exe  |
| Size        | 2,500,000 bytes  |
| Extension   | .exe             |

---

### Identification Results
| Field      | Value                                                |
|------------|------------------------------------------------------|
| Type       | Windows Executable                                   |
| MIME Type  | application/x-msdownload                             |
| Description| PE32 executable (GUI), Intel 80386, for MS Windows   |

---

### Security Alert
| Issue                     | Details                      |
|---------------------------|------------------------------|
| Extension mismatch        | Yes                          |
| Actual extension          | .exe                         |
| File name suggests        | .pdf                         |
| Risk                      | This file may be malicious   |

---

### First 32 Bytes (HEX)
4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00

## Supported File Types

### With python-magic (1000+ types)

| Category     | Types |
|--------------|-------|
| Images       | JPEG, PNG, GIF, BMP, WebP, TIFF, ICO, SVG |
| Documents    | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, RTF, ODT |
| Archives     | ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ |
| Media        | MP3, MP4, AVI, MKV, FLV, WAV, OGG, WEBM |
| Executables  | EXE, DLL, SO, ELF, MSI, APP, DMG |
| Text         | TXT, HTML, CSS, JS, JSON, XML, CSV, YAML |
| Database     | SQLite, MySQL dumps, PostgreSQL |
| System       | ISO, IMG, VHD, VMDK |

---

### Without python-magic (20+ types)

| Category | Types |
|----------|--------|
| Images   | JPEG, PNG, GIF, BMP |
| Documents| PDF, DOC |
| Archives | ZIP, RAR, 7Z |
| Media    | MP3, MP4 |
| Executables | EXE |
| Text     | UTF-8/16 text files |

## Installation Guide

---

## Basic Installation

### Method 1: Just download and run
```bash
python file_identifier.py
```

---

## Full Installation with python-magic

### Windows
```cmd
pip install python-magic-bin
python file_identifier.py
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install libmagic1
pip install python-magic
python3 file_identifier.py
```

### macOS
```bash
brew install libmagic
pip install python-magic
python3 file_identifier.py
```

### Linux (Fedora/CentOS/RHEL)
```bash
sudo dnf install file-libs
pip install python-magic
python3 file_identifier.py
```

## Common Use Cases

1. Detecting Malware
```bash
# Analyze a suspicious file
Enter filename: invoice.pdf.exe

# Output: Detected as EXE, not PDF - potential malware!
```

2. Verifying Downloads
```bash
# Check downloaded files
Enter filename: downloaded_file.zip

# Verify it's actually a ZIP archive
```

3. Forensic Analysis
```bash
# Analyze multiple files from an investigation
Enter filename: evidence1.bin evidence2.dat evidence3.unknown
```

4. Security Audits
```bash
# Check all files in a directory
Enter filename: *
```

5. Development Testing
```bash
# Test file upload functionality
Enter filename: test_upload.jpg

# Verify it's actually an image
```

---

## Security Features

1. Fake Extension Detection
```text
File: trojan.jpg.exe
Detection: EXE file pretending to be JPG
Action: Security warning with details
```

2. Double Extension Warning
```text
File: document.pdf.exe
Detection: Two extensions, likely malicious
Action: Highlight and warn user
```

3. Unknown File Alerts
```text
File: unknown.bin
Detection: No known signature
Action: Mark as suspicious, show hex dump
```

4. Size Analysis
```text
File: tiny.exe (50 bytes)
Detection: Too small for valid EXE
Action: Warning about possible stub file
```

