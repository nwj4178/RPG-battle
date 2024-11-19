import pygame
from character import Hero, Monster
from battle import Battle

# Initialize pygame
pygame.init()

# 화면 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 폰트 설정
font = pygame.font.Font(None, 32)

# 상태 변수
input_active = True
name = ""
role = ""
selected_role = None
hero = None
monster = None
battle = Battle()

# 직업 선택 버튼
roles = ["Warrior", "Mage", "Archer"]
role_buttons = [(150 + i * 100, 150, 80, 40) for i in range(len(roles))]


def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    global name, role, selected_role, hero, monster, input_active
    clock = pygame.time.Clock()

    # 게임 루프
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 이름 입력 처리
            if input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False  # 이름 입력 완료
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            # 직업 선택 처리
            if not input_active and not role:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for i, (x, y, w, h) in enumerate(role_buttons):
                        if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                            role = roles[i]
                            selected_role = i

            # 전투 시작 처리
            if hero and monster and event.type == pygame.MOUSEBUTTONDOWN:
                if attack_button.collidepoint(event.pos):
                    battle.fight(hero, monster)  # 전투 진행

        # 이름 입력 화면
        if input_active:
            display_text("Enter Hero's Name:", 50, 50)
            pygame.draw.rect(screen, BLACK, pygame.Rect(50, 100, 200, 32), 2)
            display_text(name, 60, 105)

        # 직업 선택 화면
        elif not role:
            display_text("Choose Hero's Class:", 50, 50)
            for i, (x, y, w, h) in enumerate(role_buttons):
                pygame.draw.rect(screen, BLUE if i == selected_role else BLACK, (x, y, w, h))
                display_text(roles[i], x + 10, y + 10, WHITE)

        # 전투 화면
        else:
            if not hero:
                hero = Hero(name=name, hp=100, attack=20, defense=5, role=role)
                monster = Monster(name="Goblin", hp=50, attack=10, defense=2)
                print(f"Hero {hero.name} ({hero.role}) vs Monster {monster.name} initialized.")

            # 영웅과 몬스터 정보 출력
            display_text(f"Hero: {hero}", 50, 50)
            display_text(f"Monster: {monster}", 50, 100)

            # 공격 버튼
            attack_button = pygame.draw.rect(screen, RED, pygame.Rect(250, 300, 100, 50))
            display_text("Attack", 270, 315, WHITE)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
