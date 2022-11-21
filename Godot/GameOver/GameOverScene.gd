extends Sprite


func _ready():
	Sound.stop_panic()
	Sound.play_game_over_music()
