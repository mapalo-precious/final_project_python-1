# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# FINAL PROJECT 1
Name=input('What is your name? :    ')

Religion=input("Welcome to the Religious quiz game {}. What is your religion(type'c' Christianity or Islam 'i'):     ".format(Name))

print(Religion)
while True :

#///////////////////////////////////////////////////////////////////////////// CHRISTIANITY QUIZ ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  if Religion.lower()=='c' :
    welcome_='Hello, here are some questions based on the Bible.'
    print(welcome_)
    Instructions="Here are the instructions:\n -There exactly 10 questions in both quizes, answer all of them\n-To type an answer simply type THE LETTERS  in the textbox\n -When you answer each question correctly you will be given 1 points, but if you answer a question wrongly answer a question 0.5 points will be deducted "
    print(Instructions)
    score=0

    question_CH_1=input('1.How many brothers did Joseph have?(answer this question by using numbers)\n a. 11 \n b. 12 \n c. 0 \n d. 10:     ')# Question 1 # If statement saying; if the question is correct it will add one to your score and tell you your answer is corrct. It is the same for all the questions
    if question_CH_1.lower()=='a' :
      print('Your answer is correct')
      score=score+1      #If it is wrong it will move on to the next question ad deduct 0.5 from your score. It is the same for all the questions
    else :
      print('You are wrong. Joseph had 11 brothers')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_2=input('2.What did Moses say God commanded the Pharaoh to do?\n a. make israel slaves \n  b. worship God \n c. let his people go \n d. appoint him as a governor:     ')# Question 2
    if question_CH_2.lower()=='c' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('you are wrong. Moses said God commanded the Pharaoh to let his people go ')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_3=input(' 3.What golden image did the Israelites make at Mt. Sinai?\n a. a golden pig \n b. a sun \n c. a golden chicken \n d. a golden calf :       ') # Question 3
    if question_CH_3.lower()=='d' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong. They made a golden calf')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_4=input('4.Who was Jesus’ birth father?\n a. God \n b. Joseph\n c. The spirit \n d. Mary:   ')# Question 4
    if question_CH_4.lower()=='a' :
      print('you are correct' )
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong.Jesus’ birth father is God')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_5=input("5.Name Jesus' hometown.\n a. Bethlehem \n b. Nazareth \n c. Jerusalem \n d. heaven :  ")# Question 5
    if question_CH_5.lower()=='b' :
      print('you are correct')
      score=score+2
      print('your score is {}'.format(score))
    else :
      print("You are wrong. Jesus' hometown is Nazareth")
      score=score-0.5

    question_CH_6=input('6.When God showed Abram the stars in the sky, what did he promise?\n a. That Abram would have equal descendants than the number of stars. \n b. That Abram would have more descendants than the number of stars.  \n c. That Abram would have less descendants than the number of stars. \n d.That Abram would have 10 descendants.:     ')# Question 6
    if question_CH_6.lower()=='b' :
      print('Your answer is correct')
      score=score+1
    else :
      print('You are wrong.the answer is: That Abram would have equal descendants than the number of stars.')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_7=input('7. Who did Laban trick Jacob into marrying??\n a. Sarah \n  b. Esther \n c. Rachael \n d. Leah.:     ')# Question 7
    if question_CH_7=='d' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('you are wrong. Laban trick Jacob into marrying Leah ')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_8=input(' 8.Who was Paul with when he wrote the letter to Philemon?\n a.Himself \n b. Timothy \n c. God \n d. Jesus :       ') # Question 8
    if question_CH_8.lower()=='b' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong. Paul was with Timothy when he wrote the letter to Philemon')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_9=input('9.Who killed Absalom??\n a. David \n b. Saul\n c. Sammuel \n d. Joab:   ')# Question 9
    if question_CH_9.lower()=='d' :
      print('you are correct' )
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong.Joab killed Absalom')
      score=score-0.5
      print('your score is {}'.format(score))

    question_CH_10=input("10.Who returned to Israel to build up the walls of Jerusalem?.\n a. Nehemiah \n b. Esther \n c. Cyrus \n d. John :  ")# Question 6
    if question_CH_10.lower()=='a' :
      print('you are correct')
      score=score+3
      print('your score is {}'.format(score))
    else :
      print("You are wrong. Nehemiah is the one who returned to Israel to build up the walls of Jerusalem ")
      score=score-0.5

    if score>=9 :
      print('(distinction) Excellent you pass')
    elif score>=6 :
      print('(Merit) Very good you pass')
    elif score>=4 :
      print('(pass) Well done, but work harder next time')
    else :
      print('(Fail) Sorry but you did no get enough points')
    break


