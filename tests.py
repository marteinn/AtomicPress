import tempfile
import unittest
import atomicpress


class AtomicPressTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, atomicpress.app.config['DATABASE'] = tempfile.mkstemp()
        atomicpress.app.config['TESTING'] = True
        self.app = atomicpress.app.test_client()
        atomicpress.init_db()

if __name__ == '__main__':
    unittest.main()