#Реализуйте цепную функцию суммирования.

class chain_sum_1(int):

    def __call__(self, num):

        return chain_sum_1(self + num)


def chain_sum_2(*arg):

    try:
        out = sum(arg)
    except TypeError:

        print('Ошибка в типе данных! (аргументы принимают только числа)')
        return None
    
    else:
        return out


if __name__ == '__main__':

    out = chain_sum_1(1)(2)(5)(1)
    print(out)

    out = chain_sum_2(1, 2, 5, 1)
    print(out)





