#!/usr/bin/env python3
"""
File Type Identifier - Interactive Version
Just run the program and enter filenames
"""

import os
import sys
import platform
from datetime import datetime

# Try to import magic library
try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False
    print("  'python-magic' library not found. Using built-in signatures.")
    print("   To install: pip install python-magic (or python-magic-bin for Windows)")

# Built-in signatures database (fallback if magic library not available)
FILE_SIGNATURES = {
    # Images
    b'\xff\xd8\xff': {'name': 'JPEG', 'ext': '.jpg', 'mime': 'image/jpeg'},
    b'\x89PNG\r\n\x1a\n': {'name': 'PNG', 'ext': '.png', 'mime': 'image/png'},
    b'GIF87a': {'name': 'GIF87a', 'ext': '.gif', 'mime': 'image/gif'},
    b'GIF89a': {'name': 'GIF89a', 'ext': '.gif', 'mime': 'image/gif'},
    b'BM': {'name': 'BMP', 'ext': '.bmp', 'mime': 'image/bmp'},
    
    # Documents
    b'%PDF': {'name': 'PDF', 'ext': '.pdf', 'mime': 'application/pdf'},
    b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1': {'name': 'DOC', 'ext': '.doc', 'mime': 'application/msword'},
    
    # Archives
    b'PK\x03\x04': {'name': 'ZIP', 'ext': '.zip', 'mime': 'application/zip'},
    b'Rar!\x1a\x07\x00': {'name': 'RAR', 'ext': '.rar', 'mime': 'application/x-rar-compressed'},
    b'7z\xbc\xaf\x27\x1c': {'name': '7Z', 'ext': '.7z', 'mime': 'application/x-7z-compressed'},
    
    # Media
    b'\xff\xfb': {'name': 'MP3', 'ext': '.mp3', 'mime': 'audio/mpeg'},
    b'\x00\x00\x00\x1cftyp': {'name': 'MP4', 'ext': '.mp4', 'mime': 'video/mp4'},
    
    # Executables
    b'MZ': {'name': 'EXE', 'ext': '.exe', 'mime': 'application/x-msdownload'},
    
    # Text files with BOM
    b'\xef\xbb\xbf': {'name': 'UTF-8 BOM', 'ext': '.txt', 'mime': 'text/plain'},
    b'\xff\xfe': {'name': 'UTF-16 LE', 'ext': '.txt', 'mime': 'text/plain'},
    b'\xfe\xff': {'name': 'UTF-16 BE', 'ext': '.txt', 'mime': 'text/plain'},
}

