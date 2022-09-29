extends Button

func _ready():
	modulate.a = 0

func _on_ExitButton_pressed():

	get_tree().quit()
