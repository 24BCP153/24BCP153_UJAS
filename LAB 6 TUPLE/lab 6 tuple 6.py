tuple_ =( 'apple', 'banana', 'potato')
temp_list = list(tuple_)
temp_list[1] = 'kiwi'
tuple_ = tuple(temp_list)
print(tuple_)
