question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
if '42' == question:
    print('Yes')
elif 'forty two' == question:
    print('Yes')
elif 'forty-two' == question:
    print('Yes')
else:
    print('No')
