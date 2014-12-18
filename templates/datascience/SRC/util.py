"""
Module: util
============

Description:
------------

	Contains basic utilities for interface, etc. 


{pyroject_header_foot}
"""

################################################################################
####################[ Interface Utilities ]#####################################
################################################################################

def print_status(stage, status, verbose=True):
    """
        prints status if verbose is true 
    """
    if verbose:
        print '-----> %s: %s' % (stage, status)
