import pygame
import random
from pygame import *
from pygame.locals import *

#Розширення вікна
WIDTH, HEIGHT = 800, 700

#Розширення ігрового поля
MAP_SIZE = 30
ROWS, COLS = 21,10

mixer.init()
#Музика під час гри
pygame.mixer.music.load('music_efects/menu_music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)#Гучність
#Звукові ефекти
remove_row_music = pygame.mixer.Sound('music_efects/remove_row.mp3')
congratulations_music = pygame.mixer.Sound('music_efects/congratulations.mp3')
game_over_music = pygame.mixer.Sound('music_efects/game_over.mp3')
game_over_music.set_volume(0.2)#Гучність
congratulations_music.set_volume(0.3)

#Кольори
GRAY = (128, 128, 128) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

#Загрузка зображень
frame = image.load('images/frame.png')
bg_game = image.load('images/game_bg.png')
control_settings_bg = image.load('images/control_settings_bg.png')

#Клас для спрайтів
class Sprite(sprite.Sprite): #назва класу
    def __init__(self,sprite_img,width,height,x,y): #властивотсі
        super().__init__()
        self.image = transform.scale(sprite_img,(width,height)) #розширення спрайтів
        self.rect = self.image.get_rect() #отримання значення
        self.rect.x = x #присвоєння значення x
        self.rect.y = y #присвоєння значення y
        
#Клас для зображень
class Images(sprite.Sprite):#назва класу
    def __init__(self, filename, x, y, speed, w, h):#властивотсі
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect() #отримання значення
        self.rect.x = x #присвоєння значення x
        self.rect.y = y #присвоєння значення y
        
#Відтворення зображень   
    def reset(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Клас для кнопок
class Button:
    def __init__(self, text, x, y, width, height, text_color, font_size):#властивості
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.font_size = font_size
#Відтворення кнопок
    def reset(self, window):
        font = pygame.font.Font('fonts/arcade.TTF', self.font_size)
        text_render = font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        window.blit(text_render, text_rect)
        
#Клас для заголовків
class Title(Button):
    def __init__(self, text, x, y, width, height, text_color, font_size):
        super().__init__(text, x, y, width, height, text_color, font_size) #Прийняття спадку класу "Button"
#Відтворення заголовків
    def reset(self, window):
        font = pygame.font.Font('fonts/gomarice_mix_bit_font.ttf', self.font_size)
        text_render = font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        window.blit(text_render, text_rect)

#Клас для рамки
class Frame(Sprite):
    def __init__(self, sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        
frame = Frame(frame,340,670,210,10)

#Створення блоків за допомогою "матриці"        
def create_blocks():
    blocks = [
        [[1,1],
         [1,1]],

        [[2,2]],

        [[3,3,3]],

        [[4]],

        [[5,5,5,5]],

        [[6,6,6],
         [0,6,0]], #0 це пусте поле ,а 6 буде відповідати за частину блоку

        [[7,7,7],
         [0,0,7]],

        [[8,8,8],
         [0,0,8],
         [0,0,8]],

        [[9,9,9],
         [9,0,0]],

        [[10,10,10],
         [10,0,0],
         [10,0,0]],

        [[11,11,11],
         [11,11,11],
         [11,11,11]],

        [[12,12],
         [12,0]],

        [[13,13],
         [0,13]],

        [[14,14],
         [0,14],
         [0,14]],

        [[15,15],
         [15,0],
         [15,0]],

        [[16,0,0],
         [16,16,16]],

        [[0,17,0],
         [17,17,17]],

        [[0,0,18],
         [18,18,18]],

        [[19,0,0],
         [19,0,0],
         [19,19,19]],

        [[0,0,20],
         [0,0,20],
         [20,20,20]],

        [[21,0],
         [21,0],
         [21,21]],

        [[0,0,22],
         [0,0,22],
         [22,22,22]],
        
        [[23],
         [23],
         [23]],
        
        [[24],
         [24]]
    ]
    #Випадковий вибір блоку
    return random.choice(blocks)

#Відтворення ігрового поля
def draw_board(window, board, current_block, current_row, current_col, block_color,points=0, best_result=0):
    window.blit(frame.image, (frame.rect.x, frame.rect.y))
    font = pygame.font.Font('fonts/arcade.ttf', 39)
    points_lb = font.render('POINTS', True, (255, 255, 255))
    points_value_lb = font.render(str(points), True, (255, 255, 255))
    best_result_lb = font.render('BEST  RESULT', True, (255, 255, 255))
    best_result_value_lb = font.render(str(best_result), True, (255, 255, 255))
    window.blit(points_lb,(575,30))
    window.blit(points_value_lb,(575,80))
    window.blit(best_result_lb,(575,160))
    window.blit(best_result_value_lb,(575,210))
    #Обробка рядів в довжину і ширину
    for row in range(ROWS):
        for col in range(COLS):
            #Коли поле пусте (заповнене 0),відтворюється ігрове поле на таких координатах
            if board[row][col] != 0:
                pygame.draw.rect(window, block_color[board[row][col]], (col * MAP_SIZE + 230, row * MAP_SIZE + 20, MAP_SIZE, MAP_SIZE ))
                pygame.draw.rect(window, BLACK, (col * MAP_SIZE + 230, row * MAP_SIZE+20, MAP_SIZE , MAP_SIZE), 4)
    if current_block:
        #Обробка списку блоків
        for i in range(len(current_block)):
            for j in range(len(current_block[i])):
                if current_block[i][j] != 0:
                    #Відтворення блоку на певних координатах з випадковим кольром
                    pygame.draw.rect(window, block_color[current_block[i][j]]  , ((current_col + j) * MAP_SIZE + 230, (current_row + i) * MAP_SIZE + 20, MAP_SIZE , MAP_SIZE))
                    pygame.draw.rect(window, WHITE, ((current_col + j) * MAP_SIZE + 230 , (current_row + i) * MAP_SIZE +20, MAP_SIZE , MAP_SIZE), 3)
    pygame.display.update()
    
#Створення пустого поля
def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

#Перевірка чи може блок рухатися 
def can_move(block, board, row, col):
    #Обробка списку блоків
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != 0:
                #Встановлення обмеження пересування блоків
                if row + i >= ROWS or col + j < 0 or col + j >= COLS or board[row + i][col + j] != 0:
                    return False
    return True

#Оновлення ігрового поля
def update_board(block, row, col, board):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != 0:
                if row + i >= 0 and row + i < ROWS and col + j >= 0 and col + j < COLS:
                    board[row + i][col + j] = block[i][j]
    return board

#Видалення заповнених рядів
def remove_rows(board):
    fill_rows = [row for row in range(ROWS) if 0 not in board[row]]
    #Пошук повних рядів(в ширину)
    for row in fill_rows:
        del board[row]
        board.insert(0, [0] * COLS)#Повернення ряду 0 значень
        remove_row_music.play()
    return len(fill_rows)

#Відтворення екрану "settings_pause"
def draw_settings_pause(window,sound_play):
    font = pygame.font.Font('fonts/arcade.ttf', 65)
    music_lb = font.render('M U S I C ', True, (255, 255, 255))
    on_music_lb = font.render('ON',True,(255, 255, 255))
    off_music_lb = font.render('OFF',True,(255, 255, 255))
    window.blit(music_lb , (155,266))
    if sound_play:
        #Коли музика грає чи не грає відбувається відображення даних текстів
        pygame.mixer.music.unpause()    
        window.blit(on_music_lb , (385,266))
    else:
        pygame.mixer.music.pause()
        window.blit(off_music_lb , (385,266))

#Відтвоерння екарну "control_settings"
def draw_control_settings(window):
    window.blit(control_settings_bg ,(0,0))
    font = pygame.font.Font('fonts/arcade.ttf', 65)
    right_move_text = font.render('            Move right',True,(255,255,255))
    left_move_text = font.render('            Move left', True ,(255,255,255))
    turn_move_text = font.render('            Turn 90 degrees',True,(255,255,255))
    window.blit(right_move_text , (170,180))
    window.blit(left_move_text, (170,280))
    window.blit(turn_move_text , (170,380))

#Відтворення екрану "restart"
def draw_restart_stop(window,text_font,mini_text_font,points = 0):
    game_over_text = text_font.render("GAME  OVER",True,WHITE)
    restart_text = mini_text_font.render("Press  SPACE  to  restart",True,WHITE)
    menu_text = mini_text_font.render("Press  ESCAPE  to  enter  the  menu ",True,WHITE)
    final_points_text = text_font.render('POINTS    ' + str(points), True, WHITE)
    window.blit(final_points_text , (190 , 470))
    window.blit(game_over_text, (210, 160))
    window.blit(restart_text, (130, 270))
    window.blit(menu_text,(70,370))
    
#Оновлення балів
def update_points(new_score):
    points = get_max_score()
    #Відкриття файлу та запис резултати
    with open('results', 'w') as file:
        if new_score > points:
            file.write(str(new_score))
        else:
            file.write(str(points))

#Отримання найкращого результату
def get_max_score():
    with open('results', 'r') as file:
        lines = file.readlines()        
        points = int(lines[0].strip())   

    return points 

#Встановлення складності гри
def levels(points,fall_time,clock):
    #При певній к-сті балів ,швидкість падіння блоку буде збільшуватися 
    if points >= 300:
        fall_time = 0.8
    if points >= 700:
        fall_time = 1.3
    if points >= 1000:
        fall_time = 1.6
    if points >= 1500:
        fall_time = 2.0
    if points >= 2000:
        fall_time = 2.5

#Відтворення екрану "new_best_result"
def new_best_result(window,text_font,best_result=0):
    new_best_result_text = text_font.render('New  Best  Result ' + str(best_result),True,YELLOW)
    congratulations_text = text_font.render('CONGRATULATIONS',True,YELLOW)
    window.blit(congratulations_text , (112 , 160))
    window.blit(new_best_result_text , (80,310))
    congratulations_music.play()

def start(window,text_font):
    window.fill(GRAY)
    start_text = text_font.render('PRESS   F   TO   START',True,WHITE)
    window.blit(start_text,(200,310) )
    

# #відтворення екарану "about"
# def draw_about(window):
#     fonts = pygame.font.Font("fonts/Freeman-Regular.ttf",22)
#     fonts2 = pygame.font.Font("fonts/Freeman-Regular.ttf",30)
#     text_1 = fonts2.render("Hello,my name is Denys!",True,WHITE)
#     text_2 = fonts.render("This game is a copy of Tetris developed by me on paygame.",True,WHITE)
#     text_3 = fonts.render("This project will be presented at the competition created by the Logica school.",True,WHITE)    
#     text_4 = fonts.render("For me, this is the first experience of developing such games, even independently.",True,WHITE)
#     text_5 = fonts.render("I hope you enjoyed it because it gives me strength to study hard.",True,WHITE)
#     text_7 = fonts2.render("Inst Denys_Makukh",True,WHITE)
#     text_8 = fonts.render("Tetris is a well-known block-based puzzle game in which you swop",True,WHITE)
#     text_9 = fonts.render("making solid horizontal lines with falling blocks or tetrominos",True,WHITE)
#     text_10 = fonts.render("Rotate and move the falling tetrominoes to match them with the tier lines of the stack",True,WHITE)
#     text_11= fonts.render("and preventing it from touching the top of the screen",True,WHITE)
#     window.blit(text_1,(230,120))
#     window.blit(text_2,(130,170))
#     window.blit(text_3,(75,220))
#     window.blit(text_4,(65,270))
#     window.blit(text_5,(110,320))
#     window.blit(text_7 , (20,640))
#     window.blit(text_8 , (100,380))
#     window.blit(text_9 , (110, 430))
#     window.blit(text_10, (30, 480))
#     window.blit(text_11, (130, 530))

#Головні змінні ,значання і т.д
def main(): 
    #Sound_play набуває змінної "глобальних змін"
    global sound_play  
    
    #Бали
    points = 0
    best_result = get_max_score()
    
    #Імпорт всіх модулів
    pygame.init()
    
    #Вікно та ігрове поле
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris - Denys Makukh")
    clock = pygame.time.Clock()
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    #Шрифти
    TEXT_FONT = pygame.font.Font('fonts/arcade.ttf',70)
    MINI_TEXT_FONT = pygame.font.Font('fonts/arcade.ttf',45)
    #Кольори контурів та блоків
    block_color = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(25)]
    line_color = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(25)]
    
    #Екран "pause"
    pause_bg = Images('images/pause_bg.png',0,0,0,800,800)
    menu_pause_btn = Button("M E N U", 300, 120, 150, 150, BLACK, 65) 
    quit_pause_btn = Button("Q  U  I  T", 40 , 560 , 150 , 150 , BLACK ,65)
    continue_pause_btn = Button("C O N T I N U E", 300 , 390 , 150 , 150 , BLACK ,65)
    settings_pause_btn = Button("S E T T I N G S", 300, 220, 150, 150, BLACK, 65) 
    pause_title = Title( " P A U S E ",260,-5 ,220,170 , YELLOW , 80)
    restart_pause_btn = Button("R  E S T A R  T", 310, 300, 150, 150, BLACK, 65) 
    
    #Екран "menu"
    menu_bg = Images('images/menu_bg.png',0,0,0,800,700)
    btn_play = Button(" S  t  a  r  t", 270, 170, 220, 170, WHITE, 75)
    quit_menu_btn = Button("Q  U  I  T", 40 , 560 , 150 , 150 , WHITE ,65)
    btn_settings = Button("S  E  T  T  I  N  G  S", 275, 290, 220, 170, WHITE, 72)
    btn_title = Title(" T  E  T  R  I  S", 255, 2, 220, 170, BLACK, 75) 
    about_btn = Button(" A  B  O  U T ",275,410,220,170,WHITE,75)
    
    #Екран "control_settings"
    left_move_img = Images('images/control_left.png',135,280,0,70,65)
    new_best_result_bg = Images('images/new_best_result_menu.png',0,0,0,800,700)
    right_move_img = Images('images/control_right.png',135,180,0,70,65)
    turn_move_img = Images('images/control_turn.png',135,380,0,70,65)
    control_settings_btn = Button("C O N T R O L", 282, 320, 150, 150, WHITE, 65)
    control_settings_title = Title("C O N T R O L", 278, 2, 220, 170, YELLOW, 75)
    
    #Екран "menu_settings" та "pause_settings"
    settings_menu_title = Title( "S E T T I N G S",270,-5 ,220,170 , YELLOW , 80)
    settings_menu_bg = Images('images/settings_menu_bg.png',0,0,0,800,700)
    settings_bg = Images('images/settings.png',0,0,0,800,800)
    on_volume_btn = Images('images/soundOnWhite.png',495,264,0,63,63)
    off_volume_btn = Images('images/soundOffWhite.png',495,264,0,63,63)
    menu_settings_btn = Button("M  E  N  U", 290, 450, 150, 150, WHITE, 65)  
    
    #Екран "restart"
    game_over_bg = Images('images/game_over_bg.png',0,0,0,800,700)   
    
    #Екран "run"
    btn_pause = Button("P A U S E", 65, 15, 70, 70, YELLOW, 60)
    gray_bg = Images('images/gray_bg.jpg',220,30,0,310,650)
    
    #Екран "new_best_result"
    quit_new_best_result_btn = Button("Q  U  I  T", 40 , 500 , 150 , 150 , YELLOW ,60)
    menu_new_best_result_btn = Button("M E N U", 270 , 500 , 150 , 150 , YELLOW ,60)
    restart_new_best_result_btn = Button("R E S T A R T", 550 , 500 , 150 , 150 , YELLOW ,60)
    
    #Екран "about"
    return_about_btn = Button("R E T U R N",290,530,150,150,WHITE,60)
    about_title = Title("A B O U T", 280, -30, 220, 170, YELLOW, 75)
    about_bg = Images("images/about_bg.png",0,0,0,800,700)
    
    #Кнопка ,яка використовується на багатьох екранах
    return_btn = Button("R E T U R N", 285, 460, 150, 150, WHITE, 65)
    
    #Початкові значення
    sound_play = True 
    volume_changed = False
    run = True
    current_block = None
    current_row, current_col = 0, 0
    fall_time = 0
    screen = 'menu'
    while run:
        if screen == 'menu':            
            #Візуальна частина екрану "menu"
            pygame.time.wait(1000)
            menu_bg.reset(window)
            btn_play.reset(window)
            btn_settings.reset(window)
            btn_title.reset(window)
            quit_menu_btn.reset(window)
            about_btn.reset(window)
            
            #Обробка подій на екрані 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    
                    #Коли мишка попадає на координати кнопки відбувається певна подія
                    if btn_play.x <= x <= btn_play.x + btn_play.width and btn_play.y <= y <= btn_play.y + btn_play.height:
                        screen = 'start'
                        
                    if btn_settings.x <= x <= btn_settings.x + btn_settings.width and btn_settings.y <= y <= btn_settings.y + btn_settings.height:
                        screen = 'menu_settings'
                        
                    if about_btn.x <= x <= about_btn.x + about_btn.width and about_btn.y <= y <= about_btn.y + about_btn.height:
                        screen = 'about'
                        
                    if quit_menu_btn.x <= x <= quit_menu_btn.x + quit_menu_btn.width and quit_menu_btn.y <= y <= quit_menu_btn.y + quit_menu_btn.height:
                        run = False
                        
            pygame.display.update()

        if screen == 'start':
            start(window,pygame.font.Font('fonts/arcade.TTF', 55))
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            if keys[pygame.K_f]:    
                screen = 'run'
            pygame.display.update()
        #Візуальна частина екрану "run"
        if screen == 'run':
            window.blit(bg_game,(0,0))
            gray_bg.reset(window)    
            btn_pause.reset(window)   
            levels(points,fall_time,clock)
            draw_board(window, board, current_block, current_row, current_col, block_color,points,best_result)
            
            #Створення нового блоку
            if current_block is None:
                current_block = create_blocks()
                current_row = 0
                current_col = random.randint(0, COLS - len(current_block[0])) #випадковий спавн блоку по x
                points += remove_rows(board) * 100 #бали дорівнюють видаленим рядам та помноженим на 100
                update_points(points)         
                
            #Коли блок не може рухатися відтворюється екран "restart"    
            if not can_move(current_block, board, current_row, current_col):
                screen = 'restart'
                game_over_music.play()
                
            #Обробка подій на клавіатурі та набутті руху при нажаті на певну кнопку
            key_pressed = pygame.key.get_pressed()
            
            if key_pressed[pygame.K_LEFT] and current_col > 0 and can_move(current_block, board, current_row, current_col - 1):
                current_col -= 1 #рух вліво
                
            if key_pressed[pygame.K_DOWN] and current_col > 0 and can_move(current_block, board, current_row, current_col - 1):
                current_row += 1 #рух вниз   
                
            if key_pressed[pygame.K_RIGHT] and current_col + len(current_block[0]) < COLS and can_move(current_block, board, current_row, current_col + 1):
                current_col += 1 #рух вправо
                
            if key_pressed[pygame.K_UP] and current_col + len(current_block[0]) < COLS and can_move(current_block, board, current_row, current_col + 1):
                current_block = list(zip(*current_block[::-1])) #поворот блоку
                
            #Якщо блок може рухатися то він падає
            if can_move(current_block, board, current_row + 1, current_col):
                current_row += 1 
            else:
                board = update_board(current_block, current_row, current_col, board)
                current_block = None
            fall_time += clock.tick(5) / 1000 #початкова швидкість падіння
            
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if btn_pause.x <= x <= btn_pause.x + btn_pause.width and btn_pause.y <= y <= btn_pause.y + btn_pause.height:
                        screen = 'pause'
                        
            pygame.display.update()
            
        #Візуальна частина екарну "menu_settings"
        if screen == 'menu_settings':
            settings_menu_bg.reset(window)
            settings_menu_title.reset(window)
            menu_settings_btn.reset(window)
            control_settings_btn.reset(window)
            draw_settings_pause(window,sound_play)
            
            #Зміна положення музики
            if sound_play:
                on_volume_btn.reset(window)
                if volume_changed:
                    off_volume_btn.kill()  # Видаляємо кнопку вимкненого звуку
                    volume_changed = False
            else:
                off_volume_btn.reset(window)
                if volume_changed:
                    on_volume_btn.kill()  # Видаляємо кнопку включеного звуку
                    volume_changed = False
                    
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if menu_settings_btn.x <= x <= menu_settings_btn.x + menu_settings_btn.width and menu_settings_btn.y <= y <= menu_settings_btn.y + menu_settings_btn.height:
                        screen = 'menu'
                        points = 0
                        
                    #Включення/виключення музики
                    if on_volume_btn.rect.x <= x <= on_volume_btn.rect.x + on_volume_btn.rect.width and on_volume_btn.rect.y <= y <= on_volume_btn.rect.y + on_volume_btn.rect.height:
                        sound_play = not sound_play
                        volume_changed = True
                        if sound_play:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    if control_settings_btn.x <= x <= control_settings_btn.x + control_settings_btn.width and control_settings_btn.y <= y <= control_settings_btn.y + control_settings_btn.height:
                        screen = 'control_settings'
            pygame.display.update()

        #Візуальна частина екрану "control_settings"
        if screen == 'control_settings':
            draw_control_settings(window)
            control_settings_title.reset(window)
            left_move_img.reset(window) 
            right_move_img.reset(window)
            turn_move_img.reset(window)
            return_btn.reset(window)
            
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if return_btn.x <= x <= return_btn.x + return_btn.width and return_btn.y <= y <= return_btn.y + return_btn.height:
                        screen = 'menu_settings'
            pygame.display.update()
            
#Візульна частина екрану "pause"
        if screen == 'pause':
            pause_bg.reset(window)
            menu_pause_btn.reset(window)
            settings_pause_btn.reset(window)
            continue_pause_btn.reset(window)
            pause_title.reset(window)
            quit_pause_btn.reset(window)
            restart_pause_btn.reset(window)
            
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if settings_pause_btn.x <= x <= settings_pause_btn.x + settings_pause_btn.width and settings_pause_btn.y <= y <= settings_pause_btn.y + settings_pause_btn.height:
                        screen = 'settings_pause'
                        
                    if menu_pause_btn.x <= x <= menu_pause_btn.x + menu_pause_btn.width and menu_pause_btn.y <= y <= menu_pause_btn.y + menu_pause_btn.height:
                        screen = 'menu'
                        board = create_board() #поле оновлюється
                        current_block = None #блоки не створюються
                        points = 0
                        
                    if continue_pause_btn.x <= x <= continue_pause_btn.x + continue_pause_btn.width and continue_pause_btn.y <= y <= continue_pause_btn.y + continue_pause_btn.height:
                        screen = 'run'
                        
                    if quit_pause_btn.x <= x <= quit_pause_btn.x + quit_pause_btn.width and quit_pause_btn.y <= y <= quit_pause_btn.y + quit_pause_btn.height:
                        run = False
                        
                    if restart_pause_btn.x <= x <= restart_pause_btn.x + restart_pause_btn.width and restart_pause_btn.y <= y <= restart_pause_btn.y + restart_pause_btn.height:
                        screen = 'run'
                        current_block = None
                        board = create_board()
                        points = 0
                        
            pygame.display.update()
            
        #Візуальна частина екрану "settings_pause"
        if screen == "settings_pause":
            settings_bg.reset(window)
            settings_menu_title.reset(window)
            return_btn.reset(window)
            draw_settings_pause(window,sound_play)
            control_settings_btn.reset(window)
            
            #Зміна положення музики
            if sound_play:
                on_volume_btn.reset(window)
                if volume_changed:
                    off_volume_btn.kill()  # Видаляємо кнопку вимкненого звуку
                    volume_changed = False
            else:
                off_volume_btn.reset(window)
                if volume_changed:
                    on_volume_btn.kill()  # Видаляємо кнопку включеного звуку
                    volume_changed = False
                    
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if on_volume_btn.rect.x <= x <= on_volume_btn.rect.x + on_volume_btn.rect.width and on_volume_btn.rect.y <= y <= on_volume_btn.rect.y + on_volume_btn.rect.height:
                        sound_play = not sound_play
                        volume_changed = True
                        if sound_play:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    if return_btn.x <= x <= return_btn.x + return_btn.width and return_btn.y <= y <= return_btn.y + return_btn.height:
                        screen = 'pause'
                        
                    if control_settings_btn.x <= x <= control_settings_btn.x + control_settings_btn.width and control_settings_btn.y <= y <= control_settings_btn.y + control_settings_btn.height:
                        screen = 'control_settings'
                        
            pygame.display.update()

        #Візуальна частина екрану "restart"
        if screen == 'restart':
            board = create_board()
            game_over_bg.reset(window)
            draw_restart_stop(window, TEXT_FONT, MINI_TEXT_FONT,points)
            
            #Оновлення нового найкращого результати
            if best_result < points:
                best_result = points
                screen = 'new_best_result'
                congratulations_music.play()
                
            #Обробка подій на клавіатурі при нажатті на певну кнопку
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                board = create_board()  
                points = 0
                screen = 'run'
                pygame.time.wait(900)
            elif keys[pygame.K_ESCAPE]:
                board = create_board()  
                points = 0
                screen = 'menu'
                
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            pygame.display.update()
        
        #Візуальна чатисна екарну "new_best_result"
        if screen == 'new_best_result':
            new_best_result_bg.reset(window)
            new_best_result(window,TEXT_FONT,best_result)
            quit_new_best_result_btn.reset(window)
            menu_new_best_result_btn.reset(window)
            restart_new_best_result_btn.reset(window)
            
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if quit_new_best_result_btn.x <= x <= quit_new_best_result_btn.x + quit_new_best_result_btn.width and quit_new_best_result_btn.y <= y <= quit_new_best_result_btn.y + quit_new_best_result_btn.height:
                        run = False
                        
                    if menu_new_best_result_btn.x <= x <= menu_new_best_result_btn.x + menu_new_best_result_btn.width and menu_new_best_result_btn.y <= y <= menu_new_best_result_btn.y + menu_new_best_result_btn.height:
                        screen = 'menu'
                        board = create_board()
                        current_block = None
                        points = 0
                        
                    if restart_new_best_result_btn.x <= x <= restart_new_best_result_btn.x + restart_new_best_result_btn.width and restart_new_best_result_btn.y <= y <= restart_new_best_result_btn.y +restart_new_best_result_btn.height:
                        screen = 'run'
                        board = create_board()
                        current_block = None
                        points = 0
                        
            pygame.display.update()
            
        #Візуальна частина екрану "about"
        if screen == 'about':
            about_bg.reset(window)
            return_about_btn.reset(window)
            about_title.reset(window)
            # draw_about(window)
            
            #Обробка подій на екрані             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                #Обробка подій на кліці мишки
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos 
                    if return_about_btn.x <= x <= return_about_btn.x + return_about_btn.width and return_about_btn.y <= y <= return_about_btn.y + return_about_btn.height:
                        screen = 'menu'
                        
            pygame.display.update()
            
        #Сам колір вікна є сірим
        window.fill(GRAY)
    pygame.quit()

if __name__ == "__main__":
    main()
