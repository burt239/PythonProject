
    per = True
    while per:
        xp = 137
        yv = 125
        xl = 213
        yn = 176

        window.blit(bgchoose, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            xb, yb = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                xb, yb = event.pos
                window.blit(m, (xb, yb))

                if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(svinka),(xp - xb, yv - yb)):
                    pizza = svinka
                    per = False
                if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(svinka), (xl - xb, yv - yb)):
                    pizza = zayaz
                    per = False
                if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(svinka), (xp - xb, yn - yb)):
                    pizza = devochka
                    per = False
                if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(svinka), (xl - xb, yn - yb)):
                    pizza = malchik
                    per = False