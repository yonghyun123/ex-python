# -*- coding: utf-8 -*- 
items = ['a','b','c'];
for a in items:
    print(a);

print(items[::-1]);

string = 'abcdefg';
print(string[::]);

marxes = ['Groucho', 'Chico', 'Harpo'];
print(','.join(marxes));

# sorted와 sort 차이 
# sort()는 리스트 자체를 정렬
# sorted()는 정렬된 복사본 반환

sorted_marxes = sorted(marxes);
print(sorted_marxes);

# 리스트에서 = 는 깊은복사이다. 2개의 변수가 하나의 객체를 가르키는 느낌 하지만 b = a.copy(), c = list(a), d = a[:] 이것들은 값복사
# 하나가 변경되면 다른 변수에 담겨져있는 리스트도 변경된다.
a = [1,2,3];
b = a;
a[0] = 'surprise'
print(b);

# tuple unpacking
marx_tuple = ('Groucho', 'Chico', 'Harpo');
a,b,c = marx_tuple;
print(b)

# dictionary update
# 만약 두개의 dict을 병합하려 할때 키가 겹친다면 두 번째 dict에 있는 값으로 병합된다.
first = {'a': 1, 'b': 2}
second = {'b': 'unhappy'}
first.update(second)
print(first)

# set은 내가아는 집합과 유사
# intersection, union, difference, exclusive, etc 사용가능
