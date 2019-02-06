def url(inp):
 if inp.startswith('http'):
  return inp
 else:
   try:
      requests.get('https://' + inp)
      return 'https://' + inp
   except:
       return 'http://' + inp

