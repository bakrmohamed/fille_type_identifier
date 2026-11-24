import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from fille_type_identifier import FileIdentifier

class IdentifierTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.id = FileIdentifier()
        self.id.using_magic = False

    def sample(self, name, data):
        p = self.root / name
        p.write_bytes(data)
        return self.id.analyze_file(str(p))

    def test_png_with_space(self):
        r = self.sample('my photo.png', b'\x89PNG\r\n\x1a\n' + bytes(12))
        self.assertEqual(r['identification']['type'], 'PNG')
        self.assertTrue(r['extension_match'])

    def test_mismatch(self):
        self.assertFalse(self.sample('fake.jpg', b'%PDF-1.7')['extension_match'])

    def test_unknown_is_not_mismatch(self):
        self.assertIsNone(self.sample('unknown.bin', bytes(16))['extension_match'])

    def test_empty_is_unknown(self):
        self.assertEqual(self.sample('empty.txt', b'')['identification']['type'], 'Unknown')

    def test_directory_rejected(self):
        self.assertFalse(self.id.analyze_file(str(self.root))['success'])

    def test_missing_rejected(self):
        self.assertFalse(self.id.analyze_file(str(self.root / 'missing'))['success'])

    def test_ole_is_not_word_proof(self):
        r = self.sample('book.doc', bytes.fromhex('d0cf11e0a1b11ae1'))
        self.assertEqual(r['identification']['type'], 'OLE Compound')
        self.assertIsNone(r['extension_match'])

    def test_failed_magic_falls_back(self):
        self.id.using_magic = True
        with patch.object(self.id, 'identify_with_magic', return_value=None):
            self.assertEqual(self.sample('x.pdf', b'%PDF-1.7')['identification']['type'], 'PDF')

if __name__ == '__main__':
    unittest.main()
