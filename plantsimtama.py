# PyGame Plant Tamagotchi
# Created by Wren Hayes
import pygame

# create initial attributes for game window
window_title = 'P L A N T A M A - Wren Hayes'
window_width = 600
window_height = 600
clock = pygame.time.Clock()

# other game assets for global use
background_color = (52, 116, 116)
plant_window_color = (117, 183, 158)
dark_plant_window_color = (35, 56, 48)
text_unpress_color = (255, 255, 255)
text_press_color = (78, 78, 78)
button_unpress_color = (178, 178, 178)
button_press_color = (142, 142, 142)
pygame.font.init()
font = pygame.font.SysFont(None, 24)


# create the plant stats printout function
def plant_stats(my_plant):
    print(f"Height: {my_plant.height}")
    print(f"Hunger: {my_plant.hunger}")
    print(f"Thirst: {my_plant.thirst}")
    if plant_sim.light_on is False:
        print(f"The light is currently off.")
    elif plant_sim.light_on is True:
        print(f"The light is currently on.")


# create and initialize the Sim class that runs the game
class Sim:
    # tick rate is how many times per second the screen refreshes
    tick_rate = 2

    def __init__(self, title, width, height, light_on):
        self.title = title
        self.width = width
        self.height = height
        self.light_on = light_on

        # set up game window
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(background_color)
        pygame.display.set_caption(title)

    def run_sim(self):
        # set simulation base attributes
        is_harvest_time = False

        # set plant base attributes
        # (width, height, hunger, light, thirst, image_path, x, y):
        my_plant = Plant(50, 50, 8, 8, 'sprite1.png', 275, 300)

        # start the main gameplay loop
        while not is_harvest_time:

            # create events for main gameplay loop and quits if win condition is met
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_harvest_time = True

                # checks if key is pressed for food/water
                elif event.type == pygame.KEYDOWN:

                    # if key is w, run water
                    if event.key == pygame.K_w and plant_sim.light_on is True:
                        text = font.render('You give your plant some water.', True, text_unpress_color)
                        self.game_screen.blit(text, (180, 200))

                        # push water button on screen
                        pygame.draw.ellipse(self.game_screen, button_press_color, [150, 475, 50, 50])
                        water_button_label = font.render('W', True, text_press_color)
                        self.game_screen.blit(water_button_label, (168, 492))

                        # change plant stats, display change in terminal, tick clock
                        my_plant.grow(1)
                        my_plant.water(-5)
                        plant_stats(my_plant)
                        pygame.display.update()
                        clock.tick(1)

                    # if key is f, add food
                    elif event.key == pygame.K_f and plant_sim.light_on is True:
                        text = font.render('You give your plant some food.', True, text_unpress_color)
                        self.game_screen.blit(text, (180, 200))

                        # push food button on screen
                        pygame.draw.ellipse(self.game_screen, button_press_color, [275, 500, 50, 50])
                        food_button_label = font.render('F', True, text_press_color)
                        self.game_screen.blit(food_button_label, (295, 520))

                        # change plant stats...
                        my_plant.grow(2)
                        my_plant.feed(-5)
                        plant_stats(my_plant)
                        pygame.display.update()
                        clock.tick(1)

                # check for keyup (release) and change button colors back to unpressed
                elif event.type == pygame.KEYUP:
                    pygame.draw.ellipse(self.game_screen, button_unpress_color, [150, 475, 50, 50])
                    pygame.draw.ellipse(self.game_screen, button_unpress_color, [275, 500, 50, 50])

                    # stop plant growing/adding food/water if key is released
                    if event.key == pygame.K_w or event.key == pygame.K_f:
                        my_plant.grow(0)
                        my_plant.feed(0)
                        my_plant.water(0)

                    # turn light on or off
                    elif event.key == pygame.K_s and plant_sim.light_on is False:
                        plant_sim.light_on = True
                    elif event.key == pygame.K_s and plant_sim.light_on is True:
                        plant_sim.light_on = False

                # prints events to terminal
                print(event)

            # gameplay loop conditions that are not reliant on keypresses
            if self.light_on is True:

                # creates conditions to fight against by increasing hunger and thirst every tick while light is on
                my_plant.hunger += 1
                my_plant.thirst += 1

                # draw main game area and plant based on whether light is on
                pygame.draw.ellipse(self.game_screen, plant_window_color, [100, 75, 400, 400])
                pygame.draw.ellipse(self.game_screen, button_press_color, [400, 475, 50, 50])
                my_plant.idle(self.game_screen)
                my_plant.draw(self.game_screen)

                # display thirst and hunger if light is on
                thirst_display = font.render('Thirst: ' + str(my_plant.thirst), True, text_press_color)
                self.game_screen.blit(thirst_display, (265, 375))
                hunger_display = font.render('Hunger: ' + str(my_plant.hunger), True, text_press_color)
                self.game_screen.blit(hunger_display, (258, 400))

                lamp_button_label = font.render('S', True, text_press_color)
                self.game_screen.blit(lamp_button_label, (420, 495))

            elif self.light_on is False:
                pygame.draw.ellipse(self.game_screen, dark_plant_window_color, [100, 75, 400, 400])
                pygame.draw.ellipse(self.game_screen, button_unpress_color, [400, 475, 50, 50])
                text = font.render('The light is off.', True, text_unpress_color)
                lamp_button_label = font.render('S', True, text_unpress_color)
                self.game_screen.blit(text, (240, 280))
                self.game_screen.blit(lamp_button_label, (420, 495))

            # draw basic main menu area that is returned to on tick
            # water button
            pygame.draw.ellipse(self.game_screen, button_unpress_color, [150, 475, 50, 50])
            water_button_label = font.render('W', True, text_unpress_color)
            self.game_screen.blit(water_button_label, (168, 492))
            # food button
            pygame.draw.ellipse(self.game_screen, button_unpress_color, [275, 500, 50, 50])
            food_button_label = font.render('F', True, text_unpress_color)
            self.game_screen.blit(food_button_label, (295, 520))

            # update game display at rate of tick_rate
            pygame.display.update()
            clock.tick(self.tick_rate)

        # create win condition
            if my_plant.height >= 65 and my_plant.hunger <= 0 and my_plant.thirst <= 0 and plant_sim.light_on is True:
                text = font.render('It\'s harvest time! Congratulations!', True, text_unpress_color)
                self.game_screen.blit(text, (175, 250))
                pygame.display.update()

                # delay for 7 seconds, then quit
                pygame.time.delay(7000)
                is_harvest_time = True

        # create lose condition
            elif my_plant.hunger >= 25 and my_plant.thirst >= 25:
                text = font.render('Oh no! Your plant died. :(', True, text_unpress_color)
                self.game_screen.blit(text, (200, 200))
                text = font.render('Start over.', True, text_unpress_color)
                self.game_screen.blit(text, (260, 225))
                pygame.display.update()

                # delay for 3 seconds, then start over
                pygame.time.delay(3000)
                is_harvest_time = True


