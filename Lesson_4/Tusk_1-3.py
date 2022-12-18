text = input('please input something: ')
if text.isdigit():
  if int(text) % 2 == 0:
    print ('You entered a number and it is even')
  else:
    print ('You entered a number and it is odd')
else:
  print (f'You entered a text with {len(text)} symbols')