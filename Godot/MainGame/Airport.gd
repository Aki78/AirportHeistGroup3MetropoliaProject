extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Airport_mouse_entered():
#	bubbleAnimation.play("oscilate")
	$Airport.rect_scale = Vector2(2.0,2.0)
	$InfoBox.appear()
	$InfoBox.rect_scale = Vector2(2.0,2.0)
	$InfoBox.rect_position.x += 2000
#	rect_scale = Vector2(bubbleAnimation.osc, bubbleAnimation)

func _on_Airport_mouse_exited():
#	bubbleAnimation.stop(true)
	$Airport.rect_scale = Vector2(1.0,1.0)
	$InfoBox.dissapear()
	$InfoBox.rect_position.x -= 2000
