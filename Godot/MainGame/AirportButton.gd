extends TextureButton

var mouse_out
var mouse_over

var own_index

var self_size = 5
var extended_size = 15

onready var bubbleAnimation = $AnimationPlayer

func _ready():
#	rect_scale = Vector2(1.0,1.0)
#	self.rect_size=Vector2(self_size,self_size)
	set_button_scale(self_size,self_size)

func init(index):
	own_index = index

func add_info(name,coordinate, distance, price, co2):
	$InfoBox.add_info(name,coordinate, distance, price, co2)

func _on_Airport_mouse_entered():
#	self.rect_size = Vector2(extended_size,extended_size)
	print("Entered")
#	rect_size.x = 100
	set_button_scale(extended_size,extended_size)
	$InfoBox.appear()


func _on_Airport_mouse_exited():
#	self.rect_size=Vector2(self_size,self_size)
	set_button_scale(self_size,self_size)
	$InfoBox.dissapear()

func set_button_scale(x,y):
	var size = rect_size
	var myscale = Vector2((size.x/(size.x/x))/50, (size.y/(size.y/y))/50)
	self.set_scale(myscale)

func _on_Airport_pressed():
	pass 
