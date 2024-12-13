import sys
import pygame


def main():
    pygame.init()

    screen_widght = 688
    screen_height = 462
    screen = pygame.display.set_mode((screen_widght, screen_height))

    clock = pygame.time.Clock()

    image = pygame.image.load("elka_fon.png")
    image_mask = pygame.image.load("elka_maska.png")
    screen.blit(image, (0, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                color = image_mask.get_at(pos)[:3]
                if color == (255, 0, 0):
                    print("True")
                    #функция

            

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
