import os.path
import tempfile
import unittest
from unittest import mock

from src.delete import rm


class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self):
        with open(self.tmpfilepath, 'wb') as f:
            f.write(b'Delete me!')

    def test_rm_1(self):
        # Remove the file.
        rm(self.tmpfilepath)

        # Test that it was actually removed.
        self.assertFalse(
            os.path.isfile(self.tmpfilepath),
            'Failed to remove the file.',
        )

    @mock.patch('src.delete.os')
    def test_rm_2(self, mock_os):
        rm('any path')
        # Test that rm called os.remove with the right parameters.
        mock_os.remove.assert_called_with('any path')

    @mock.patch('src.delete.os.path')
    @mock.patch('src.delete.os')
    def test_rm_3(self, mock_os, mock_path):
        # Force the file to not exist.
        mock_path.isfile.return_value = False
        rm('any path')
        self.assertFalse(
            mock_os.remove.called,
            'Failed to not remove the file if not present.',
        )

        # Force the file to exist.
        mock_path.isfile.return_value = True
        rm('any path')
        mock_os.remove.assert_called_with('any path')
