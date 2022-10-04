extends Sprite


var rot_speed = -5

func _ready():
	pass



func _physics_process(delta):
	rotation_degrees += rot_speed *delta