class FileIdentifier:
    """Main class for file identification"""
    
    def __init__(self):
        """Initialize file identifier with available method"""
        self.using_magic = MAGIC_AVAILABLE
        
        if MAGIC_AVAILABLE:
            try:
                self.magic_mime = magic.Magic(mime=True)
                self.magic_desc = magic.Magic()
            except Exception as e:
                print(f"  Error initializing magic: {e}")
                self.using_magic = False
    
    def read_file_header(self, filepath, bytes_to_read=64):
        """Read first bytes of a file"""
        try:
            with open(filepath, 'rb') as f:
                return f.read(bytes_to_read)
        except Exception as e:
            return None
    
    def identify_with_magic(self, filepath):
        """Identify file using python-magic library"""
        try:
            mime_type = self.magic_mime.from_file(filepath)
            description = self.magic_desc.from_file(filepath)
            
            # Extract file type from description
            file_type = self._extract_type_from_desc(description)
            
            return {
                'type': file_type,
                'mime': mime_type,
                'description': description,
                'method': 'magic-library',
                'confidence': 'high'
            }
        except Exception as e:
            return None
    
    def identify_with_signatures(self, filepath):
        """Identify file using built-in signatures"""
        header = self.read_file_header(filepath)
        if not header:
            return None
        
        # Check against all signatures
        for signature, info in FILE_SIGNATURES.items():
            if header.startswith(signature):
                return {
                    'type': info['name'],
                    'mime': info['mime'],
                    'extension': info['ext'],
                    'method': 'signature-db',
                    'confidence': 'medium'
                }
        
        # Try to guess from first bytes
        if header[:2] in [b'MZ', b'ZM']:
            return {'type': 'EXE', 'mime': 'application/x-msdownload', 'method': 'heuristic', 'confidence': 'low'}
        elif header[:4] == b'RIFF':
            return {'type': 'RIFF', 'mime': 'application/x-riff', 'method': 'heuristic', 'confidence': 'low'}
        
        return None
    
    def _extract_type_from_desc(self, description):
        """Extract file type from magic description"""
        desc_lower = description.lower()
        
        if 'jpeg' in desc_lower or 'jpg' in desc_lower:
            return 'JPEG'
        elif 'png' in desc_lower:
            return 'PNG'
        elif 'gif' in desc_lower:
            return 'GIF'
        elif 'pdf' in desc_lower:
            return 'PDF'
        elif 'zip' in desc_lower:
            return 'ZIP'
        elif 'rar' in desc_lower:
            return 'RAR'
        elif 'mpeg' in desc_lower or 'mp3' in desc_lower:
            return 'MP3'
        elif 'microsoft' in desc_lower and 'word' in desc_lower:
            return 'MS Word'
        elif 'ascii' in desc_lower or 'text' in desc_lower:
            return 'Text'
        
        # Extract first meaningful word
        words = description.split()
        if words:
            return words[0]
        return 'Unknown'
    
    def analyze_file(self, filepath):
        """Complete file analysis"""
        # Check if file exists
        if not os.path.exists(filepath):
            return {
                'error': f"File '{filepath}' does not exist",
                'success': False
            }
        
        # Get file info
        file_info = {
            'filename': os.path.basename(filepath),
            'path': os.path.abspath(filepath),
            'size': os.path.getsize(filepath),
            'extension': os.path.splitext(filepath)[1].lower(),
            'modified': datetime.fromtimestamp(os.path.getmtime(filepath))
        }
        
        # Identify file
        if self.using_magic:
            result = self.identify_with_magic(filepath)
        else:
            result = self.identify_with_signatures(filepath)
        
        # Read file header for display
        header_data = self.read_file_header(filepath, 32)
        
        # Combine results
        if result:
            return {
                'success': True,
                'file_info': file_info,
                'identification': result,
                'header_bytes': header_data,
                'extension_match': self.check_extension_match(file_info['extension'], result)
            }
        else:
            return {
                'success': True,
                'file_info': file_info,
                'identification': {
                    'type': 'Unknown',
                    'mime': 'application/octet-stream',
                    'method': 'none',
                    'confidence': 'none'
                },
                'header_bytes': header_data,
                'extension_match': False
            }
    
    def check_extension_match(self, actual_extension, identification):
        """Check if file extension matches identified type"""
        if not actual_extension:
            return None
        
        # Common extension to type mapping
        extension_map = {
            '.jpg': ['JPEG', 'JFIF', 'EXIF'],
            '.jpeg': ['JPEG', 'JFIF', 'EXIF'],
            '.png': ['PNG'],
            '.gif': ['GIF', 'GIF87a', 'GIF89a'],
            '.bmp': ['BMP', 'Bitmap'],
            '.pdf': ['PDF'],
            '.doc': ['DOC', 'Microsoft Word', 'MS Word'],
            '.docx': ['DOC', 'Microsoft Word', 'MS Word'],
            '.zip': ['ZIP'],
            '.rar': ['RAR'],
            '.7z': ['7Z', '7-Zip'],
            '.mp3': ['MP3', 'MPEG', 'ID3'],
            '.mp4': ['MP4', 'MPEG-4'],
            '.exe': ['EXE', 'PE32', 'PE64', 'MZ'],
            '.txt': ['Text', 'ASCII', 'UTF', 'BOM']
        }
        
        if actual_extension in extension_map:
            expected_types = extension_map[actual_extension]
            identified_type = identification.get('type', '').upper()
            
            for expected in expected_types:
                if expected.upper() in identified_type:
                    return True
        
        return False
    
    def display_results(self, analysis):
        """Display analysis results"""
        if not analysis['success']:
            print(f"\n Error: {analysis['error']}")
            return
        
        file_info = analysis['file_info']
        ident = analysis['identification']
        
        print("\n" + "="*60)
        print(" FILE ANALYSIS RESULTS")
        print("="*60)
        
        # File information
        print(f"\n File: {file_info['filename']}")
        print(f"   Path: {file_info['path']}")
        print(f"   Size: {file_info['size']:,} bytes")
        print(f"   Modified: {file_info['modified'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Extension: {file_info['extension'] or '(none)'}")
        
        # Identification results
        print(f"\n Identified as: {ident.get('type', 'Unknown')}")
        print(f"   Method: {ident.get('method', 'Unknown')}")
        print(f"   Confidence: {ident.get('confidence', 'Unknown')}")
        
        if ident.get('mime'):
            print(f"   MIME Type: {ident['mime']}")
        
        if ident.get('description'):
            print(f"   Description: {ident['description']}")
        
        # Extension validation
        if analysis['extension_match'] is not None:
            if analysis['extension_match']:
                print(f"\n Extension matches file content")
            else:
                print(f"\n  WARNING: Extension doesn't match file content!")
                print(f"   The file might have been renamed or is suspicious")
        
        # Show first bytes
        if analysis['header_bytes']:
            print(f"\n First 32 bytes (hex):")
            hex_str = ' '.join(f'{b:02x}' for b in analysis['header_bytes'])
            print(f"   {hex_str.upper()}")
            
            print(f"\n   ASCII preview:")
            ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in analysis['header_bytes'])
            print(f"   {ascii_str}")
        
        print("\n" + "="*60)
    
    def bytes_to_hex(self, data, bytes_per_line=16):
        """Convert bytes to formatted hex display"""
        if not data:
            return "No data"
        
        result = []
        for i in range(0, len(data), bytes_per_line):
            chunk = data[i:i + bytes_per_line]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            result.append(f"{i:04x}: {hex_part:<{bytes_per_line*3}}  {ascii_part}")
        
        return '\n'.join(result)

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def show_banner():
    """Display program banner"""
    print("\n" + "="*60)
    print(" FILE TYPE IDENTIFIER")
    print("="*60)
    print("Identify file types using Magic Bytes")
    print("Enter filename or 'quit' to exit")
    print("="*60)

