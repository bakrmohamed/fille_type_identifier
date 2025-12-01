#  File Type Identifier using Magic Bytes


A simple yet powerful Blue Team security tool that identifies real file types by analyzing magic bytes (file signatures) instead of just trusting file extensions. Perfect for security analysis, digital forensics, and malware detection.

##  Features

- ** Accurate Detection**: Uses `python-magic` library (same as Linux `file` command)
- ** Security Focused**: Detects malicious files with fake extensions
- ** Easy to Use**: Interactive interface - just run and enter filename
- ** Detailed Analysis**: Shows MIME types, descriptions, and hex dumps
- ** Cross-Platform**: Works on Windows, Linux, and macOS
- ** Fast**: Analyzes files in milliseconds
- ** Two Methods**: Uses python-magic library or built-in signature database

##  Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/bakrmohamed/file-type-identifier.git
cd file-type-identifier

# Install python-magic for best accuracy (optional but recommended)
pip install python-magic

## Usage
bash

# Run the program
python file_identifier.py

# When prompted, enter any filename:
Enter filename (or 'quit' to exit): yourfile.ext


##  Examples

# Analyze a single file
Enter filename: image.jpg

# Analyze multiple files
Enter filename: document.pdf archive.zip music.mp3

# Use full paths
Enter filename: /home/user/documents/report.pdf
Enter filename: C:\Users\Name\Downloads\file.exe

# Analyze all files in current directory
Enter filename: *

What It Detects
Security Threats

    Disguised Executables: .exe files renamed as .pdf, .jpg, .doc

    Malware Delivery: Files with double extensions like invoice.pdf.exe

    Spoofed Files: Files pretending to be something they're not

    Unknown Binary Files: Unrecognized or suspicious file types

File Information

    Real File Type: Actual format determined by magic bytes

    MIME Type: Internet media type (e.g., image/jpeg)

    File Description: Detailed information about the file

    Extension Match: Whether file extension matches actual content

    Security Status: Flag suspicious files with warnings



Example Output

Normal File Analysis

========================================
 FILE ANALYSIS RESULTS
========================================

 File Information:
   Name:      photo.jpg
   Size:      1,245,678 bytes
   Modified:  2024-01-15 14:30:25
   Extension: .jpg

 Identification Results:
   Type:        JPEG Image
   MIME Type:   image/jpeg
   Description: JPEG image data, JFIF standard 1.01
   Method:      python-magic
   Confidence:  High

 Validation:
   File extension matches detected type

 First 32 bytes (HEX):
   FF D8 FF E0 00 10 4A 46 49 46 00 01 01 00 00 01
========================================

Supported File Types
With python-magic (1000+ types):

    Images: JPEG, PNG, GIF, BMP, WebP, TIFF, ICO, SVG

    Documents: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, RTF, ODT

    Archives: ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ

    Media: MP3, MP4, AVI, MKV, FLV, WAV, OGG, WEBM

    Executables: EXE, DLL, SO, ELF, MSI, APP, DMG

    Text: TXT, HTML, CSS, JS, JSON, XML, CSV, YAML

    Database: SQLite, MySQL dumps, PostgreSQL

    System: ISO, IMG, VHD, VMDK

Without python-magic (20+ types):

    JPEG, PNG, GIF, BMP

    PDF, DOC

    ZIP, RAR, 7Z

    MP3, MP4

    EXE

    UTF-8/16 text files




