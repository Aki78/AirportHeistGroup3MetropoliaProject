extends ColorRect


onready var large_scale = 10

func _ready():
	set_scale(Vector2(1,1))
	start_dialog()

func start_dialog():
	var tween = get_node("Tween")
	tween.interpolate_property(self, "rect_scale",
			Vector2(0,0), Vector2(large_scale,large_scale), 0.5,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
#	stop_dialog()

func stop_dialog():
	var tween = get_node("Tween")
	tween.interpolate_property(self, "rect_scale",
			Vector2(50,50), Vector2(0,0), 0.5,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")

func _input(event):
	if event.is_action_released("ui_up"):
		var ypos = $Row1/Label.rect_position.y
		$RighArrow.position.y = 10

	if event.is_action_released("ui_down"):
		var ypos = $Row2/Label.rect_position.y
		print(ypos)
		$RighArrow.position.y = 20
