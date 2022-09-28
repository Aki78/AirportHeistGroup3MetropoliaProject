extends Node2D

onready var camera_script = preload("res://Singletons/GlobalCamera.gd")
onready var camera = Camera2D.new()

func _ready() -> void:
	set_camera()

# adding camera to root	
func set_camera():
	camera.set_script(camera_script)
	camera.make_current()
	camera.process_mode = 1
	camera.anchor_mode = 0
	add_child(camera)
	
func shake_cam():
	camera.shake_amount += 2.0

# ease in for scene, used in ready() input usually is self
func my_ease_in(my_self, duration = 0.5):
	my_self.modulate.a = 0
	var anima := Anima.begin(my_self)
	anima.then({animate = my_self, items_delay = duration,
	 property = 'opacity', from = 0, to = 1 })
	anima.play()
	return anima

# ease out scene, must yield(anima, "animation_completed") aftewards.
func my_ease_out(my_self, duration = 0.5):
	var anima := Anima.begin(my_self)
	anima.then({animate = my_self, items_delay = duration,
	 property = 'opacity', from = 1, to = 0 })
	anima.play()
	return anima

#animating children of VBoxContainer
func animate_list(vnode, d = 0.3):
	var anima := Anima.begin(vnode)
	anima.then({group = vnode, items_delay = d, 
	 property = 'opacity', from = 0, to = 1.0 })
	anima.with({group = vnode, items_delay = d, duration = 0.5,
	 property = 'x', easing = Anima.EASING.EASE_OUT_BACK, from=-100, to =0 })

	anima.play()
	
#animating children of VBoxContainer
func animate_list_out(vnode, d = 0.3):
	var anima := Anima.begin(vnode)
	anima.then({group = vnode, items_delay = d,
	 property = 'opacity', from = 1, to = 0 })
	anima.with({group = vnode, items_delay = d, duration = d,
	 property = 'x',from=0, to =-100 })
	anima.play()

#animating children of VBoxContainer
func move_right(my_self, d = 0.1, pixels = 20):
	var anima := Anima.begin(my_self)
	anima.then({animate = my_self , duration = d,
	 property = 'x',from=0, to=pixels })
	anima.play()
	
func move_left(my_self, d = 0.1, pixels = 20):
	var anima := Anima.begin(my_self)
	anima.then({animate = my_self, duration = d,
	 property = 'x',from=pixels, to= -pixels })
	anima.play()

func blink_red(my_self, d = 3, f = 0.3):
	var anima := Anima.begin(my_self)
	for i in range(int(d / f)):
		anima.then({animate = my_self, duration = f / 2,
		 property = 'opacity',from=0, to=1 })
		anima.then({animate = my_self, duration = f / 2,
		 property = 'opacity',from=1, to=0 })
	anima.play()
	
