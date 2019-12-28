import unittest 
from bsgs import bsgs

class TestBabyStepGiantStep(unittest.TestCase):
    def test_bsgs(self):
        self.assertAlmostEqual(bsgs(2,5,11) , (1,0))
        self.assertAlmostEqual(bsgs(5,3,2017) , (22,40))