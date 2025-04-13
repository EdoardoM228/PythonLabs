import pygame
import random
import sys

# Инициализация pygame
pygame.init()
pygame.mixer.init()

# Константы
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_PATH = "Poppins-MediumItalic.ttf" 
BG_COLOR = (230, 230, 250)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (70, 170, 70)

# Загрузка изображений и масштабирование
def load_image(name, size=(100, 100)):
    try:
        img = pygame.image.load(f"images/{name.lower()}.png")
        return pygame.transform.scale(img, size)
    except:
        # Заглушка, если изображение не найдено
        surf = pygame.Surface(size)
        surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return surf

# Элементы игры с их свойствами
ELEMENTS = {
    "Камень": {"beats": ["Ножницы", "Огонь", "Губка"], "image": "rock", "color": (128, 128, 128)},
    "Ножницы": {"beats": ["Бумага", "Губка", "Воздух"], "image": "scissors", "color": (0, 0, 255)},
    "Бумага": {"beats": ["Камень", "Воздух", "Вода"], "image": "paper", "color": (255, 255, 0)},
    "Огонь": {"beats": ["Ножницы", "Бумага", "Губка"], "image": "fire", "color": (255, 0, 0)},
    "Вода": {"beats": ["Огонь", "Камень", "Воздух"], "image": "water", "color": (0, 0, 255)},
    "Воздух": {"beats": ["Огонь", "Камень", "Вода"], "image": "air", "color": (200, 200, 255)},
    "Губка": {"beats": ["Бумага", "Воздух", "Вода"], "image": "sponge", "color": (255, 165, 0)}
}

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Расширенная Камень-Ножницы-Бумага")

# Загрузка изображений
images = {name: load_image(data["image"]) for name, data in ELEMENTS.items()}

# Шрифты
try:
    title_font = pygame.font.Font(FONT_PATH, 48)
    main_font = pygame.font.Font(FONT_PATH, 36)
    small_font = pygame.font.Font(FONT_PATH, 24)
except:
    title_font = pygame.font.SysFont("Arial", 48)
    main_font = pygame.font.SysFont("Arial", 36)
    small_font = pygame.font.SysFont("Arial", 24)

# Класс кнопки
class Button:
    def __init__(self, x, y, width, height, text, color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surf = main_font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

# Функция определения победителя
def get_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "Ничья!"
    elif ai_choice in ELEMENTS[player_choice]["beats"]:
        return "Игрок победил!"
    else:
        return "AI победил!"

# Главная функция игры
def main():
    clock = pygame.time.Clock()
    running = True
    game_state = "menu"  # menu, game, result
    
    # Игровые переменные
    player_choice = None
    ai_choice = None
    result = "Выберите элемент!"
    player_score = 0
    ai_score = 0
    target_score = 3
    
    # Создание кнопок с увеличенными размерами
    buttons = []
    button_width = 150  # Увеличенная ширина кнопки
    button_height = 120  # Увеличенная высота кнопки
    start_x = 50  # Начальная позиция по X
    spacing = 30  # Увеличенный промежуток между кнопками
    
    # Тексты для кнопок (сокращенные варианты)
    button_texts = {
        "Камень": "Камень",
        "Ножницы": "Ножницы",
        "Бумага": "Бумага",
        "Огонь": "Огонь",
        "Вода": "Вода",
        "Воздух": "Воздух",
        "Губка": "Губка"
    }
    
    for i, element in enumerate(ELEMENTS):
        btn_text = button_texts.get(element, element[:5])
        buttons.append(Button(start_x, 400, button_width, button_height, btn_text))
        start_x += button_width + spacing
    
    # Увеличенная кнопка сброса
    reset_button = Button(WIDTH // 2 - 150, 550, 300, 70, "Новая игра")
    
    # Главный игровой цикл
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game_state == "menu":
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "game"
            
            elif game_state == "game":
                for i, button in enumerate(buttons):
                    if button.is_clicked(mouse_pos, event):
                        player_choice = list(ELEMENTS.keys())[i]
                        ai_choice = random.choice(list(ELEMENTS.keys()))
                        result = get_winner(player_choice, ai_choice)
                        
                        if "Игрок" in result:
                            player_score += 1
                        elif "AI" in result:
                            ai_score += 1
                            
                        if player_score >= target_score or ai_score >= target_score:
                            game_state = "result"
            
            if reset_button.is_clicked(mouse_pos, event):
                # Сброс игры
                player_choice = None
                ai_choice = None
                result = "Выберите элемент!"
                player_score = 0
                ai_score = 0
                game_state = "game"
        
        # Отрисовка
        screen.fill(BG_COLOR)
        
        if game_state == "menu":
            # Экран приветствия
            title = title_font.render("Расширенная Камень-Ножницы-Бумага", True, BLACK)
            subtitle = main_font.render("Нажмите любую клавишу для начала", True, BLACK)
            rules = small_font.render("Играйте до 3 побед. Выберите элемент, который победит AI.", True, BLACK)
            
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
            screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 200))
            screen.blit(rules, (WIDTH // 2 - rules.get_width() // 2, 300))
            
            # Показываем все элементы с увеличенными промежутками
            y_pos = 350
            elements_per_row = 4
            x_spacing = (WIDTH - elements_per_row * 150) // (elements_per_row + 1)
            
            for i, (element, data) in enumerate(ELEMENTS.items()):
                row = i // elements_per_row
                col = i % elements_per_row
                x_pos = x_spacing + col * (150 + x_spacing)
                y_pos = 350 + row * 180
                
                screen.blit(images[element], (x_pos, y_pos))
                text = small_font.render(element, True, data["color"])
                screen.blit(text, (x_pos, y_pos + 130))
        
        elif game_state in ["game", "result"]:
            # Отображение счета
            score_text = main_font.render(f"{player_score} : {ai_score}", True, BLACK)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 30))
            
            # Отображение выбора игрока и AI (с увеличенными изображениями)
            if player_choice:
                player_text = main_font.render("Игрок:", True, BLACK)
                screen.blit(player_text, (200, 100))
                screen.blit(pygame.transform.scale(images[player_choice], (150, 150)), (200, 150))
                
                ai_text = main_font.render("AI:", True, BLACK)
                screen.blit(ai_text, (WIDTH - 350, 100))
                screen.blit(pygame.transform.scale(images[ai_choice], (150, 150)), (WIDTH - 350, 150))
            
            # Отображение результата
            result_text = main_font.render(result, True, BLACK)
            screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 300))
            
            # Кнопки выбора элементов
            for button in buttons:
                button.check_hover(mouse_pos)
                button.draw(screen)
            
            # Если игра завершена
            if game_state == "result":
                if player_score >= target_score:
                    final_text = title_font.render("Вы выиграли матч!", True, (0, 150, 0))
                else:
                    final_text = title_font.render("AI выиграл матч!", True, (150, 0, 0))
                
                screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, 350))
                reset_button.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()    

if __name__ == "__main__":
    main()