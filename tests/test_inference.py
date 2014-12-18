"""
Test: test_inference
====================

Description:
------------
	
	tests classes contained in inference.py


##################
Jay Hack
jhack@stanford.edu
Fall 2014
##################
"""
import os
import unittest
import nose
from nose.utils import *
import numpy as np
import pandas as pd

from pyroJect.inference import ScipyInference
from sklearn.pipeline import Pipeline
from sklearn.preprocess import PCA
from sklearn.linear_model import LogisticRegression

class Inference(ScipyInference):
	"""
		Basic inference class
	"""

	def __init__(self):
		super(ScipyInference, self).__init__(self)

	def define_pipeline(self):
		return Pipeline([
							('PCA', PCA(n_components=5)),
							('LR', LogisticRegression())
						])

	def featurize(self, data):
		if 'label' in data.columns:
			X = data[set(data.columns) - set(['label'])].as_matrix()
			y = data['label'].as_matrix()
			return X, y
		else:
			return data.as_matrix()

	



class Test_EXAMPLE(unittest.TestCase):

	################################################################################
	####################[ setUp/tearDown	]#######################################
	################################################################################

	def setUp():
		"""
			sets self.data_dir, self.model_path, self.data
		"""
		self.data_dir = os.split(__file__)[0] #current directory
		self.model_path = os.path.join(self.data_dir, 'model.pkl')

		#=====[ Step 2: get data	]=====
		self.data = pd.DataFrame(np.random.randn(100, 10))
		self.data['label'] = self.data.sum(axis=1) > 0


	def tearDown():
		"""
			removes the model, if it exists
		"""
		if os.path.exists(self.model_path):
			os.remove(self.model_path)


	################################################################################
	####################[ EXAMPLE TESTS	]###########################################
	################################################################################

	def test_train(self):
		"""
		TEST TRAIN 
		----------
		just trains
		"""
		inference = Inference()
		inference.train(self.data)


	def test_train_classify(self):
		"""
		TEST TRAIN CLASSIFY 
		-------------------
		trains then classifies 
		"""
		inference = Inference()
		inference.train(self.data.iloc[:50])
		output = inference.classify(self.data.iloc[50:][range(10)])
		self.assertEqual(output.shape, (100,))


	def test_evaluate(self):
		"""
		TEST EVALUATE 
		-------------
		evaluates the model
		"""
		inference = Inference()
		inference.evaluate(self.data)




