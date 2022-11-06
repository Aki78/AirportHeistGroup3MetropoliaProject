extends Sprite

func _ready():
	CameraScript.my_ease_in(self)
	Sound.stop_panic()
	Sound.play_victory()



func _on_WonScene_tree_exiting():
	Sound.stop_victory()
