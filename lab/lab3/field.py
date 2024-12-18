def field(goods, *args):
    assert len(args) > 0

    result = []
    
    if len(args) == 1:
        for item in goods:
            if args[0] in item and item[args[0]] is not None:
                result.append(item[args[0]])
    else:
        for item in goods:
            str_result = "{"
            skip = False
            for arg in args:
                if arg in item and item[arg] is not None:
                    str_result += f'{arg} : {item[arg]}'
                    if arg != args[-1]:
                        str_result += ", "
                else:
                    skip = True
                    break
            if not skip:
                str_result += "}"
                result.append(str_result)
    
    return result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

print(field(goods,'color','title') )