#include "raylib.h"

const int screenWidth = 1280;
const int screenHeight = 720;

const int paddleWidth = 20;
const int paddleHeight = 100;
const int ballSize = 20;

int main() {
    InitWindow(screenWidth, screenHeight, "Pong Game");

    int playerScore = 0;
    int computerScore = 0;

    Rectangle player = { 50, screenHeight / 2 - paddleHeight / 2, paddleWidth, paddleHeight };
    Rectangle computer = { screenWidth - 50 - paddleWidth, screenHeight / 2 - paddleHeight / 2, paddleWidth, paddleHeight };
    Vector2 ball = { screenWidth / 2, screenHeight / 2 };
    Vector2 ballSpeed = { 300.0f, 300.0f };

    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        // Player movement
        if (IsKeyDown(KEY_UP) && player.y > 0) player.y -= 500 * GetFrameTime();
        if (IsKeyDown(KEY_DOWN) && player.y < screenHeight - paddleHeight) player.y += 500 * GetFrameTime();

        // Computer AI movement
        if (computer.y + paddleHeight / 2 < ball.y) computer.y += 300 * GetFrameTime();
        if (computer.y + paddleHeight / 2 > ball.y) computer.y -= 300 * GetFrameTime();

        // Ball movement
        ball.x += ballSpeed.x * GetFrameTime();
        ball.y += ballSpeed.y * GetFrameTime();

        // Ball collision with top and bottom
        if (ball.y <= 0 || ball.y >= screenHeight - ballSize) ballSpeed.y *= -1;

        // Ball collision with paddles
        if (CheckCollisionCircleRec(ball, ballSize / 2, player) || CheckCollisionCircleRec(ball, ballSize / 2, computer)) {
            ballSpeed.x *= -1.1f; // Increase speed slightly
        }

        // Scoring
        if (ball.x <= 0) {
            computerScore++;
            ball = { screenWidth / 2, screenHeight / 2 };
            ballSpeed = { 300.0f, 300.0f };
        }
        if (ball.x >= screenWidth) {
            playerScore++;
            ball = { screenWidth / 2, screenHeight / 2 };
            ballSpeed = { -300.0f, 300.0f };
        }

        // Draw everything
        BeginDrawing();
        ClearBackground(GREEN);

        DrawRectangleRec(player, WHITE);
        DrawRectangleRec(computer, WHITE);
        DrawCircleV(ball, ballSize / 2, YELLOW);

        DrawText(TextFormat("Player: %i", playerScore), 10, 10, 20, WHITE);
        DrawText(TextFormat("Computer: %i", computerScore), screenWidth - 150, 10, 20, WHITE);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}