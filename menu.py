def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  print('Choose a game mode:')
  print('1. Human vs Human')
  print('2. Random AI vs Random AI')
  print('3. Human vs Random AI')
  print('4. Human vs Unbeatable AI')
  valasz = int(input('Your choice is: '))
  if valasz < 1 or valasz > 4:
    return get_menu_option()
  return valasz
  pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    pass