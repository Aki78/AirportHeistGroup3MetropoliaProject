extends Node2D


export(float) var power = 0.1;
export(float) var maxSize = 100;
export(float) var offsetDecreaseSpeed = 0.1;
export(float) var maxOffsetStrength = 0.178;
export(Vector2) var self_position = Vector2(0,0);
export(float) var delay = 1;


var currentScale = 0;
var currentOffsetStrength = 0;
var expand = false;
var decreaseStrength = false;

onready var timer = Timer.new()

# Called when the node enters the scene tree for the first time.
func _ready():
	self.scale = Vector2.ZERO;
	currentOffsetStrength = maxOffsetStrength;
#	position = self_position
	timer.connect("timeout",self,"_on_timer_timeout")
	timer.one_shot = true
	timer.wait_time = delay
	timer.autostart = true
	add_child(timer)

func _process(delta):
	#self.scale += Vector2.ONE * currentScale;
	if(expand):
		if(self.scale.x < maxSize):
			self.scale += delta*Vector2.ONE * power;
		else:
			expand = false;
			decreaseStrength = true;
	if(!expand && decreaseStrength):
		currentOffsetStrength -= offsetDecreaseSpeed;
		self.material.set_shader_param("offsetStrength", currentOffsetStrength);
		if(currentOffsetStrength <=0):
			_resetObject();
	pass

func _resetObject():
	self.scale = Vector2.ZERO;
	currentOffsetStrength = maxOffsetStrength;
	self.material.set_shader_param("offsetStrength", maxOffsetStrength);
	expand = false;
	decreaseStrength = false;

func _on_timer_timeout():
	expand = true
