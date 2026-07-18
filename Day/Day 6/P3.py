fruits = ['apple','banana','cherry']
    
iterator = iter(fruits)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break