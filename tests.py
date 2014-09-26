import tempfile
import unittest
import wordflask

__author__ = 'martinsandstrom'


class WordFlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, wordflask.app.config['DATABASE'] = tempfile.mkstemp()
        wordflask.app.config['TESTING'] = True
        self.app = wordflask.app.test_client()
        wordflask.init_db()

if __name__ == '__main__':
    unittest.main()