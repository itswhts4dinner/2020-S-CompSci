while True:
  print("what word are you looking for?")
  search_word = input()


  with open('all_the_words.txt') as file:
      contents = file.read()
      if search_word in contents:
          print ('word found')
      else:
          print ('word not found')
