from random import randint
import os
import time
#from pygame import mixer
import pygame

def nauber():
    os.system('clear')
    print('                                  @@@@@@@@@@@@@@@@@@@@@@@@@.    %@(..%@@@@@@@@@@@@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                  @@@@@@@@@@@@@@@@@@&..  .  .   .       .,&@@@@@@@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                  @@@@@@@@@@@@@&&(.... . ..              .       (@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                  @@@@@@@@@@@&       .            ..     .  .      ,@@@@@@@@@')
    time.sleep(0.1)
    print('                                  @@@@@@@@@@ ...         .  ..                      .#@@@@@@@')
    time.sleep(0.1)
    print('                                  @@@@@@@%.   .          . .                 ..   . ...**%@@@')
    time.sleep(0.1)
    print('                                  @@@@@@(   .. .                .                .  ..   . @@')
    time.sleep(0.1)
    print('                                  @@@@@@            ..             .,    .. .            ,./@')
    time.sleep(0.1)
    print('                                  @@@@@/            .     ... .       .  .    .      .   .. *')
    time.sleep(0.1)
    print('                                  @@@@&           .  ..,,**,,,...,  , ..  .              .. *')
    time.sleep(0.1)
    print('                                  @@@%     .      .,***,/((((((///(/*..,   .  .            .,')
    time.sleep(0.1)
    print('                                  @@@         ...,,,*/*./((##########(*,...,.         .     ,')
    time.sleep(0.1)
    print('                                  @@,         .,,**//,,/################//((/**...     .    .')
    time.sleep(0.1)
    print('                                  @@         .,*/((((#(###%#%%%%%%%%######(((((/,,.  ...    .')
    time.sleep(0.1)
    print('                                  @%.       ,*/(((((###%%%#%%%%%%%%%%%#######(#((/*. .    .. ')
    time.sleep(0.1)
    print('                                  @/       ,*(((((((((((######%%%%%%##%#########((/*.        ')
    time.sleep(0.1)
    print('                                  @/,.  ../(((((*,......,,,(###%%%%%%%%%%%#####(((/*  .      ')
    time.sleep(0.1)
    print('                                  &(/   ./(#####(//((((##/..,,,/(#%%%%%%%%######((/* .       ')
    time.sleep(0.1)
    print('                                  (#(*  */((##%#(/*. , ,.,*(/,..,*((#(###((##(((((/*.        ')
    time.sleep(0.1)
    print('                                  (#/(..//((##%%%##((#(/*/*,*/(/((##(/,/,,,,**(/(//*,.      @')
    time.sleep(0.1)
    print('                                  #(#(.,///(###%%%%%#((###(/(////(%%#**/*,... .  .,*.      %@')
    time.sleep(0.1)
    print('                                  ###..*///(####%%%%%%%###((/((((%%%(*/,,*.,//((/. .,     (@@')
    time.sleep(0.1)
    print('                                  ##/..*//(((##%%%%%%%%%%%%%#####%%#//////*,.(*.***,*    @@@@')
    time.sleep(0.1)
    print('                                  @,...*//((((##%%%&&%%%%###%#%%%%%%(/((##(((((,*((*,   ,@@@@')
    time.sleep(0.1)
    print('                                  @.  .,/(((((###%%%####((#####%%%%##(####(((((((/(*,   &@@@@')
    time.sleep(0.1)
    print('                                  @%  .,/(((((((##(*//(#((//(#(((###(#(#%%%%%###((/,  %@@@@@@')
    time.sleep(0.1)
    print('                                  @%  ../((((###* ...,,,,, ..,/((//#(#((%%%%%%##(/*  @@@@@@@@')
    time.sleep(0.1)
    print('                                  %    .,/(#(###.,*,,,,,,. .  ., ,  .,((##%%%##(/,. @@@@@@@@@')
    time.sleep(0.1)
    print('                                       .,,/(((#/*####/***//(((.....   .*/(####(/*. #@@@@@@@@@')
    time.sleep(0.1)
    print('                                        ..,,///*,(######(//(///****/.   ./(##(/*,..@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    .    ...,,,.,*(#%###((###(///*,,,,...*#((//*..@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    ,,      .. .*,*(#%%#(*....,*/(/////.,#((/(*. @@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    **.     ....,.**/(#(/*.   ..,(((//.,/(///*. &@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    //*          ....**((((#(//(((/*,..,..... .@@@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    //**.          ..,**/,**/*/**,..  .....  .,@@@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    ////**           ......,***,.    ..         ,@@@@@@@@@@@@')
    time.sleep(0.1)
    print('                                    //(///*,      .        .....                   &@@@@@@@@@')
    time.sleep(0.1)
    print('                                   *///(///***,        .. .. .                       &@@@@@@@')
    time.sleep(0.1)
    print('                                  ,*(((//////////*.    .....  .. .                     *@@@@@')
    time.sleep(0.1)
    print('                                  **/(((((/(/////((((/*,,.      ..,*/.                   @@@@')
    time.sleep(0.1)
    print('                                  ///((((###((/((///////*///*//////*.                      @@')
    time.sleep(0.1)
    print('                                  ,(((((((########(((((((////(((//**                        @')
    time.sleep(2)
    os.system('clear')


