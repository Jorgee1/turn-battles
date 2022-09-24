import pyray as ray

screen_width = 800
screen_height = 600

menu = ray.Rectangle(0,0,screen_width,200)
menu.y = screen_height - menu.height

enemy = ray.Rectangle(0,0,100,100)
enemy.x = screen_width/2 - enemy.width/2
enemy.y = 20

player = ray.Rectangle(0,0,100,100)
player.x = screen_width/2 - player.width/2
player.y = screen_height - 20 - player.height - menu.height

character_index = 0
menu_index = 0
main_options = ['Attack', 'Items', 'Exit']
attack_options = ['Heavy', 'Light']

menu_stack = []
menu_stack.append(main_options)

ray.init_window(screen_width, screen_height, "Hello")
while not ray.window_should_close():

    if ray.is_key_pressed(ray.KEY_DOWN):
        menu_index += 1
    elif ray.is_key_pressed(ray.KEY_UP):
        menu_index -= 1
    
    if ray.is_key_pressed(ray.KEY_Z):
        menu_index = 0
        menu_stack.append(attack_options)

    if ray.is_key_pressed(ray.KEY_X):

        if len(menu_stack) > 1:
            menu_index = 0
            menu_stack.pop()


    if menu_index < 0: menu_index = len(menu_stack[-1]) - 1
    if menu_index >= len(menu_stack[-1]): menu_index = 0


    if ray.is_key_pressed(ray.KEY_LEFT):
        character_index += 1
    elif ray.is_key_pressed(ray.KEY_RIGHT):
        character_index -= 1

    if character_index < 0: character_index = 2 - 1
    if character_index >= 2: character_index = 0


    ray.clear_background(ray.BLACK)

    ray.draw_rectangle_rec(enemy, ray.WHITE)
    ray.draw_rectangle_rec(player, ray.WHITE)
    
    if character_index == 0:
        ray.draw_rectangle_lines_ex(enemy, 5, ray.RED)
    else:
        ray.draw_rectangle_lines_ex(player, 5, ray.RED)

    # Menu
    ray.draw_rectangle_rec(menu, ray.WHITE)

    for index, option in enumerate(menu_stack[-1]):
        text_size = ray.measure_text(option, 20)
        ray.draw_text(option, int(menu.x) + 20, int(menu.y) + index * 20, 20, ray.BLACK )
        if index == menu_index:
            ray.draw_text('*', 5, int(menu.y) + index * 20, 20, ray.BLACK)

    ray.end_drawing()

ray.close_window()


