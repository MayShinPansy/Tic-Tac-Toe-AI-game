#MAY_SHIN_THANT
#4488OLRZ(23029352)
#TIC_TAC_TOE(MINI-PROJECT)
import pygame
import sys
import random

# Initialize Pygame and set up the game window
pygame.init()
background_image = pygame.image.load("background.jpg") # Load background image
background_image = pygame.transform.scale(background_image, (600, 600)) # Scale background to fit window

# Constants for the game
WIDTH, HEIGHT = 600, 600 # Dimensions of the game window
LINE_WIDTH = 15  # Thickness of grid lines
BOARD_SIZE = 3   # Tic-tac-toe grid size (3x3)
CELL_SIZE = WIDTH // BOARD_SIZE   # Size of each cell in the grid
CIRCLE_RADIUS = CELL_SIZE // 3  # Radius for O's if drawn as a circle
CIRCLE_WIDTH = 15  # Thickness of circle
CROSS_WIDTH = 25  # Thickness of cross lines
SPACE = 55  # Padding for drawing X and O

# Colors
PINK = (255, 182, 193)  # Light pink color
BLACK = (0, 0, 0)  # Black
RED = (204, 0, 0)  # Dark red
BLUE = (0, 0, 255)  # Blue
WHITE = (255, 255, 255)  # White
GRAY = (128, 128, 128)  # Gray for menus and text boxes
MINECRAFT_GREEN = (67, 166, 42)  # Theme color for Minecraft-style green
DARK_GREEN = (36, 78, 36)  # Darker green for the background
DARK_GREY = (105, 105, 105)  # For grid lines
LIGHT_GREY = (211, 211, 211)  
CACTUS_GREEN = (77, 152, 56)
LIGHT_RED = (255, 99, 71)  

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up screen dimensions
pygame.display.set_caption('Tic-Tac-Toe')    # Set the title of the game window

# Set up fonts
font = pygame.font.Font("Minecraft.ttf", 30)  # Main font for buttons
large_font = pygame.font.Font("Minecraft.ttf", 40)   # Larger font for titles
input_font = pygame.font.Font("Minecraft.ttf", 35)   # Font for text input

