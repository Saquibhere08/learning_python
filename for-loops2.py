items =[int,float,"harry",3,4,5,6,7,6222,4332,3323,23,43,5,656]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)