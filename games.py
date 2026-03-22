import random
from random import randint
from random import choice
print("Четыре игры на выбор")
print('1-Крестики Нолики\n2-Камень Ножницы Бумага\n3-Угадай Число\n4-Виселица')

while True:
   num_pl = int(input('Число от 1 до 4: '))

   if num_pl == 1:
    print(" Игра Крестики-нолики для двух игроков ")

    board = list(range(1,10))

    def draw_board(board):
       print("-" * 13)
       for i in range(3):
          print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
          print("-" * 13)


    def take_input(player_token):
       valid = False
       while not valid:
          player_answer = input("Ход:  " + player_token+"? ")
          try:
             player_answer = int(player_answer)
          except:
             print("Некорректный ввод. Вы уверены, что ввели число?")
             continue
          if player_answer >= 1 and player_answer <= 9:
             if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
             else:
                print("Эта клетка уже занята!")
          else:
            print("Некорректный ввод. Введите число от 1 до 9.")

    def check_win(board):
       win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
       for each in win_coord:
           if board[each[0]] == board[each[1]] == board[each[2]]:
              return board[each[0]]
       return False

    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
               take_input("X")
            else:
               take_input("O")
            counter += 1
            if counter > 4:
               tmp = check_win(board)
               if tmp:
                  print(tmp, "выиграл!")
                  win = True
                  break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)
    main(board)

   elif num_pl == 2:
    start = input('Игра "Камень, ножницы, бумага".\nЧтобы начать введите "+"' )

    if start == '+':

        print('Если захотите закончить введите "-".')
        print('Если захотите узнать счёт введите "с".')
        user_ball = 0
        rand_ball = 0
        while True:
            user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
            list_play = ['к', 'н', 'б']
            if user in list_play:
                rand = random.choice(list_play)
                print(rand)

                if rand == 'к' and user == 'н':
                    rand_ball += 1
                if rand == 'к' and user == 'б':
                    user_ball += 1
                if rand == 'н' and user == 'к':
                    user_ball += 1
                if rand == 'н' and user == 'б':
                    rand_ball += 1
                if rand == 'б' and user == 'н':
                    user_ball += 1
                if rand == 'б' and user == 'к':
                    rand_ball += 1
            elif user == 'с':
                print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            elif user == '-':
                print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
                print('Конец игры! Заходите ещё!')
                break
            else:
                print('Вводите к, н или б')



    else:
        print('Ошибка, запустите программу и введите "+".')

   elif num_pl == 3:
    x = randint(1, 10)
    attempt = 0

    while True:
        print("Я загадал число от 1 до 10, угадай его :)")
        user_num = int(input("Ваша догадка: "))
        attempt += 1
        if user_num == x:
            print(f"Ты угадал число, молодец!\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
            break
        elif user_num > x:
            print("Моё число меньше.")
        elif user_num < x:
            print("Моё число больше")

   elif num_pl == 4:
    HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |    |
         | 
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |   
         |     
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |   
         |   
         ----------
        """
    )

    max_wrong = len(HANGMAN) - 1
    WORDS = ("ананас","абрикос","апельсин","банан","бирка","бензин","ваза","вопрос","вода","гриб","гора","герой","дом","деревня","дерево","ель","ежевика","енот","ёж","ёлка","ёмкость","жираф","журнал","жук","зонт","звезда","заяц","ива","икра","искра","йод","йогурт","йога","кот","книга","карандаш","лиса","лампа","лес","медведь","мяч","мир","облако","осень","огонь","пенал","петух","парк","ракета","рыба","рука","солнце","собака","стол","тигр","тетрадь","топор","утро","утка","ученик","фонарь","флаг","филин","хлеб","художник","хор","цирк","цветок","цапля","чашка","часы","человек","шар","щкола","шишка","щётка","щука","щит","эхо","этаж","эра","юла","юг","юпитер","яблоко","ягода","язык")

    word = choice(WORDS) 
    so_far = "_" * len(word) 
    wrong = 0  
    used = []  

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong]) 
        print("\nВы использовали следующие буквы:\n", used)
        print("\nНа данный момент слово выглядит так:\n", so_far)

        guess = input("\n\nВведите свое предположение: ")

        while guess in used:
            print("Вы уже вводили букву", guess)  
            guess = input("Введите свое предположение: ") 

        used.append(guess) 
        if guess in word: 
            print("\nДа!", guess, "есть в слове!")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
    
        else:
            print("\nИзвините, буквы \"" + guess + "\" нет в слове.") 
            wrong += 1
    
    if wrong == max_wrong: 
        print(HANGMAN[wrong])
        print("\nТебя повесили!")
    else:
        print("\nВы угадали слово!")
    
    print("\nЗагаданное слово было \"" + word + '\"')
    
   else:
      print("Ошибка!")