# Условная конструкция. Операторы if, elif, else

first_ = input('первое число:')
second_ = input('второе число:')
thifd_ = input('третье число:')
if first_ == second_ and first_ == thifd_ :
    print('3')
elif first_ == second_ or first_ == thifd_ or second_ == thifd_ :
    print('2')
else:
    print('0')
