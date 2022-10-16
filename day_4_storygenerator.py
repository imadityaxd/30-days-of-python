#story generator by random module
import random
when = ['A few years ago', 'Yesterday','Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Adi', 'Vishal', 'Vikash', 'Daniel', 'Nikhil', 'Lukesh']
residence =  ['Barcelona','India', 'Germany', 'Venice', 'England' ]
went = ['cinema', 'university', 'seminar','stadium', 'college','market']
happened = ['made a lot of enemies.', 'punched him in the face.', 'eats a burger.', 'founds a treasure.', 'fought of a bull.', 'kissed a girl.']
print(random.choice(when)+ ', '+ random.choice(name) + ' who lived in '+ random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
