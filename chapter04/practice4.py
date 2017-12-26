# -*- coding: utf-8 -*- 

# 4.1 
guess_me = 7

if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right");
start = 1
while start <= guess_me:
    if start < guess_me:
        print("too low")
    elif start > guess_me:
        print("oops")
    else:
        print("just right");
    start += 1;

items = [3,2,1,0];
result = []
for item in items:
    result.append(item);
    
print(result)

even_list = [number for number in range(10) if number % 2 == 0]
print(even_list)