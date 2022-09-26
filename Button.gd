extends Button


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	print("Button")


func _on_Button_pressed():
	#print("Pressed")
	$Label.text = "Pressed"
	get_tree().change_scene("res://BackGround.tscn")
