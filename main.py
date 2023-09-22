tiles.set_current_tilemap(tilemap("level"))
char = sprites.create(assets.image("Cook down"), SpriteKind.player)
controller.move_sprite(char)