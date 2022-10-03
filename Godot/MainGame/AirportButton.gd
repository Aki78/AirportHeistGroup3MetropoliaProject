extends TextureButton

var mouse_out
var mouse_over

var own_index

onready var bubbleAnimation = $AnimationPlayer

func _ready():
	rect_scale = Vector2(0.05,0.05)
#	modulate.g =255

func init(index):
	own_index = index

func _on_TextureButton_mouse_entered():
#	bubbleAnimation.play("oscilate")
	rect_scale = Vector2(0.1,0.1)
	$InfoBox.appear()
#	rect_scale = Vector2(bubbleAnimation.osc, bubbleAnimation)

func _on_TextureButton_mouse_exited():
#	bubbleAnimation.stop(true)
	rect_scale = Vector2(0.05,0.05)
	$InfoBox.dissapear()
	
func add_info(name,coordinate, distance, price, co2):
	$InfoBox.add_info(name,coordinate, distance, price, co2)

func _on_Airport_pressed():
	if own_index in Http.closest_list:
		Http.send_move(own_index)