def main():
    """Main interactive program"""
    clear_screen()
    show_banner()
    
    # Create identifier instance
    identifier = FileIdentifier()
    
    while True:
        print("\n" + "-"*60)
        
        # Get filename from user
        user_input = input("Enter filename (or 'quit' to exit): ").strip()
        
        # Check for quit command
        if user_input.lower() in ['quit', 'exit', 'q', 'bye']:
            print("\n Goodbye!")
            break
        
        # Check for help command
        if user_input.lower() in ['help', 'h', '?']:
            print("\n HELP:")
            print("  • Enter full path or filename if in current directory")
            print("  • Examples:")
            print("      document.pdf")
            print("      /home/user/image.jpg")
            print("      C:\\Users\\Name\\file.zip")
            print("  • Commands: quit, exit, q, help, h, ?")
            print("  • Press Ctrl+C to exit at any time")
            continue
        
        # Check for list files command
        if user_input.lower() in ['list', 'ls', 'dir']:
            print("\n Files in current directory:")
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for i, file in enumerate(sorted(files), 1):
                size = os.path.getsize(file)
                print(f"  {i:3}. {file:30} ({size:,} bytes)")
            continue
        
        # If no input, continue
        if not user_input:
            continue
        
        # Handle multiple files separated by space
        if ' ' in user_input:
            files = user_input.split()
            print(f"\n Analyzing {len(files)} file(s)...")
            
            for i, filepath in enumerate(files, 1):
                print(f"\n[{i}/{len(files)}] Analyzing: {filepath}")
                if os.path.exists(filepath):
                    result = identifier.analyze_file(filepath)
                    identifier.display_results(result)
                else:
                    print(f" File not found: {filepath}")
        else:
            # Single file
            filepath = user_input
            
            # If just filename without path, check current directory
            if not os.path.isabs(filepath) and not os.path.exists(filepath):
                # Try in current directory
                if os.path.exists(os.path.join('.', filepath)):
                    filepath = os.path.join('.', filepath)
            
            # Analyze file
            result = identifier.analyze_file(filepath)
            identifier.display_results(result)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Program interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        sys.exit(1)
        

        