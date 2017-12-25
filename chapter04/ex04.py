# -*- coding: utf-8 -*- 
english = 'Monday', 'Tuesday', 'Wednesday';
french = 'Lundi', 'Mardi', 'Mercredi';

print(list(zip(english, french)));
print(dict(zip(english, french)));

'''
None 과 false 차이
함수가 명시적으로 return을 호출하지 않으면 반환값을 None으로 한다
false와 none 은 다르다.
'''
thing = None;
if thing:
  print("It's some thing");
else:
  print("It's no thing");

if thing is None:
  print("It's nothing");
else:
  print("It's something");

'''
 * vs **
 * 는 매개변수를 모아 튜플로 반환
 ** 매개변수를 모아 딕셔너리로 반환
'''
# inner function

def knights(saying):
    def inner(quote):
        # return "We are the knights who say:",quote # return tuple
        return "We are the knights who say: "+quote # return string
    return inner(saying)

print(knights('Ni'));

# lambda function

def edit_story(words, func):
    for word in words:
        print(func(word));

stairs = ['thud', 'meow', 'thud', 'hiss'];

def enliven(word):
    return word.capitalize() + '!';
# edit_story(stairs, enliven); # general
edit_story(stairs, lambda string: string.capitalize()+'!')

a = "abcd";
print(a[::-1]);

animal = 'fruitbat'
def change_and_print_global():
    global animal # using global variable
    animal = 'sex'
    print('inside valuable = '+animal);
change_and_print_global();
print(animal);

