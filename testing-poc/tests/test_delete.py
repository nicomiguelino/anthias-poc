import os.path
import tempfile
import unittest

from src.delete import rm


class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self):
        with open(self.tmpfilepath, 'wb') as f:
            f.write(b'Delete me!')

    def test_rm(self):
        # Remove the file.
        rm(self.tmpfilepath)

        # Test that it was actually removed.
        self.assertFalse(
            os.path.isfile(self.tmpfilepath),
            'Failed to remove the file.',
        )
