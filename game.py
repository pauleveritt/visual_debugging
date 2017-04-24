import arcade as arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0

        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite('character.png', 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        output = 'Score: %02d' % self.score
        arcade.draw_text(output, 100, 100, arcade.color.WHITE)
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.all_sprites_list.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    MyGame(600, 600, 'My Game')
    arcade.run()


if __name__ == '__main__':
    main()
