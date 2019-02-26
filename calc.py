from os import system, name 
def add(inittial_num):
  second_num =  float(input("Add number:"))
  return inittial_num+second_num


def substract(inittial_num):
  second_num = float(input("Substract number:"))
  return inittial_num-second_num


def multiply(inittial_num):

  second_num = float(input("Multiply with number:"))
  return inittial_num*second_num


def divide(inittial_num):
  second_num = float(input('Divide with number:'))
  return inittial_num/second_num 

def clear(): 
  
    if name == 'nt': # for windows
        _ = system('cls') 
  
    # for linux and mac 
    else: 
        _ = system('clear')


def calculator(current_number):

  clear()

  print("The current result is: ",current_number)
  print("1. Add a number")
  print("2. Substract a number")
  print("3. Multiply by a number")
  print("4. Devide by a number")
  print("0. Print result")
  print("-99. Exit")

  select_command=int(input())
  while select_command != 1 and select_command != 2 and select_command != 3 and select_command != 4 and select_command != -99 and select_command != 0:
    print("Please select one of the options above.")
    select_command=int(input())
  if select_command==1:
    current_number=add(current_number)
    calculator(current_number)
  elif select_command==2:
    current_number=substract(current_number)
    calculator(current_number)
  elif select_command==3:
    current_number=multiply(current_number)
    calculator(current_number)
  elif select_command==4:
    current_number=divide(current_number)
    calculator(current_number)
  elif select_command==0:
    clear()
    print("The result is: ",current_number)
  elif select_command==-99:
    exit
    clear()

clear()
initial_number=float(input('Enter an initial number to calculate with: '))
calculator(initial_number)