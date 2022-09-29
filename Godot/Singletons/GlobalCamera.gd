extends Camera2D

var shake_amount = 0.0 setget set_shake
var shake_max_amount = 2.0
onready var pos = global_position

func set_shake(new):
	shake_amount = clamp(new,0.0,shake_max_amount)

#shaking camera
func _process(delta):
	global_position = pos
	global_position.x += rand_range(-shake_amount,shake_amount)
	global_position.y += rand_range(-shake_amount,shake_amount)
	self.shake_amount -= delta*shake_max_amount
