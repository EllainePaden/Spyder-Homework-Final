# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:04:27 2020

@author: Ellaine
"""

#Introduction to the Quiz

def Introduction():
   name = input('Kindly Enter your Name: ')
   print("Hello" + "\t" + name.title() + "!" + "\nWelcome to the Planetary Quiz" + "\nChoose the Correct Answer to the following questions.")


#quiz proper

def Quiz():
  questions = ['\n1. How many planets are there in the Solar System? \nA. 3 \tB. 9\n',
              '\n2. What planet is closest to the sun? \nA. Mars \tB. Mercury\n',
              '\n3. Which is the coldest planet of the Solar System? \nA. Pluto \tB. Saturn\n',
              '\n4. Which is the densest planet? \nA. Earth \tB. Jupiter\n',
              '\n5. Which planet is not a terrestial planet \nA. Saturn \tB. Mars\n',
              '\n6. What is the eight planet from the sun? \nA. Neptune \tB. Jupiter\n',
              '\n7. Which planet has the largest ring system? \nA. Saturn \tB. Jupiter\n',
              '\n8. What is the rotational period of Earth? \nA. 24 hours \tB. 36 hours\n',
              '\n9. Which is shorter, Mercury  day or year? \nA. Day \tB. Year\n',
              '\n10. Which planet has the hottest temperature? \nA. Venus \tB. Mars\n'
              ]
  answers = ['B','B','A','A','A','A','A','A','B','A']

  score = 0
  a = 0
   
  

  for question in questions:
    print(question)

    ans = input("Kindly Enter your Answer: ")

    if ans.upper() == answers[a]:
      print("\nYou are correct!\n")
      score +=1
    else:
      print("\nSorry, you got it wrong\n")

    a +=1

  print("\nYour Final Score is:{0} out of 10".format(score))
  
  if score < 6:
    print("\nBetter luck next time =(")
  else:
    print("\nGood job! =)")

Introduction()
Quiz()
 


