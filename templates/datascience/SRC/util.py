"""
Module: util
============

Description:
------------

	Contains basic utilities for interface, etc. 


####################
{author}
{email}
{date}
####################
"""

################################################################################
####################[ Interface Utilities ]#####################################
################################################################################

def print_status(stage, status, verbose=True):
    """
        prints status if verbose is set
    """
    if verbose:
        print '-----> %s: %s' % (stage, status)
