extends Sprite

func _ready():
	CameraScript.my_ease_in(self, 5)
	Sound.stop_panic()
	var score = State.load_score()
	print(score)
	$Score.text = str(score)

func _on_WonScene_tree_exiting():
	Sound.stop_victory()

