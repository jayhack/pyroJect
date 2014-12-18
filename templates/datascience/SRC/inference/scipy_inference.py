"""
Module: scipy_inference
=======================

Description:
------------

	Defines instance of ScipyInference, an instance of BaseInference,
	that uses the scipy stack (numpy, pandas, sklearn) to deal with 
	inference

####################
Jay Hack
jhack@stanford.edu
Fall 2014
####################
"""
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
			returns scores
		"""
		X, y = self.featurize(data)
		return cross_val_score(self.pipeline, X, y, cv=5, verbose=2)
