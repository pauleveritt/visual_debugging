import random

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title) -> None:
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0

        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite('character.png', 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        # Stepping 1
        self.coin_list = arcade.SpriteList()
        for i in range(50):
            coin = arcade.Sprite('coin_01.png', 0.2)
            # Stack Frames
            coin.center_x = random.randrange(600)
            coin.center_y = random.randrange(600)
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        # Poking Around
        output = 'Score: %02d' % self.score
        # output = f'Score: {self.score:02d}'
        arcade.draw_text(output, 100, 100, arcade.color.WHITE)
        self.all_sprites_list.draw()

    def update(self, delta_time):
        # Breakpoints
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.coin_list
        )
        for coin in hit_list:
            coin.kill()
            # Stepping 2
            self.score += 1

    def on_mouse_motion(self, x, y, dx, dy):
        # Old-fashioned
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()


def main():
    MyGame(600, 600, 'My Awesome Game')
    arcade.run()


if __name__ == '__main__':
    main()