# Get username
def get_username():
    global username
    input_active = True  # State for username input
    username = ""  # Initialize username
    while input_active:
        screen.blit(background_image, (0, 0))  # Display background
        input_box_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 10, 300, 50)  # Rectangle size and position
        pygame.draw.rect(screen, GRAY, input_box_rect) # Draw input box
        prompt_text = large_font.render("Enter Your Name:", True, BLACK) # Prompt for username
        name_display = input_font.render(username, True, BLACK) # Display entered text
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 3)) # Center prompt
        screen.blit(name_display, (WIDTH // 2 - name_display.get_width() // 2, HEIGHT // 2)) # Center text input
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit game on quit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Handle keyboard input
                if event.key == pygame.K_RETURN and username: # Confirm input on Enter key
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Remove character on Backspace
                    username = username[:-1]
                else:
                    username += event.unicode # Add typed character
                    
# Update the game window title with username and difficulty
def update_title():
    pygame.display.set_caption(f"{username} vs AI - Difficulty: {difficulty}")

# Initialize the game board and set default difficulty
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Empty 3x3 board
difficulty = 'Easy'  # Default AI difficulty

# Draw difficulty menu
def draw_menu():
    screen.blit(background_image, (0, 0)) # Display background
    menu_title = large_font.render("Choose Difficulty", True, BLACK) # Menu title
    easy_button = font.render("Easy", True, BLACK) # Easy button text
    medium_button = font.render("Medium", True, BLACK) # Medium button text
    hard_button = font.render("Hard", True, BLACK) # Hard button text
    
    # Draw buttons with grey backgrounds
    pygame.draw.rect(screen, GRAY, (200, 150, 200, 50)) # Easy Button
    pygame.draw.rect(screen, GRAY, (200, 250, 200, 50)) # mEDIUM Button
    pygame.draw.rect(screen, GRAY, (200, 350, 200, 50)) # hard Button
    
    # Display text for buttons and menu title
    screen.blit(menu_title, (WIDTH // 2 - menu_title.get_width() // 2, 30)) # Center title
    screen.blit(easy_button, (200 + 50, 150 + 10)) # Easy button label
    screen.blit(medium_button, (210 + 30, 250 + 10)) # Medium button label
    screen.blit(hard_button, (200 + 50, 350 + 10))  # Hard button label

    pygame.display.flip() # Refresh screen


# Draw the grid lines for the Tic-Tac-Toe board
def draw_lines():
    pygame.draw.line(screen, DARK_GREY, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH) # Horizontal line 1
    pygame.draw.line(screen, DARK_GREY, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH) # Horizontal line 2
    pygame.draw.line(screen, DARK_GREY, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH) # Vertical line 1
    pygame.draw.line(screen, DARK_GREY, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH) # Vertical line 2
    
# Load images for X and O
x_image = pygame.image.load("X.png") # Load image for X
o_image = pygame.image.load("O.png") # Load image for O

# Resize images to fit within the cells 
x_image = pygame.transform.scale(x_image, (CELL_SIZE - 30, CELL_SIZE - 30)) # Scale X image
o_image = pygame.transform.scale(o_image, (CELL_SIZE - 30, CELL_SIZE - 30)) # Scale O image

# Draw figures (X and O) on the board
def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X.png':  # Check if the cell contains an X
                screen.blit(x_image, (col * CELL_SIZE + 10, row * CELL_SIZE + 10))  # Draw X at correct position
            elif board[row][col] == 'O.png':  # Check if the spot is an 'O'
                screen.blit(o_image, (col * CELL_SIZE + 10, row * CELL_SIZE + 10))  # Draw O at correct position


# Display the winner or a draw
def show_winner(winner):
    screen.blit(background_image, (0, 0)) # Display background
    if winner == "Draw": # Check for a draw
        text = large_font.render("It's a Draw!", True, BLACK) # Display draw message
    else:
        text = large_font.render(f"{winner} Wins!", True, BLACK) # Display winner message
    return_button = font.render("Return to Menu", True, RED) # Text for return button
    pygame.draw.rect(screen, GRAY, (176, 400, 250, 50)) # Draw return button rectangle
    screen.blit(return_button, (175 + 20, 400 + 10)) # Place button text
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2)) # Center winner text
    pygame.display.flip() # Refresh screen
    return_button_rect = pygame.Rect(200, 400, 200, 50) # Define return button area

    while True: # Wait for user action
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit game on quit
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Check for mouse click
                if return_button_rect.collidepoint(event.pos):  # Check if return button clicked
                    return "menu" # Return to menu
        pygame.display.update() # Update display

# Reset the game board for a new game
def reset_game():
    global board
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Clear board

# AI move for "Easy" difficulty (random moves)
def ai_move_easy():
    available_squares = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if not board[row][col]]  # Get empty squares
    if available_squares:  # Check if there are available moves
        row, col = random.choice(available_squares) # Pick a random square
        board[row][col] = 'O.png' # AI places O
        
# AI move for "Medium" difficulty (block and win logic)
def ai_move_medium():
    available_squares = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if not board[row][col]] # Get empty squares
    for row, col in available_squares: # Check all possible moves
        board[row][col] = 'O.png'  # Simulate AI move
        if check_win('O.png'): # Check if AI wins with this move
            return # Execute winning move
        board[row][col] = None # Undo simulated move

    for row, col in available_squares: # Check if player can win
        board[row][col] = 'X.png' # Simulate player move
        if check_win('X.png'):  # If player would win
            board[row][col] = 'O.png'  # Block player's win
            return
        board[row][col] = None # Undo simulated move

    if available_squares: # Make a random move if no immediate win/block needed
        row, col = random.choice(available_squares)
        board[row][col] = 'O.png'
        
