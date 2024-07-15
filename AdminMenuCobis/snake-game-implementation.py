from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Configuración del juego
GRID_SIZE = 20
INITIAL_SNAKE_LENGTH = 3
INITIAL_SPEED = 200  # milisegundos

# Estado del juego
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = 'right'
food = None
score = 0
game_over = False

def generate_food():
    global food
    while True:
        new_food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if new_food not in snake:
            food = new_food
            break

@app.route('/')
def index():
    return render_template('index.html', grid_size=GRID_SIZE)

@app.route('/start', methods=['POST'])
def start_game():
    global snake, direction, food, score, game_over
    snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
    direction = 'right'
    generate_food()
    score = 0
    game_over = False
    return jsonify(success=True)

@app.route('/move', methods=['POST'])
def move():
    global snake, direction, food, score, game_over

    if game_over:
        return jsonify(game_over=True, score=score)

    new_direction = request.json['direction']
    if new_direction in ['up', 'down', 'left', 'right']:
        if (new_direction == 'up' and direction != 'down') or \
           (new_direction == 'down' and direction != 'up') or \
           (new_direction == 'left' and direction != 'right') or \
           (new_direction == 'right' and direction != 'left'):
            direction = new_direction

    head = snake[0]
    if direction == 'up':
        new_head = (head[0], (head[1] - 1) % GRID_SIZE)
    elif direction == 'down':
        new_head = (head[0], (head[1] + 1) % GRID_SIZE)
    elif direction == 'left':
        new_head = ((head[0] - 1) % GRID_SIZE, head[1])
    else:  # right
        new_head = ((head[0] + 1) % GRID_SIZE, head[1])

    if new_head in snake:
        game_over = True
        return jsonify(game_over=True, score=score)

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        generate_food()
    else:
        snake.pop()

    return jsonify(
        snake=snake,
        food=food,
        score=score,
        game_over=game_over
    )

if __name__ == '__main__':
    generate_food()
    app.run(debug=True)