extends Sprite


var rot_speed = 10

func _ready():
	pass



func _physics_process(delta):
	rotation_degrees += rot_speed *delta
