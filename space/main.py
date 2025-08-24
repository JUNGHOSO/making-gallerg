import pygame
from pygame.mixer_music import set_volume

from objects.alien import Alien
from objects.fighter import Fighter
from objects.beam import Beam
from objects.explosion import Explosion

from constants import *
from scene_manager import SceneManager
from scenes.game_over_scene import GameOverScene
from scenes.game_scene import GameScene
from scenes.home_scene import HomeScene

print("Start up")
pygame.init()
pygame.key.set_repeat(500,500)
surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock=pygame.time.Clock()

SceneManager.instance.add("home",HomeScene())
SceneManager.instance.add("game",GameScene())
SceneManager.instance.add("game_over",GameOverScene())



while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT or(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print("Shutdowm")
            pygame.quit()
            exit()
            break
        if event.type == pygame.KEYDOWN:
            SceneManager.instance.scene.on_key_down(event.key)

        if event.type == pygame.KEYUP:
           SceneManager.instance.scene.on_key_up(event.key)


    delta_seconds=clock.tick(FPS)/1000

    SceneManager.instance.scene.on_update(delta_seconds)


    #render
    surface.fill((0,0,0))
    SceneManager.instance.scene.on_render(surface)


    pygame.display.update()
    clock.tick(FPS)