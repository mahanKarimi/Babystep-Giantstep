import unittest 
from src import bsgs

class TestBabyStepGiantStep(unittest.TestCase):
    def test_bsgs(self):
        self.assertAlmostEqual(bsgs.bsgs(2,5,11) , (1,0))
        self.assertAlmostEqual(bsgs.bsgs(5,3,2017) , (22,40))