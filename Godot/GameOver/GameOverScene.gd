extends Sprite


func _ready():
	Sound.stop_panic()
	Sound.stop_victory()
	Sound.play_game_over_music()
