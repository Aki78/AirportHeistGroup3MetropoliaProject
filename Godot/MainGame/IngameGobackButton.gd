extends Button

func _ready():
	pass

func _on_Button_pressed():
	print("Go back to menu")
	get_tree().change_scene("res://Hud/MainMenu.tscn")
