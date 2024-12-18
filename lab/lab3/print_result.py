def print_result(input_func):
    def output_func(*args, **kwargs):
        print(input_func.__name__)
        result=input_func(*args, **kwargs)
        if isinstance(result,list):
            for i in result:
                print(i)
        elif isinstance(result,dict):
            for key,val in result.items():
                print('{} = {}'.format(key,val))
        else:
            print(result)

        return result
    return output_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()