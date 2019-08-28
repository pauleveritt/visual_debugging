from game import MyGame


def test_setup():
    game = MyGame(100, 100, 'Test')
    assert game.is_stopped is True


def test_not_stopped():
    game = MyGame(100, 100, 'Test')
    game.is_stopped = False
    game.on_draw()
    assert game.is_stopped is True


def test_stopped():
    game = MyGame(100, 100, 'Test')
    game.is_stopped = True
    game.on_draw()
    assert game.is_stopped is True
