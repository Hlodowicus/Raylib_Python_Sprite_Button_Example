from pyray import *

NUM_FRAMES = 3

screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib example - sprite button")

init_audio_device()

fxButton = Sound = load_sound("button-3.wav")
button = Texture2D = load_texture("button.png")

frameHeight = button.height/NUM_FRAMES
sourceRect = Rectangle(0, 0, button.width, frameHeight)

btnBounds = Rectangle(screenWidth/2.0 - button.width/2.0, screenHeight/2.0 - button.height/NUM_FRAMES/2.0, button.width, frameHeight)

btnState = 0
btnAction = False

counter = 0

mousePoint = Vector2(0.0, 0.0)

set_target_fps(60)

while not window_should_close():
    mousePoint = get_mouse_position()
    btnAction = False

    if check_collision_point_rec(mousePoint, btnBounds):
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT): btnState = 2
        else: btnState = 1

        if is_mouse_button_released(MouseButton.MOUSE_BUTTON_LEFT): 
            btnAction = True
            counter += 1
    else: btnState = 0

    if btnAction == True:
        play_sound(fxButton)
    
    sourceRect.y = btnState * frameHeight

    begin_drawing()

    clear_background(RAYWHITE)

    draw_texture_rec(button, sourceRect, [btnBounds.x, btnBounds.y], WHITE)

    draw_text(str(counter), 50, 50, 100, BLUE)

    end_drawing()

    


unload_texture(button)
unload_sound(fxButton)
close_audio_device()
close_window()