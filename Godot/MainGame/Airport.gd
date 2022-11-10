extends Node2D


func set_pixel_size():
	var is = get_node("sprite").get_texture().get_size() #image size
	var th = 50 #target height
	var tw = 100 #target width
	var scale = Vector2((is.x/(is.x/tw))/50, (is.y/(is.y/th))/50)

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
