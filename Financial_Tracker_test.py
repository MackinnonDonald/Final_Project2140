from Financial_Tracker import *
import unittest

class TestFinanceTracker(unittest.TestCase):
    
    def test_create_tracker(self):
        sample_tracker = PersonalFinanceTracker()
        self.assertIsInstance(sample_tracker, PersonalFinanceTracker)

if __name__ == '__main__':
    unittest.main()
