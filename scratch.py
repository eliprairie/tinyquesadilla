# create and initialize plant class
class Plant:
    def __init__(self, name, height, hunger, light, thirst):
        self.name = name
        self.height = height
        self.hunger = hunger
        self.light = light
        self.thirst = thirst

    def grow(self, grow_amount):
        self.height += grow_amount

    def feed(self, feed_amount):
        self.hunger += feed_amount

    def shine(self, light_amount):
        self.light += light_amount

    def water(self, water_amount):
        self.thirst += water_amount


# set plant base attributes
myPlant = Plant('', 0, 10, 0, 10)

# set plant name
myPlant.name = input("What would you like to name your plant? ")
print(f"Your plant is now named {myPlant.name}. \n")

# create win condition
if myPlant.height >= 10 and myPlant.hunger == 0 and myPlant.light == 5 and myPlant.thirst == 0:
    print(f"It\'s harvest time! You have succeeded at raising {myPlant.name}! Congratulations!")
    is_harvest_time = True
else:
    is_harvest_time = False

# begin simulation
time.sleep(1)
print(f"{myPlant.name} has three stats:")
print(f"Height: {myPlant.height}")
print(f"Hunger: {myPlant.hunger}")
print(f"Thirst: {myPlant.thirst}")
print(f"There is a light on your desk over {myPlant.name} as well. It is currently off. \n")
time.sleep(1)
print(f"Your goal is to make {myPlant.name} happy and grow tall!")

# inform user of options
time.sleep(1)
print(
    "To do this, you can enter text options like 'f' for food, 's' to turn the lightswitch on and off, and 'w' to water. \n")


# create choose function to get input
def choose():
    choice = ""
    while choice != "f" and choice != "s" and choice != "w":
        choice = input("What would you like to do first? ").lower().strip()

    if choice == "f" and not is_harvest_time:
        print(f"You give {myPlant.name} some plant food. It seems happy!")
        myPlant.grow(1)
        myPlant.feed(-1)
    elif choice == "w" and not is_harvest_time:
        print(f"You give {myPlant.name} some water. It seems happy!")
        myPlant.grow(1)
        myPlant.water(-1)
    elif choice == "s" and light_on is False and not is_harvest_time:
        print("You turn the light on.")
        myPlant.shine(1)
    elif choice == "s" and light_on is True and not is_harvest_time:
        print("You turn the light off.")
        myPlant.shine(-1)
    else:
        return choice


time.sleep(1)
choose()


# create initial attributes for game window
window_title = 'PlantSim 3000inator'
window_width = 600
window_height = 600
clock = pygame.time.Clock()

# other game assets for global use
background_color = (52, 116, 116)
plant_window_color = (117, 183, 158)
text_color = (255, 255, 255)
main_menu_color = (142, 142, 142)


# create and initialize the Sim class
class Sim:
    tick_rate = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # set up game window
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(background_color)
        pygame.display.set_caption(title)

    def run_sim(self):
        # set simulation base attributes
        is_harvest_time = False
        light_on = False

        # set plant base attributes
        my_plant = Plant('', 50, 50, 10, 0, 10, 'sprite1.png', 275, 300)

        # start the main gameplay loop
        while not is_harvest_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_harvest_time = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        water_amount = 1
                    # elif event.key == pygame.K_f:
                    #     feed_amount = 1
                    # elif event.key == pygame.K_s and light_on is False:
                    #     light_on = True
                    # elif event.key == pygame.K_s and light_on is True:
                    #     light_on = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_f:
                        water_amount = 0
                        feed_amount = 0
                    # elif event.key == pygame.K_s and light_on is False:
                    #     return light_on
                    # elif event.key == pygame.K_s and light_on is True:
                    #     return light_on
                # show me events that are happening in the game window
                print(event)

            # draw main game area and plant
            pygame.draw.rect(self.game_screen, plant_window_color, [50, 50, 500, 500])
            my_plant.draw(self.game_screen)

            # draw main menu area
            pygame.draw.rect(self.game_screen, main_menu_color, [50, 500, 500, 50])

            # update game display at rate of tick_rate
            pygame.display.update()
            clock.tick(self.tick_rate)


# create and initialize the Plant class
class Plant:
    def __init__(self, name, width, height, hunger, light, thirst, image_path, x, y):
        plant_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(plant_image, (width, height))

        self.name = name
        self.width = width
        self.height = height
        self.hunger = hunger
        self.light = light
        self.thirst = thirst
        self.image_path = image_path
        self.x_pos = x
        self.y_pos = y

    def grow(self, height, grow_amount):
        if height >= 10:
            self.height += grow_amount
        elif height <10:
            return self.height

    def feed(self, name, hunger, feed_amount):
        if hunger >= 0:
            print(f"{name} seems a little hungry.")
            self.hunger -= feed_amount
        elif hunger <= 10:
            self.hunger += 0
            print(f"{name} is full!")

    # def shine(self, name, light, light_amount):
    #     if light >= 5:
    #         print(f"{name} seems happy with the amount of light.")
    #         self.light += 0
    #     elif light < 5:
    #         print(f"{name} seems to be a little droopy.")
    #         self.light += light_amount

    def water(self, name, thirst, water_amount):
        if thirst >= 0:
            print(f"{name} seems to be drying up at the tips of the leaves.")
            self.thirst -= water_amount
        elif thirst <= 10:
            print(f"{name} seems happy with the amount of water.")

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


# start pygame
pygame.init()

# begin new game
plant_sim = Sim(window_title, window_width, window_height)
plant_sim.run_sim()


# quit the simulation
pygame.quit()
quit()

