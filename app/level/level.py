from typing import NoReturn, Callable
from typing import List, Tuple
from dataclasses import dataclass

import pygame

from app.base import BaseController, BaseTile
from app.settings import TILE_SIZE, screen
from app.supports import ImportSupport, texture_dir, sound_dir
from app.data import levels, BaseLevel
from app.assets.engine.particles import JumpParticle, LandParticle, ExplosionParticle
from app.assets.engine.characters import Enemy
from app.assets.world.animated import Coin, Palm, Water
from app.assets.world.static import Crate, Sky, Clouds
from app.assets.tiles import StaticTile
from app.assets.engine.characters.player import Player, PlayerParticleData


def _create_till_group(layout, _type: str) -> pygame.sprite.Group:
    sprite_group = pygame.sprite.Group()

    for row_index, row in enumerate(ImportSupport.import_csv_layout(layout)):
        for col_index, val in enumerate(row):
            if val != '-1':
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if _type == 'terrain':
                    terrain_tile_list = ImportSupport.import_cut_graphics(texture_dir("terrain/terrain_tiles.png"))
                    tile_surface = terrain_tile_list[int(val)]
                    sprite = StaticTile(TILE_SIZE, x, y, tile_surface)
                if _type == 'grass':
                    grass_tile_list = ImportSupport.import_cut_graphics(texture_dir("decoration/grass/grass.png"))
                    tile_surface = grass_tile_list[int(val)]
                    sprite = StaticTile(TILE_SIZE, x, y, tile_surface)
                if _type == 'crates':
                    sprite = Crate(TILE_SIZE, x, y)
                if _type == 'coins':
                    if val == '0':
                        sprite = Coin(TILE_SIZE, x, y, texture_dir("coins/gold"), 5)
                    if val == '1':
                        sprite = Coin(TILE_SIZE, x, y, texture_dir("coins/silver"), 1)
                if _type == 'fgPalms':
                    if val == '0':
                        sprite = Palm(TILE_SIZE, x, y, texture_dir("terrain/palm_small"), 38)
                    if val == '1':
                        sprite = Palm(TILE_SIZE, x, y, texture_dir("terrain/palm_large"), 64)
                if _type == 'bgPalms':
                    sprite = Palm(TILE_SIZE, x, y, texture_dir("terrain/palm_bg"), 64)
                if _type == 'enemies':
                    sprite = Enemy(TILE_SIZE, x, y)
                if _type == 'constrains':
                    sprite = BaseTile(TILE_SIZE, x, y)

                sprite_group.add(sprite)

    return sprite_group


@dataclass()
class LevelData:
    currentLevel: int
    surface: pygame.Surface
    createMenu: Callable
    changeCoins: Callable
    health: Callable


class _Player:
    PLAYER_ON_GROUND = False

    def __init__(self):
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()

        self.dust_sprite = pygame.sprite.GroupSingle()

    def jump_particle(self, position: Tuple[int, int]) -> NoReturn:
        if self.player.sprite.position.FACING_RIGHT:
            position -= pygame.math.Vector2(10, 5)
        else:
            position += pygame.math.Vector2(10, -5)
        jump_particle = JumpParticle(position)
        self.dust_sprite.add(jump_particle)

    def on_ground(self) -> NoReturn:
        if self.player.sprite.position.ON_GROUND:
            self.PLAYER_ON_GROUND = True
        else:
            self.PLAYER_ON_GROUND = False

    def create_landing(self):
        if not self.PLAYER_ON_GROUND and self.player.sprite.position.ON_GROUND and not self.dust_sprite.sprites():
            if self.player.sprite.position.FACING_RIGHT:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            self.dust_sprite.add(LandParticle(self.player.sprite.rect.midbottom - offset))

    def is_death(self) -> bool:
        if self.player.sprite.rect.top > screen.height:
            return True

    def is_win(self) -> bool:
        if pygame.sprite.spritecollide(self.player.sprite, self.goal, False):
            return True

    def setup(self, layout: List, health: Callable, surface: pygame.Surface) -> '_Player':
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if value == '0':
                    sprite = Player(
                        (x, y),
                        surface=surface,
                        health=health,
                        particles=PlayerParticleData(jump=self.jump_particle)
                    )
                    self.player.add(sprite)
                if value == '1':
                    hat_surface = pygame.image.load(texture_dir("character/hat.png")).convert_alpha()
                    sprite = StaticTile(TILE_SIZE, x, y, hat_surface)
                    self.goal.add(sprite)
        return self


class _Map:
    TILLS = [
        "terrain", "coins", "fgPalms", "bgPalms", "crates",
        "enemies", "constrains", "grass"
    ]

    def __init__(self, level_data: BaseLevel):
        self._create(level_data)

    def _create(self, level_data: BaseLevel) -> NoReturn:
        for name in self.TILLS:
            setattr(self, name, _create_till_group(getattr(level_data, name), name))

    def enemy_collision_reverse(self) -> NoReturn:
        for enemy in self.enemies.sprites():
            if pygame.sprite.spritecollide(enemy, self.constrains, False):
                enemy.reverse()


