# lene.exceptions
# Exception hierarchy for lene package
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Fri Feb 21 09:19:57 2014 -0500
#
# Copyright (C) 2014 UMD Metacognitive Lab
# For license information, see LICENSE.txt
#
# ID: exceptions.py [] bengfort@cs.umd.edu $

"""
Exception hierarchy for lene package
"""

##########################################################################
## Top Level Exceptions
##########################################################################

class LeneException(Exception):
    """
    Top level exception for Lene errors
    """
    pass

##########################################################################
## Lexer Exceptions
##########################################################################

class LexicalError(LeneException):
    """
    Error reading the knowledge base
    """
    pass

class UnexpectedCharacter(LexicalError):
    """
    Unexpected character or mark on a line
    """

    def __init__(self, char, line):
        msg = "Unexpected Character %r on line %d" % (char, line)
        super(UnexpectedCharacter, self).__init__(msg)

class SyntacticError(LexicalError):
    """
    Improper syntax in knowledge base
    """
    pass

##########################################################################
## RDF/OWL Exception
##########################################################################

class OntologyException(LeneException):
    """
    Error constructing RDF or reading the ontology
    """
    pass

class GraphBindingError(OntologyException):
    """
    Binding or unbinding from a graph caused an issue
    """
    pass

##########################################################################
## Runtime Exception
##########################################################################

class LeneRuntimeError(Exception):
    """
    Raise these to print an error and exit 2
    """
    pass
