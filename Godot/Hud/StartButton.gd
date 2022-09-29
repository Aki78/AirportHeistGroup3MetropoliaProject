extends Button

func _ready():
	modulate.a = 0
func _on_StartButton_pressed():

	get_tree().change_scene("res://MainGame/GameScreen.tscn")
