def hello():
    print('Greetings user!')
def pack(sandwich, chips, candy):
    return[sandwich,chips,candy]
food_list = ['sandwich', 'chips', 'candy']
def eat_lunch(food_list):
    if not food_list:
        print('My lunchbox is empty!')
    else:
        print(f'First I eat {food_list[0]}')
        for food in food_list[1:]:
            print(f'Next I eat {food}')


hello()
print(pack('sandwich','chips','candy'))
print(pack(1,2,3))
eat_lunch(food_list)