# AI move for "Hard" difficulty (minimax algorithm)
def ai_move_hard():
    def minimax(is_maximizing): # Recursive function to evaluate game state
        if check_win('O.png'): # AI win
            return 1
        if check_win('X.png'):  # Player win
            return -1
        if check_draw(): #DRAW
            return 0

        scores = []  # List to store scores for each move
        for row, col in [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if not board[r][c]]: # Loop through empty squares
            board[row][col] = 'O.png' if is_maximizing else 'X.png' # Simulate AI or player move
            scores.append(minimax(not is_maximizing))  # Recursive call
            board[row][col] = None # Undo simulated move
        return max(scores) if is_maximizing else min(scores) # Return best score

    best_score, best_move = -float('inf'), None  # Initialize best score and move
    for row, col in [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if not board[r][c]]:
        board[row][col] = 'O.png' # Simulate AI move
        score = minimax(False) # Evaluate move
        board[row][col] = None # Undo simulated move
        if score > best_score: # Update best move
            best_score, best_move = score, (row, col)

    if best_move: # If a move is found, execute it
        board[best_move[0]][best_move[1]] = 'O.png'

# Check if a player has won
def check_win(player):
     # Check rows, columns, and diagonals for a win
    return any(all(board[row][col] == player for col in range(BOARD_SIZE)) for row in range(BOARD_SIZE)) or \
           any(all(board[row][col] == player for row in range(BOARD_SIZE)) for col in range(BOARD_SIZE)) or \
           all(board[i][i] == player for i in range(BOARD_SIZE)) or \
           all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE))

# Check if the board is full (draw)
def check_draw():
    return all(board[row][col] is not None for row in range(BOARD_SIZE) for col in range(BOARD_SIZE))

# Main game loop
def main():
    global difficulty
    in_menu = True # Start in menu
    game_over = False # Game over state
    player = 'X.png' # Player's symbol

    while True:
        if in_menu: # If in the menu
            draw_menu() # Show menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Exit game
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # Handle menu button clicks
                    x, y = event.pos # Get mouse position
                    if 200 <= x <= 400 and 150 <= y <= 200: # Easy button
                        difficulty = "Easy"
                        update_title()  # Update title with chosen difficulty
                        in_menu = False
                    elif 200 <= x <= 400 and 250 <= y <= 300: # Medium button
                        difficulty = "Medium"
                        update_title()
                        in_menu = False
                    elif 200 <= x <= 400 and 350 <= y <= 400: # Hard button
                        difficulty = "Hard"
                        update_title()
                        in_menu = False
            continue
        # Draw game screen
        screen.fill(DARK_GREEN)  # Fill background
        draw_lines() # Draw grid lines
        draw_figures() # Draw X and O
        pygame.display.flip()  # Refresh screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over: # Handle clicks during gameplay
                mouse_x, mouse_y = event.pos # Get click position
                clicked_row = mouse_y // CELL_SIZE # Determine row
                clicked_col = mouse_x // CELL_SIZE # Determine column
                if not board[clicked_row][clicked_col]: # Check if cell is empty
                    board[clicked_row][clicked_col] = player # Player move
                    if check_win(player):  # Check for player win
                        if show_winner(username) == "menu": # Show winner and check for menu return
                            in_menu = True
                            in_menu = True
                            reset_game()
                            game_over = False
                            break
                        game_over = True
                    elif check_draw():  # Check for draw
                        if show_winner("Draw") == "menu":  # Show draw and check for menu return
                            in_menu = True
                            reset_game()
                            game_over = False
                            break
                        game_over = True
                    player = 'O.png'
                    if not game_over:
                        if difficulty == "Easy":
                            ai_move_easy() # Easy AI logic
                        elif difficulty == "Medium":
                            ai_move_medium() # Medium AI logic (some basic strategy)
                        elif difficulty == "Hard":
                            ai_move_hard() # Hard AI logic (advanced strategy)
                        if check_win('O.png'):  # Check for AI win
                            if show_winner("AI") == "menu":
                                in_menu = True
                                reset_game()
                                game_over = False
                                break
                            # End the game if the AI wins
                            game_over = True
                        # If no one wins, check for a draw
                        elif check_draw():
                         # Handle the draw scenario and possibly return to the menu
                            if show_winner("Draw") == "menu":
                                in_menu = True
                                reset_game()
                                game_over = False
                                break
                             # End the game if it’s a draw
                            game_over = True
                        player = 'X.png'
        # Small delay after the game ends to give players time to see the result
        if game_over:
            pygame.time.wait(2000)
# Entry point of the game
if __name__ == "__main__":
    get_username() # Get the player's username before starting
    main() # Run the main game loop
