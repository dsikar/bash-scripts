from content import Content


"""
 The class will be helpful in the future for request packets like 
 7.1	Configuration Request, and otherwise that does not have a content or playload.
"""

class EmptyContent(Content):

  def __init__(self):
    Content.__init__(self);
  