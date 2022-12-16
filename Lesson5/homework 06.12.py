def dictionary():
    dict1 = {1:'hello', 2:'world'}
    dict2 = {3:'goodbye', 4:'america'}
    dict1.update(dict2)
    print(dict1)
    return dict1
dictionary()