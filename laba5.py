import pygame as pg


def main():
    pg.init()
    WIDTH, HEIGHT = 800, 800
    size = 80
    sizeX = WIDTH // size
    sizeY = HEIGHT // size
    arr = [[0 for _ in range(size)] for __ in range(size)]
    arrNext = [[0 for _ in range(size)] for __ in range(size)]
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    done = False
    running = True
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                arr[x//sizeX][y//sizeY] = 1 - arr[x//sizeX][y//sizeY]
            if event.type == pg.KEYDOWN:
                if event.unicode == ' ':
                    running = not running
        screen.fill((0, 0, 0))
        if running:
            for i in range(size):
                for j in range(size):
                    s = arr[(i - 1) % size][(j - 1) % size] + arr[i][(j - 1) % size] + arr[(i + 1) % size][(j - 1) % size] + arr[(i + 1) % size][j] + arr[(i + 1) % size][(j + 1) % size] + arr[i][(j + 1) % size] + arr[(i - 1) % size][(j + 1) % size] + arr[(i - 1) % size][j]
                    if ((s == 2) and (arr[i][j] == 1)) or (s == 3):
                        arrNext[i][j] = 1
                    else:
                        arrNext[i][j] = 0
            arr, arrNext = arrNext, arr
        for i in range(size):
            for j in range(size):
                if arr[i][j]:
                    if arrNext[i][j]:
                        pg.draw.rect(screen, (255, 255, 255), [i * sizeX, j * sizeY, sizeX - 1, sizeY - 1])
                    else:
                        pg.draw.rect(screen, (0, 255, 0), [i * sizeX, j * sizeY, sizeX - 1, sizeY - 1])
                else:
                    if arrNext[i][j]:
                        pg.draw.rect(screen, (0, 0, 255), [i * sizeX, j * sizeY, sizeX - 1, sizeY - 1])
        pg.display.flip()
        clock.tick(60)
    pg.quit()


if __name__ == '__main__':
    main()
# пробел - пауза\продолжить. клик - поменять цвет
