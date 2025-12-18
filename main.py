import pygame
import sys
from settings import WIDTH, HEIGHT, GRID_SIZE
from snake import Snake
from food import Food

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

# Шрифт для отображения очков
font = pygame.font.SysFont(None, 36)

# Кадровый таймер
clock = pygame.time.Clock()

# Создаем объекты
snake = Snake()
food = Food()

score = 0  # переменная для подсчета очков

def main():
    global score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))

        # Передвижение змейки
        snake.move()

        # Проверка столкновения с едой
        if snake.positions[0] == (food.x, food.y):
            score += 1  # увеличиваем счет
            snake.positions.append(snake.positions[-1])  # растим змейку
            food.spawn()

        # Рендеринг
        screen.fill((0, 0, 0))
        snake.draw(screen)
        food.draw(screen)

        # Отображение счета
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        # Ограничение кадров
        clock.tick(10)

if __name__ == '__main__':
    main()