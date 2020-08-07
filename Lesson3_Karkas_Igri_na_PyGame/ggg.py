import pygame as pg

game_flag = True


def main():  # основной метод игры
    global game_flag

    def event_check(event):
        global game_flag
        if event.type == pg.QUIT:
            game_flag = False

    # здесь определяются константы, классы и функции
    FPS = 60  # частота обновлени окна
    gameover_f = False  # флаг конца игры
    name_win = 'название'  # название ока
    x, y = 600, 400  # размеры окна

    # здесь происходит инициация, создание объектов и др.
    pg.init()  # иницилизация библиотек
    pg.display.set_mode((x, y))  # создание окна
    pg.display.set_caption(name_win)
    clock = pg.time.Clock()

    # создание обектов
    #

    # отображает объекты на экран до цикла
    pg.display.update()

    # главный цикл
    while game_flag:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for i in pg.event.get():
            event_check(i)

        # --------
        # изменение объектов и многое др.
        # --------

        # обновление экрана
        pg.display.update()


if __name__ == '__main__':
    main()
