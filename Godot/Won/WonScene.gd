extends Sprite

func _ready():
	CameraScript.my_ease_in(self, 5)
	Sound.stop_panic()
	Sound.stop_game_over_music()
	var score = State.load_score()
	print(score)
	$Score.text = str(score)

func _on_WonScene_tree_exiting():
	Sound.stop_victory()



func _on_Button_pressed():
	$HTTPRequest.request('https://Aki78.pythonanywhere.com/updatescore?username=bbb&score=1000',
	[],
	true,
	 8,
	JSON.print("{}"))


func _on_LineEdit_text_changed(new_text):
	pass # Replace with function body.
