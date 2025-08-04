
def NULL_not_found(object: any) -> int:

    obj_type = type(object)
    obj_type_name = obj_type.__name__
    match obj_type_name:
        case 'NoneType' if object is None:
            print(f"Nothing: {object} {obj_type}")
            return 0
        case 'float' if object != object:
            print(f"Cheese: {object} {obj_type}")
            return 0
        case 'int' if object == 0:
            print(f"Zero: {object} {obj_type}")
            return 0
        case 'str' if object == '':
            print(f"Empty: {object} {obj_type}")
            return 0
        case 'bool' if object is False:
            print(f"Fake: {object} {obj_type}")
            return 0
        case _:
            print("Type not found")
    return 1
