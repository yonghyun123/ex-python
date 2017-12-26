# -*- coding: utf-8 -*- 

def get_description():
  """Return random weather, just like the pros"""
  import random as rd
  possibilities = ['Rain','snow','sleet','fog','sun','who knows']
  return rd.choice(possibilities)