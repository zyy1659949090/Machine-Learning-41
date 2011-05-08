'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.classification.Dummys import Always1Predictor


class Test(unittest.TestCase):
    __verbose = True #print some stats?

    def testDummyModel(self):
        dummy = Always1Predictor()
        dummy.buildClassifier('../../../../data/a1a')
        dummy.validateModel('../../../../data/a1a.t')
        if self.__verbose:
            print '# instances\n    training:{tr:d}\n    test:{te:d}'.format(
                                tr=dummy.get_inst_train(), te=dummy.get_inst_test())
            print '{corr:2.3f}% correct - RMSE: {rmse:.3f}'.format(
                                corr=dummy.get_pctCorrect(), rmse=dummy.get_rmse())
        self.assertTrue(dummy.get_pctCorrect() > 24) # for data set a1a !!!


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()