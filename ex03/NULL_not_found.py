def NULL_not_found(object: any) -> int:
    dict_types = {'NoneType': 'Nothing', 'float': 'Cheese', 'int': 'Zero', 'str': 'Empty', 'bool': 'Fake'}
    obj_type = type(object)
    obj_type_name = obj_type.__name__
    match obj_type_name:
        case 'NoneType' if object is None:
            print(f"Nothing: {object} {obj_type}")
        case 'float' if object != object:
            print(f"Cheese: {object} {obj_type}")
        case 'int' if object == 0:
            print(f"Zero: {object} {obj_type}")
        case 'str' if object == '':
            print(f"Empty: {object} {obj_type}")
        case 'bool' if object is False:
            print(f"Fake: {object} {obj_type}")
        case _:
            print("Type not found")
            

    return 1