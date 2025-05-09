import random  

def check_win(player_choice, computer_choice):
  if player_choice == computer_choice:
    return 'tie'
  elif (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
    return 'win'
  else:
    return 'lose'

def get_choice():
  player_choice = input('Enter your choice (rock, paper, scissors): ')
  if player_choice not in ['rock', 'paper', 'scissors']:
    print('Invalid choice. Please try again.')
    return get_choice()
  print(f'You chose: {player_choice}')
  print('Computer is choosing...')    
  computer_choice = random.choice(['rock', 'paper', 'scissors'])
  print(f'Computer chose: {computer_choice}')
  result = check_win(player_choice, computer_choice)
  if result == 'tie':
    print('It\'s a tie!')
  elif result == 'win':
    print('You win!')
  else:
    print('You lose!')
  # if player_choice == computer_choice:
  #   print('It\'s a tie!')
  # elif (player_choice == 'rock' and computer_choice == 'scissors') or \
  #      (player_choice == 'paper' and computer_choice == 'rock') or \
  #      (player_choice == 'scissors' and computer_choice == 'paper'):
  #   print('You win!')
  # else:
  #   print('You lose!')
  choices = {
    'player_choice': player_choice,
    'computer_choice': computer_choice
  }
  return choices


choices = get_choice()