def jogar():
    opc = 0
    while opc == 0:
        print()
        print()
        print('		███████╗██╗ ██████╗ █████╗     ███╗   ██╗ █████╗ ██╗   ██╗██████╗ ███████╗██████╗   ██╗')
        print('		██╔════╝██║██╔════╝██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗  ██║')
        print('		█████╗  ██║██║     ███████║    ██╔██╗ ██║███████║██║   ██║██████╔╝█████╗  ██████╔╝  ██║')
        print('		██╔══╝  ██║██║     ██╔══██║    ██║╚██╗██║██╔══██║██║   ██║██╔══██╗██╔══╝  ██╔══██╗  ╚═╝')
        print('		██║     ██║╚██████╗██║  ██║    ██║ ╚████║██║  ██║╚██████╔╝██████╔╝███████╗██║  ██║  ██╗')
        print('		╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═╝')
        print()
        print('		Avisos: ')
        print('		1 - todas as palavras estão em letras minúsculas.')
        print('		2 - Não há linguagens com símbolos.')
        print('		3 - Não há espaços nas palavras.')
        print('		4 - Divirta-se!.')
        print()
        pygame.init()
        pygame.mixer.music.load('musica.ogg')
        pygame.mixer.music.play()
        opc = input('		<-Pressione enter para iniciar o jogo-> ')
    pygame.mixer.music.pause()
    ling = ['java', 'php', 'python', 'ruby', 'scala', 'lua', 'haskell', 'prolog', 'julia',
            'javascript', 'dart', 'kotlin', 'delphi', 'swift', 'bash', 'clojure', 'perl', 'sql']
    tracos = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ',
              '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
    veri = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ',
            '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
    jogadas = []
    dica = 'Liguagens de programação'
    jogando = True
    letra = ''
    palavra = randint(0, (len(ling)-1))
    jogo = ling[palavra]
    jogo = list(jogo)
    teste = 0
    veri3 = []
    vidas = len(ling[palavra])

    def tela():
        print()
        os.system('clear')
        print()
        print()
        print('		 ██████╗  ██████╗     ██╗')
        print('		██╔════╝ ██╔═══██╗    ██║')
        print('		██║  ███╗██║   ██║    ██║')
        print('		██║   ██║██║   ██║    ╚═╝')
        print('		╚██████╔╝╚██████╔╝    ██╗')
        print('		 ╚═════╝  ╚═════╝     ╚═╝')
        print()
        print()
        print('		', end='')
        for i in range(0, len(ling[palavra])):
            print(tracos[i], end='')
            veri[i] = '_ '
        print()
        print()
        print('		Tentativas: ',end='')
        for bla in range(len(jogadas)):
            print(jogadas[bla],' ',end='') 
        print()
        print()
        print('		Dica: {}'.format(dica))
        print()
        print('		Vidas: {}'.format(vidas))
    tela()
    veri3 = '_'*len(ling[palavra])
    veri3 = list(veri3)
    while jogando:
        veri2 = ling[palavra]
        repete = False
        while repete == False:
            print()
            letra = input('		Digite uma letra: ')
            if letra in jogadas:
                
                print()
                print('		Letra já digitada, tente outra!')
                time.sleep(1)
                
            if not letra in str(ling[palavra]):
                if not letra in jogadas:
                    vidas -= 1
                if vidas <= 0:
                    print()
                    print('		Perdeu!!! A palavra era: {}'.format(str(ling[palavra])))
                    pygame.init()
                    pygame.mixer.music.load('erro.ogg')
                    pygame.mixer.music.play()
                    time.sleep(3)
                    os.system('clear')
                    jogar()
                if not letra in jogadas:
                    jogadas.append(letra)
                    repete = True 
                    
            for k in range(len(ling[palavra])):
                if letra == veri2[k]:
                    tracos[k] = letra+' '
                    veri3[k] = letra
            tela()
            if veri3 == jogo:
                print()
                print('		Parabéns você ganhou!!!')
                pygame.init()
                pygame.mixer.music.load('acerto.ogg')
                pygame.mixer.music.play()
                time.sleep(3)
                os.system('clear')
                jogar()

nauber()
jogar()
