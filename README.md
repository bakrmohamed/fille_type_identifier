#  File Type Identifier using Magic Bytes


A simple yet powerful Blue Team security tool that identifies real file types by analyzing magic bytes (file signatures) instead of just trusting file extensions. Perfect for security analysis, digital forensics, and malware detection.

## ✨ Features

- **🔍 Accurate Detection**: Uses `python-magic` library (same as Linux `file` command)
- **🛡️ Security Focused**: Detects malicious files with fake extensions
- **🚀 Easy to Use**: Interactive interface - just run and enter filename
- **📊 Detailed Analysis**: Shows MIME types, descriptions, and hex dumps
- **🌐 Cross-Platform**: Works on Windows, Linux, and macOS
- **⚡ Fast**: Analyzes files in milliseconds
- **🔧 Two Methods**: Uses python-magic library or built-in signature database

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/bakrmohamed/file-type-identifier.git
cd file-type-identifier

# Install python-magic for best accuracy (optional but recommended)
pip install python-magic
