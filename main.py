import pygame
import math
from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        BLACK
        # Música
        pygame.mixer.music.load("assent/MusicaFondo.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)


        self.sound_shoot = pygame.mixer.Sound("assent/disparo.mp3")
        self.sound_explosion = pygame.mixer.Sound("assent/golpe.mp3")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Invasion Espacial")
        self.clock = pygame.time.Clock()
        self.running = True

        # Fondo
        self.background = pygame.image.load("assent/Fondo.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.font = pygame.font.Font(None, 32)

        self.reset_game()

    # Reiniciar juego completo
    def reset_game(self):
        self.player = Player()
        self.bullet = Bullet()
        self.enemies = [Enemy() for _ in range(8)]
        self.score = 0
        self.game_over = False

        pygame.mixer.music.play(-1)

    # Colisión bala-enemigo
    def check_bullet_collision(self, enemy):
        distance = math.hypot(
            enemy.x - self.bullet.x,
            enemy.y - self.bullet.y
        )
        return distance < 27

    # Colisión enemigo-jugador
    def check_player_collision(self, enemy):
        distance = math.hypot(
            enemy.x - self.player.x,
            enemy.y - self.player.y
        )
        return distance < 40

    def show_game_over(self):
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart = self.font.render("Presiona R para reiniciar", True, WHITE)

        self.screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        self.screen.blit(restart, (WIDTH // 2 - 130, HEIGHT // 2))

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            # =========================
            # JUEGO NORMAL
            # =========================
            if not self.game_over:

                if keys[pygame.K_LEFT]:
                    self.player.move(-1)

                if keys[pygame.K_RIGHT]:
                    self.player.move(1)

                if keys[pygame.K_SPACE]:
                    if not self.bullet.active:
                        self.bullet.shoot(self.player.x)
                        self.sound_shoot.play()

                self.screen.blit(self.background, (0, 0))

                self.player.draw(self.screen)

                # Bala
                self.bullet.move()
                self.bullet.draw(self.screen)

                # Enemigos
                for enemy in self.enemies:
                    enemy.move()
                    enemy.draw(self.screen)

                    # Bala golpea enemigo (modo láser)
                    if self.bullet.active and self.check_bullet_collision(enemy):
                        self.score += 100
                        self.sound_explosion.play()
                        enemy.reset_position()

                    # Enemigo toca jugador
                    if self.check_player_collision(enemy):
                        self.game_over = True
                        pygame.mixer.music.stop()

                # Puntaje
                score_text = self.font.render(
                    f"Puntaje: {self.score}",
                    True,
                    WHITE
                )
                self.screen.blit(score_text, (10, 10))

            # =========================
            # GAME OVER
            # =========================
            else:
                self.screen.blit(self.background, (0, 0))
                self.show_game_over()

                if keys[pygame.K_r]:
                    self.reset_game()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()