# create and initialize the Plant class
class Plant:
    def __init__(self, width, height, hunger, thirst, image_path, x_pos, y_pos):

        plant_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(plant_image, (width, height))

        self.width = width
        self.height = height
        self.hunger = hunger
        self.thirst = thirst
        self.image_path = image_path
        self.x_pos = x_pos
        self.y_pos = y_pos

    def grow(self, grow_amount):
        max_height = 74
        if self.height < max_height:
            self.height += grow_amount
        elif self.height >= max_height:
            return self.height

    def feed(self, feed_amount):
        min_hunger = 0
        if self.hunger > min_hunger:
            self.hunger += feed_amount
        elif self.hunger <= min_hunger:
            return self.hunger

    def water(self, water_amount):
        min_thirst = 0
        if self.thirst > min_thirst:
            self.thirst += water_amount
        elif self.thirst <= min_thirst:
            return self.thirst

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

    def idle(self, background):
        if self.y_pos == 300:
            self.y_pos += 5
            background.blit(self.image, (self.x_pos, self.y_pos))
        elif self.y_pos == 305:
            self.y_pos -= 5
            background.blit(self.image, (self.x_pos, self.y_pos))


# start pygame
pygame.init()


# begin new game
plant_sim = Sim(window_title, window_width, window_height, False)
plant_sim.run_sim()


# quit out when win has been reached
pygame.quit()
quit()