#/////////////////////////////////////////////////////////////////////////////////////////// ISLAMIC QUIZ /////////////////////////////////////////////////////////////////////////////////////

  elif Religion.lower()=='i' :
    welcome_='Hello, here are some questions based on the Quran.'
    print(welcome_)
    Instructions='Here are the instructions:\n -There exactly 10 questions in both quizes, answer all of them\n-To type an answer simply type a, b, c or d  in the textbox\n -When you answer each question correctly you will be given 4 points, but if you answer a question wrongly answer a question 2.5 points will be deducted '
    print(Instructions)
    score=0

    question_IS_1=input('1.Who will get their book of deeds in the right hand on the Day of Judgment?\n a.The disbelievers\n b.The believers\n c.The hypocrites\n d. The leaders :   ')# Question 1
    if question_IS_1.lower()=='a' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong.the believers will get their book of deeds in the right hand on the Day of Judgment')
      score=score-0.5
      print('your score is {}'.format(score))

    question_IS_2=input('2.What was the relation between Prophet Musa (alayhi as-salaam) & Prophet Haroon (alayhi as-salaam)?\n a. Cousins\n b. Brothers \n c.Father & son \n d. Friends :')# Question 2
    if question_IS_2.lower()=='b' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
     print('You are wrong. the relation between Prophet Musa (alayhi as-salaam) & Prophet Haroon (alayhi as-salaam) is cousins')
     score=score-0.5
     print('your score is {}'.format(score))

    question_IS_3=input('3.What is Az-Zaqqum?\n a. Food for the people of hellfire\n b. Drink for the people of hellfire \n c. Home for the people of hellfire \n d. Clothes for the people of hellfire :')# Question 3
    if question_IS_3.lower()=='a' :
      print('you are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong. Az-Zaqqum is food for the people of hellfire')
      score=score-0.5
      print('your score is {}'.format(score))


    question_IS_4=input('4.What does Zam Zam mean?\n a. Holy water\n b. Water well \n c. Stop \n d. Drink :')# Question 4
    if question_IS_4.lower()=='c' :
      print('you are correct')
      print('your score is {}'.format(score))
      score=score+1
    else :
      print('You are wrong.Zam Zam means stop')
      score=score-0.5
      print('your score is {}'.format(score))

    question_IS_5=input('5.What is the virtue of reciting Ayatul Kursi before going to bed at night to sleep?\n a. Takes away hunger\n b. Gives you strength \n c. You are protected from harm till sunrise \n d. House in Jannah :')# Question 5
    if question_IS_5.lower()=='c' :
      print('you are correct')
      score=score+2
      print('your score is {}'.format(score))
    else :
      print('You are wrong. the virtue of reciting Ayatul Kursi before going to bed at night to sleep is you are protected from harm till sunrise')
      score=score-0.5
      print('your score is {}'.format(score))

    question_IS_6=input('6.Which Angel is Hellfire’s gatekeeper?\n a. Jibraeel (as) \n b. Mikaeel (as)\n c.Maalik (as) \n d. Israfeel (as) :   ')# Question 6
    if question_IS_6.lower()=='c' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong.')
      score=score-0.5
      print('your score is {}'.format(score))

    question_IS_7=input('7.Which of the following is the name of Allah with the meaning – The Most Loving One?\n a. Al-Majeed\n b. Al-Wadud \n c. Al-Muqtadir\n d Al-Waarith :    ')# Question7
    if question_IS_7.lower()=='b' :
      print('You are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
     print('You are wrong. the name of Allah with the meaning the Most Loving One is Al-Wadud')
     score=score-0.5
     print('your score is {}'.format(score))

    question_IS_8=input('8.What is the name of Madinah in the Quran?\n a.Bakkah\n b. Quds\n c. Marwah\n d.Yathrib  :    ')# Question 8
    if question_IS_8.lower()=='d' :
      print('you are correct')
      score=score+1
      print('your score is {}'.format(score))
    else :
      print('You are wrong. the name of Madinah in the Quran is Yathrib ')
      score=score-0.5
      print('your score is {}'.format(score))


    question_IS_9=input('9.Why we should not curse time?\n a. Because it will bring bad luck\n b.Because Allah says He is Time\n c.  Because Allah says He will cut our time\n d. Because it will bring good luck :    ')# Question 9
    if question_IS_9.lower()=='b' :
      print('you are correct')
      print('your score is {}'.format(score))
      score=score+1
    else :
      print('You are wrong. We should not curse time because Allah says he is time')
      score=score-0.5
      print('your score is {}'.format(score))

    question_IS_10=input('10.Allah says, with His knowledge, He is more closer to us than our ________?\n a. Thoughts /n b. Heart \n c. Jugular Vein \n d. Blood :      ')# Question 10
    if question_IS_10.lower()=='c' :
      print('you are correct')
      score=score+3
      print('your score is {}'.format(score))
    else :
      print('You are wrong. Allah says, with His knowledge, He is more closer to us than our jugular vein')
      score=score-0.5
      print('your score is {}'.format(score))

    if score>=9 :
      print('(distinction) Excellent you pass')
    elif score>=6 :
      print('(Merit) Very good you pass')
    elif score>=3 :
      print('(pass) Well done, but work harder next time')
    else :
      print('(Fail) Sorry but you did no get enough points')
    break

  else :
    print('You can only choose between Chrstianity or islam')
    Religion=input('Welcome to the Religious quiz game {}. What is your religion(Are you part of Christianity or Islam?)   '.format(Name))
