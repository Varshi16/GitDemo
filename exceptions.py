ItemsInCart = 0

if ItemsInCart != 2:
    #raise Exception('Products in cart not matching')
    pass

#assert (ItemsInCart == 2)
try:
    with open('filelog.txt') as reader:
        reader.read()

except:
    print('Somehow i reached this block because there is a failure in try block')

try:
    with open('filelog.txt') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('prints anyway')