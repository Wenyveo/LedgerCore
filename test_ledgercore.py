# test_ledgercore.py
"""
Tests for LedgerCore module.
"""

import unittest
from ledgercore import LedgerCore

class TestLedgerCore(unittest.TestCase):
    """Test cases for LedgerCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerCore()
        self.assertIsInstance(instance, LedgerCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
