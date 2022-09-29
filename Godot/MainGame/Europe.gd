extends Sprite

export var AirportScene : PackedScene

onready var airports = []

func _ready():
	randomize()
	CameraScript.my_ease_in(self)
	for i in range(100):
		var airport = AirportScene.instance()
		airport.rect_position.x = rand_range(-100,100)*i
		airport.rect_position.y = rand_range(-100,100)*i
		airports.append(airport)
		add_child(airport)

func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
