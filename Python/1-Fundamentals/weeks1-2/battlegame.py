art = """

                        /\\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \\
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``


"""

play_again = True

print(art)

while play_again:

    wizard = "Wizard"
    wizard_hp = 70
    wizard_dmg = 150

    elf = "Elf"
    elf_hp = 100
    elf_dmg = 100

    human = "Human"
    human_hp = 100
    human_dmg = 150

    dragon = "Dragon"
    dragon_hp = 300
    dragon_dmg = 50


    print("Welcome to the greatest battle of all time!")
    print("You are about to take on a huge fire breathing dragon, and must choose your warrior.")

    while True:
        print(
            """
            Here are the characters you can choose from:
            1. Wizard
            2. Elf
            3. Human
            """
        )

        user_choice = int(input(
            "Choose your character and choose wisely (type the number of your choice): "))

        if user_choice == 1:
            character = wizard
            my_hp = wizard_hp
            my_dmg = wizard_dmg
            break
        elif user_choice == 2:
            character = elf
            my_hp = elf_hp
            my_dmg = elf_dmg

            break
        elif user_choice == 3:
            character = human
            my_hp = human_hp
            my_dmg = human_dmg
            break
        else:
            print("That is not a valid option")

    print(f"You have chosen character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_dmg}")


    user_ready = input("Are you ready to fight?! Type 'yes' or 'no': ").lower()
    if user_ready == "yes":
        start_game = True
    elif user_ready == "no":
        print("That is a shame... come back when you are ready.")
        start_game = False

    while start_game:
        dragon_hp -= my_dmg
        print(f"Your {character} damaged the dragon!")
        print(f"The dragons hp is now {dragon_hp}")
        if dragon_hp <= 0:
            print("The dragon was slain!")
            break
        my_hp -= dragon_dmg
        print("The dragon struck back!")
        print(f"The {character} hp is now {my_hp}")
        if my_hp <= 0:
            print(f"Your {character} died :( ")
            print("GAME OVER")
            break
    keep_playing = input("\nWould you like to play again? Type 'yes' or 'no': ").lower()
    if keep_playing != "yes":
        play_again = False
