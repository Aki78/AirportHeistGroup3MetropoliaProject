extends ColorRect

onready var Airport = $TextureButton


func _ready():
	var airport2 = Airport.duplicate()
	airport2.rect_position.x += 100 
	add_child(airport2)
	

