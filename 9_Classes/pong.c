#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <SDL2/SDL.h>

// Constants
#define WIDTH 640
#define HEIGHT 480
#define PADDLE_WIDTH 10
#define PADDLE_HEIGHT 60
#define BALL_SIZE 10

// Function to handle collisions between ball and paddles
bool checkCollision(SDL_Rect ball, SDL_Rect paddle) {
    return (ball.x < paddle.x + PADDLE_WIDTH &&
            ball.x + BALL_SIZE > paddle.x &&
            ball.y < paddle.y + PADDLE_HEIGHT &&
            ball.y + BALL_SIZE > paddle.y);
}

int main() {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        fprintf(stderr, "SDL_Init Error: %s\n", SDL_GetError());
        return 1;
    }

    // Create a window and renderer
    SDL_Window* window = SDL_CreateWindow("Pong", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (window == NULL || renderer == NULL) {
        fprintf(stderr, "SDL_CreateWindow or SDL_CreateRenderer Error: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    // Create paddles and ball
    SDL_Rect paddle1 = {10, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT};
    SDL_Rect paddle2 = {WIDTH - 10 - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT};
    SDL_Rect ball = {WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE};

    // Set initial ball speed
    int ballSpeedX = 5;
    int ballSpeedY = 5;

    // Main game loop
    bool quit = false;
    SDL_Event e;

    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }
        }

        const Uint8 *state = SDL_GetKeyboardState(NULL);

        // Move paddles
        if (state[SDL_SCANCODE_W] && paddle1.y > 0) {
            paddle1.y -= 5;
        }
        if (state[SDL_SCANCODE_S] && paddle1.y < HEIGHT - PADDLE_HEIGHT) {
            paddle1.y += 5;
        }

        if (state[SDL_SCANCODE_UP] && paddle2.y > 0) {
            paddle2.y -= 5;
        }
        if (state[SDL_SCANCODE_DOWN] && paddle2.y < HEIGHT - PADDLE_HEIGHT) {
            paddle2.y += 5;
        }

        // Move ball
        ball.x += ballSpeedX;
        ball.y += ballSpeedY;

        // Ball collisions with walls
        if (ball.y <= 0 || ball.y + BALL_SIZE >= HEIGHT) {
            ballSpeedY = -ballSpeedY;
        }

        // Ball collisions with paddles
        if (checkCollision(ball, paddle1) || checkCollision(ball, paddle2)) {
            ballSpeedX = -ballSpeedX;
        }

        // Scoring
        if (ball.x <= 0 || ball.x + BALL_SIZE >= WIDTH) {
            ball.x = WIDTH / 2 - BALL_SIZE / 2;
            ball.y = HEIGHT / 2 - BALL_SIZE / 2;
            ballSpeedX = -ballSpeedX;
        }

        // Clear the screen
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        // Draw paddles and ball
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &paddle1);
        SDL_RenderFillRect(renderer, &paddle2);
        SDL_RenderFillRect(renderer, &ball);

        // Update the window
        SDL_RenderPresent(renderer);

        // Cap the frame rate
        SDL_Delay(16);
    }

    // Cleanup and exit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
