import pygame
import pygame_gui
import warnings
import DoublePendulum


pygame.init()
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Double Pendulum')
clock = pygame.time.Clock()

pos = (width / 2, height/3)
dp = DoublePendulum.DoublePendulum(pos)
points = []


manager = pygame_gui.UIManager((width, height))
reset = pygame_gui.elements.UIButton(pygame.Rect((10, height - 40), (100, 30)), 'Reset', manager)
label_g = pygame_gui.elements.UILabel(pygame.Rect((width - 400, height - 40), (90, 30)), 'g: %.2f' % dp.g, manager)
slider_g = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((width - 310, height - 40), (300, 30)), dp.g, (0.1, 20), manager)
label_m2 = pygame_gui.elements.UILabel(pygame.Rect((width - 400, height - 70), (90, 30)), 'm2: %.2f' % dp.m2, manager)
slider_m2 = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((width - 310, height - 70), (300, 30)), dp.m2, (0.1, 40), manager)
label_m1 = pygame_gui.elements.UILabel(pygame.Rect((width - 400, height - 100), (90, 30)), 'm1: %.2f' % dp.m1, manager)
slider_m1 = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((width - 310, height - 100), (300, 30)), dp.m1, (0.1, 40), manager)
label_r2 = pygame_gui.elements.UILabel(pygame.Rect((width - 400, height - 130), (90, 30)), 'r2: %d' % dp.r2, manager)
slider_r2 = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((width - 310, height - 130), (300, 30)), dp.r2, (1, 250), manager)
label_r1 = pygame_gui.elements.UILabel(pygame.Rect((width - 400, height - 160), (90, 30)), 'r1: %d' % dp.r1, manager)
slider_r1 = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((width - 310, height - 160), (300, 30)), dp.r1, (1, 250), manager)

is_running = True

while is_running:
    dt = clock.tick(144) / 1000
    manager.update(dt)
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == reset:
                dp.reset()
                points = []
    
        
    dp.g = slider_g.get_current_value()
    label_g.set_text('g: %.2f' % dp.g)
    dp.m2 = slider_m2.get_current_value()
    label_m2.set_text('m2: %.2f' % dp.m2)
    dp.m1 = slider_m1.get_current_value()
    label_m1.set_text('m1: %.2f' % dp.m1)
    dp.r2 = slider_r2.get_current_value()
    label_r2.set_text('r2: %d' % dp.r2)
    dp.r1 = slider_r1.get_current_value()
    label_r1.set_text('r1: %d' % dp.r1)        

    window.fill((0, 0, 0))

    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            dp.update(dt)
        except Warning:
            dp.reset()
            points = []
    (x1, y1, x2, y2) = dp.get_pos()
    points.append((x2, y2))
    pygame.draw.aaline(window, (255, 255, 255), pos, (x1, y1))
    pygame.draw.circle(window, (255, 255, 255), (x1, y1), dp.m1)
    pygame.draw.aaline(window, (255, 255, 255), (x1, y1), (x2, y2))
    pygame.draw.circle(window, (255, 255, 255), (x2, y2), dp.m2)
    if len(points) > 1:
        pygame.draw.aalines(window, (255, 0, 0), False, points)
    
    manager.draw_ui(window)
    pygame.display.update()
    
    