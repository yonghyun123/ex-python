# -*- coding: utf-8 -*- 
from pprint import pprint

def answer(a):
    print(a);

def run_something(func):
  a = 42
  func.__call__(a);
  
run_something(answer)

def knight(saying):
    def inner():
        return "who say:"+saying;
    return inner;

a = knight("yong")();
b = knight("hyun");
print(globals())
