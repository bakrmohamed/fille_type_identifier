# File Type Identifier

Inspect local file headers using a small built-in signature table, or an optional python-magic backend. The original repository and script spelling are retained.

## Run

```bash
git clone https://github.com/bakrmohamed/fille_type_identifier.git
cd fille_type_identifier
python fille_type_identifier.py
```

Enter an existing file path, including paths containing spaces, or several space-separated paths without spaces. Use `list` to list local files and `quit` to exit. Wildcards are not expanded. Files are opened for reading only.

Optional installation provides the same interactive program as `file-identifier`:

```bash
python -m pip install .
file-identifier
```

The built-in backend needs only Python. For optional libmagic support, install the system libmagic library and `python -m pip install '.[magic]'`. On Windows, a compatible libmagic installation is also needed. If the backend cannot initialize or inspect a file, built-in signatures are used.

## What the result means

A known header suggests a format, not that a file is valid or safe. Extension comparison is a narrow hint: unknown formats and ambiguous containers return no comparison. OLE Compound does not prove a file is a Word document. ZIP signatures cannot distinguish every Office or archive subtype. The program does not scan for malware, inspect every byte, unpack archives, flag double extensions, or validate executable size.

Empty and unrecognized files remain Unknown. Header matches can be forged. Never execute a suspicious file to identify it. Local paths, file sizes and header bytes are printed, so review output before sharing it.

## Offline regression tests

```bash
python -m unittest -v
```

Eight tests cover PNG, misleading extensions, unknown and empty files, missing files, directories, ambiguous OLE containers and fallback after a libmagic failure. Tests use temporary synthetic files, not malware. Optional native libmagic behavior and operating-system compatibility are not covered by this suite.