class Level:
    WORLD_SHIFT = 0
    CURRENT_X = None

    def __init__(self, level: LevelData):
        self.COIN = pygame.mixer.Sound(sound_dir("effects/coin.wav"))
        self.STOMP = pygame.mixer.Sound(sound_dir("effects/stomp.wav"))
        self.display_surface = level.surface
        self.current_level = level.currentLevel

        current_level = levels[self.current_level]
        self.new_level = current_level.unlock
        self.back_to_menu = level.createMenu
        self.change_coins = level.changeCoins

        self.player = _Player().setup(
            layout=ImportSupport.import_csv_layout(current_level.player),
            health=level.health,
            surface=self.display_surface
        )

        self.explosion_sprites = pygame.sprite.Group()
        self.map = _Map(current_level)

        self.sky = Sky(8)
        level_width = len(ImportSupport.import_csv_layout(current_level.terrain)[0]) * TILE_SIZE
        self.water = Water(screen.height - 20, level_width=level_width)
        self.clouds = Clouds(400, level_width=level_width, cloud_number=30)

    def horizontal_movement_collision(self) -> NoReturn:
        player = self.player.player.sprite
        player.position.collision_rect.x += player.position.direction.x * player.position.SPEED
        collidable_sprites = self.map.terrain.sprites() + self.map.crates.sprites() + self.map.fgPalms.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.position.collision_rect):
                if player.position.direction.x < 0:
                    player.position.collision_rect.left = sprite.rect.right
                    player.position.ON_LEFT = True
                    self.CURRENT_X = player.rect.left
                elif player.position.direction.x > 0:
                    player.position.collision_rect.right = sprite.rect.left
                    player.position.ON_RIGHT = True
                    self.CURRENT_X = player.rect.right

    def vertical_movement_collision(self) -> NoReturn:
        player = self.player.player.sprite
        player.position.apply_gravity()
        collidable_sprites = self.map.terrain.sprites() + self.map.crates.sprites() + self.map.fgPalms.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.position.collision_rect):
                if player.position.direction.y > 0:
                    player.position.collision_rect.bottom = sprite.rect.top
                    player.position.direction.y = 0
                    player.position.ON_GROUND = True
                elif player.position.direction.y < 0:
                    player.position.collision_rect.top = sprite.rect.bottom
                    player.position.direction.y = 0
                    player.position.ON_CEILING = True

        if player.position.ON_GROUND and player.position.direction.y < 0 or player.position.direction.y > 1:
            player.position.ON_GROUND = False

    def scroll_x(self) -> NoReturn:
        player = self.player.player.sprite
        player_x = player.rect.centerx
        direction_x = player.position.direction.x

        if player_x < screen.width / 4 and direction_x < 0:
            self.WORLD_SHIFT = 8
            player.position.SPEED = 0
        elif player_x > screen.width - (screen.width / 4) and direction_x > 0:
            self.WORLD_SHIFT = -8
            player.position.SPEED = 0
        else:
            self.WORLD_SHIFT = 0
            player.position.SPEED = 8

    def check_coin_collisions(self) -> NoReturn:
        collided_coins = pygame.sprite.spritecollide(self.player.player.sprite, self.map.coins, True)
        if collided_coins:
            self.COIN.play()
            for coin in collided_coins:
                self.change_coins(coin.value)

    def check_enemy_collisions(self) -> NoReturn:
        enemy_collisions = pygame.sprite.spritecollide(self.player.player.sprite, self.map.enemies, False)
        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.player.sprite.position.direction.y >= 0:
                    self.STOMP.play()
                    self.player.player.sprite.position.direction.y = -15
                    explosion_sprite = ExplosionParticle(enemy.rect.center)
                    self.explosion_sprites.add(explosion_sprite)
                    enemy.kill()
                else:
                    self.player.player.sprite.status.damage()

    def input(self) -> NoReturn:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.back_to_menu(self.current_level, self.current_level)

    def run(self):
        self.input()
        # Sky
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface, self.WORLD_SHIFT)

        # Background palms
        self.map.bgPalms.update(self.WORLD_SHIFT)
        self.map.bgPalms.draw(self.display_surface)

        # Dust particles
        self.player.dust_sprite.update(self.WORLD_SHIFT)
        self.player.dust_sprite.draw(self.display_surface)

        # Terrain
        self.map.terrain.update(self.WORLD_SHIFT)
        self.map.terrain.draw(self.display_surface)

        # Enemy
        self.map.enemies.update(self.WORLD_SHIFT)
        self.map.constrains.update(self.WORLD_SHIFT)
        self.map.enemy_collision_reverse()
        self.map.enemies.draw(self.display_surface)
        self.explosion_sprites.update(self.WORLD_SHIFT)
        self.explosion_sprites.draw(self.display_surface)

        # Crate
        self.map.crates.update(self.WORLD_SHIFT)
        self.map.crates.draw(self.display_surface)

        # Grass
        self.map.grass.update(self.WORLD_SHIFT)
        self.map.grass.draw(self.display_surface)

        # Coins
        self.map.coins.update(self.WORLD_SHIFT)
        self.map.coins.draw(self.display_surface)

        # Foreground palms
        self.map.fgPalms.update(self.WORLD_SHIFT)
        self.map.fgPalms.draw(self.display_surface)

        # Player sprites
        self.player.player.update()
        self.horizontal_movement_collision()

        self.player.on_ground()
        self.vertical_movement_collision()
        self.player.create_landing()

        self.scroll_x()
        self.player.player.draw(self.display_surface)
        self.player.goal.update(self.WORLD_SHIFT)
        self.player.goal.draw(self.display_surface)

        if self.player.is_death():
            self.back_to_menu(self.current_level, 0)
        if self.player.is_win():
            self.back_to_menu(self.current_level, self.new_level)

        self.check_coin_collisions()
        self.check_enemy_collisions()

        # water
        self.water.draw(self.display_surface, self.WORLD_SHIFT)


__all__ = [
    "Level",
    "LevelData"
]
