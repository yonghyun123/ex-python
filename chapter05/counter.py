# -*- coding: utf-8 -*- 

from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast);
print(breakfast_counter)

lunch = ['eggs','eggs','bacon'];
lunch_counter = Counter(lunch);
print(lunch_counter);

print(lunch_counter + breakfast_counter)

# 회문 끝장난다. deque로 한방에
def palindrome(word):
  from collections import deque
  dq = deque(word)
  while len(dq) > 1:
    if(dq.popleft() != dq.pop()):
      return False
  return True;

print(palindrome('abccba'))

# 더 신박하네
def another_palindrome(word):
  return word == word[::-1]
print(another_palindrome('wwwbbbwwww'))