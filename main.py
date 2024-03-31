import pygame

# Initialize Pygame
pygame.init()

# Create the window and set its title
window = pygame.display.set_mode((1200, 399))
pygame.display.set_caption("Angry Nerds: AI-Driver")  # Set window title

# Load track and car images
track = pygame.image.load('track1.png')
car = pygame.image.load('tesla2.png')
car = pygame.transform.scale(car, (40, 70))

# Load Angry Birds icon
icon = pygame.image.load('angry_birds_icon_prev_ui.png')  # Assuming you have an icon named 'angry_birds_icon.png'

# Set window icon
pygame.display.set_icon(icon)

# Initialize car position and other variables
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()

# Main game loop
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    
    clock.tick(60)
    
    # Calculate camera position
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    
    # Get pixel colors around the camera
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    
    # Change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    
    # Drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    
    # Draw everything on the window
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (128, 128, 128, 128), (cam_x, cam_y), 0, 0)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
