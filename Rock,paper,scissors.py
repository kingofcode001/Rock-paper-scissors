
import random

emojis={'r':'🪨','p':'📄','s':'✂️'}
choice=['r','p','s']

while True:
    user_choice=input("enter your choice('r','p','s'): ").lower()
    if user_choice not in choice:
        print('invalid chioice')
        continue

    computer_choice=random.choice(choice) 

    print(f"computer choice is {emojis[computer_choice]}")
    print(f"you choice is {emojis[user_choice]}")

    if user_choice==computer_choice:
        print('it is tie')
        
    elif ((user_choice=='r' and computer_choice=='s') or (user_choice=='p' and computer_choice=='r') or 
         (user_choice=='s' and computer_choice=='p')):
        print('you win')
        
    else:
        print('you lose')
        
        

    should_continue=input("do you want to continue? (y/n): ").lower()
    if should_continue != 'y':
        print('let play again')
        break       





    