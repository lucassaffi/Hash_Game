import pygame
class hash_game:
    #Initialize and create the fundamental variables of the game
    def __init__(self):
        print('O jogo comecou!')
        self.plays = []
        self.winning_plays = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.plays_player_A = []
        self.plays_player_B = []
        self.turn = 0
        self.close_screen = False
        self.end_game = False
        self.end_turn = False
        self.clicked = False
        self.run()

    #Verify if the selected quadrant has already been selected
    def check_play(self,jogada):
        if (jogada in self.plays)==False:
            return 0
        else:
            return 1

    #Determine the configurations of the screen
    def config_screen(self,screen_size,icon_size,screen_color):
        #Initialize pygame
        pygame.init()
        #Determine the dimensions of the screen
        width = screen_size[0]
        height = screen_size[1]
        #Create screen
        screen = pygame.display.set_mode((width,height))
        #Set title of the screen
        pygame.display.set_caption('My Game')
        #Set quadrant's boundaries
        q1 = [(0,0),(int(width/3),int(height/3))]
        q2 = [(int(width/3),0),(int(2*width/3),int(height/3))]
        q3 = [(int(2*width/3),0),(int(width),int(height/3))]
        q4 = [(0,int(height/3)),(int(width/3),int(2*height/3))]
        q5 = [(int(width/3),int(height/3)),(int(2*width/3),int(2*height/3))]
        q6 = [(int(2*width/3),int(height/3)),(int(width),int(2*height/3))]
        q7 = [(0,int(2*height/3)),(int(width/3),int(height))]
        q8 = [(int(width/3),int(2*height/3)),(int(2*width/3),int(height))]
        q9 = [(int(2*width/3),int(2*height/3)),(int(width),int(height))]
        quadrant_list = [[q1,1],[q2,2],[q3,3],[q4,4],[q5,5],[q6,6],[q7,7],[q8,8],[q9,9]]
        #Set icon's size
        icon_size = icon_size
        #Load and resize icons. Replace the path of these icons.
        player_A_icon = pygame.image.load('C:\\Users\\lucas\\OneDrive\\ML\\Tests\\Hash_Game\\Images\\close.png')
        player_A_icon = pygame.transform.scale(player_A_icon,(icon_size,icon_size))
        player_B_icon = pygame.image.load('C:\\Users\\lucas\\OneDrive\\ML\\Tests\\Hash_Game\\Images\\circle.png')
        player_B_icon = pygame.transform.scale(player_B_icon,(icon_size,icon_size))
        #Set screen's color
        screen.fill((screen_color[0],screen_color[1],screen_color[2]))
        #Draw lines
        pygame.draw.line(screen, (0,0,0),(int(width/3),0),(int(width/3),height),6)
        pygame.draw.line(screen, (0,0,0),(int(2*width/3),0),(int(2*width/3),height),6)
        pygame.draw.line(screen, (0,0,0),(0,int(height/3)),(width,int(height/3)),6)
        pygame.draw.line(screen, (0,0,0),(0,int(2*height/3)),(width,int(2*height/3)),6)
        pygame.display.update()

        return screen_size,screen,icon_size,player_A_icon,player_B_icon,quadrant_list

    def processo_jogada(self,screen,plays_player,quadrant_list,jogador_icone,icon_size):

        #Idenifies when some button is clicked
        for event in pygame.event.get():
            #Finish game and the screen
            if event.type == pygame.QUIT:
                self.close_screen = True
                self.end_game = True
                self.end_turn = True
                self.clicked = True
                print('O jogo terminou')
            #Execute a play
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                click = [x,y]
                for j in quadrant_list:
                    if x>j[0][0][0] and x<j[0][1][0] and y>j[0][0][1] and y<j[0][1][1]:
                        #Check if the play has already been done. if one, is has not.
                        check = self.check_play(j[1])
                        if check == 0:
                            self.plays.append(j[1])
                            plays_player.append(j[1])
                            self.end_turn = True
                            self.clicked = True
                            self.turn = self.turn + 1
                            screen.blit(jogador_icone,(j[0][0][0]+int((j[0][1][0]-j[0][0][0])/2)-int(icon_size/2),j[0][0][1]+int((j[0][1][1]-j[0][0][1])/2)-int(icon_size/2)))
                            pygame.display.update()

                            #Identify if the player won
                            for a in plays_player:
                                for b in plays_player:
                                    for c in plays_player:
                                        if [a,b,c] in self.winning_plays:
                                            #Identify the quadrants that resulted the victory
                                            quadrant_winner_list = []
                                            for k in quadrant_list:
                                                if k[1] == a or k[1] == b or k[1] == c:
                                                    quadrant_winner_list.append(k[1])
                                            #Set the winning line position
                                            for m in quadrant_list:
                                                if m[1] == min(quadrant_winner_list):
                                                    x_min = int((m[0][1][0]+m[0][0][0])/2)
                                                    y_min = int((m[0][1][1]+m[0][0][1])/2)
                                                elif m[1] == max(quadrant_winner_list):
                                                    x_max = int((m[0][1][0]+m[0][0][0])/2)
                                                    y_max = int((m[0][1][1]+m[0][0][1])/2)

                                            #Draw the winning line
                                            pygame.draw.line(screen, (255,0,0),(x_min,y_min),(x_max,y_max),5)
                                            pygame.display.update()

                                            #Print the winner
                                            if plays_player == self.plays_player_A:
                                                print('Player A won!')
                                            elif plays_player == self.plays_player_B:
                                                print('Player B won!')

                                            #Finish the game
                                            self.end_game = True
                                            self.end_turn = True
                                            self.clicked = True
                        else:
                            print('Escolha outra jogada')


    #Run the game
    def run(self):
        #Configure the screen and icons of the players
        screen_size,screen,icon_size,player_A_icon,player_B_icon,quadrant_list = self.config_screen((600,600),50,(255,255,255))

        self.close_screen = False
        #While the screen is not closed
        while self.close_screen == False:
            #Identify when the quit button is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_screen = True
            #While the game has not finished
            while self.end_game == False:
                self.end_turn = False
                #While the turn is not finished
                while self.end_turn == False:
                    if self.turn%2 == 0:
                        self.clicked = False
                        #While the play has not been chosen by the player
                        while self.clicked == False:
                            cont = self.processo_jogada(screen,self.plays_player_A,quadrant_list,player_A_icon,icon_size)
                    else:
                        self.clicked = False
                        #While the play has not been chosen by the player
                        while self.clicked == False:
                            cont = self.processo_jogada(screen,self.plays_player_B,quadrant_list,player_B_icon,icon_size)

game = hash_game()
