
def all_thing_is_obj(obj: any) -> int:
    t_list = ['dict', 'list', 'set', 'tuple']
    type_name = type(obj).__name__
    if type_name in t_list:
        print(f"{type_name.capitalize()} : {type(obj)}")
        return 42
    if type_name == 'str':
        print(f"{obj} is in the kitchen : {type(obj)}")
        return 42
    print("Type not found")
    return 42
