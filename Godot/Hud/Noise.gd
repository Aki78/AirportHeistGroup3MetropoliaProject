extends Sprite

func _ready():
	pass # Replace with function body.




func _on_Timer_timeout():
	position.x = rand_range(0, 2000)
	position.y = rand_range(0, 500)
	rotation_degrees = rand_range(-10,10)
