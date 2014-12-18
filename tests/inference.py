"""
Module: inference
=================

Description:
------------

	Contains base classes for objects that deal with 
	every aspect of performing inferences based on data.

{pyroject_header_foot}
"""
import pickle
import numpy as np
import pandas as pd

from util import *

################################################################################
####################[ BaseInference ]###########################################
################################################################################

class BaseInference(object):
	"""
		Class: BaseInference
		====================

		Description:
		------------

			Base class for objects that will contain models,
			have the capability to train/update them and perform 
			inferences based on them.

			The main methods are as follows:
			
				load: load a model  (given a path)
				save: save the model (given a path)
				featurize: raw data -> X, y (or just X)
				train: raw data -> updated model
				classify: raw data -> predicted labels
				evalute: raw data -> evaluation of model

			In addition to load/save, which, given a path, return 
			load/save the model.

			Development should focus on filling in the define_pipeline
			method, which returns a pipeline. pipeline should support 
			fit(X,y), transform(X), and fit_transform(X,y) methods.

		
		Usage:
		------

			In [1]: ice = inference()
			In [2]: ice.train(data)
			In [4]: ice.classify(data)
			In [5]: ice.evaluate(data)
			In [3]: ice.save('/path/to/model.pkl')
			In [4]: ice.load('/path/to/model.pkl')
	"""

	def __init__(self):
		"""
			sets self.pipeline. self.pipeline must provide 
			fit, transform and fit_transform methods.
		"""
		self.pipeline = self.define_pipeline()


	def define_pipeline(self, data):
		"""
			defines the pipeline 
		"""
		raise NotImplementedError


	def featurize(self, data):
		"""
			raw data -> X, y
		"""
		raise NotImplementedError


	def train(self, data, verbose=False):
		"""
			raw data -> trained self.pipeline
		"""
		print_status('inference.train', 'featurizing data', verbose)
		X, y = self.featurize(data)

		print_status('inference.train', 'fitting model')
		self.pipeline.fit(X, y)


	def classify(self, data):
		"""
			raw data -> predicted labels 
		"""
		X = self.featurize(data)
		return self.pipeline.predict(X)


	def evaluate(self, data):
		"""
			performs cross-validation on inference pipeline. 
		"""
		raise NotImplementedError


	def save(self, path):
		"""
			saves self.pipeline to specified path via pickle
		"""
		print_status('inference.save', 'saving model to path %s' % path)
		pickle.dump(self.pipeline, open(path, 'w'))


	def load(self, path):
		"""
			loads self.pipeline from a specified path 
		"""
		print_status('inference.load', 'loading model from path %s' % path)
		self.pipeline = pickle.load(open(path, 'r'))









################################################################################
####################[ ScipyInference ]##########################################
################################################################################

from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score

class ScipyInference(BaseInference):
	"""
		Class: ScipyInference
		=====================
		
		Description:
		------------
		Inference using the scipy stack: numpy, pandas, sklearn.

		Performs evaluation using sklearn.cross_validation.cross_val_score

	"""

	def __init__(self):
		super(ScipyInference, self).__init__()
		

	def evaluate(self, data, cv=5):
		"""
			evaluates the classifier 
		"""
		X, y = self.featurize(data)

		print_status('inference.evaluate', 'running cross-validation', True)
		scores = cross_val_score(self.pipeline, X, y, cv=5, verbose=2)
		print "Cross Validation Scores:\n-------"
		for i, s in enumerate(scores):
			print "Cross-Validation run #%i: %s" % (i+1, str(s))
		print "\nAverage: %s" % str(scores.mean())

