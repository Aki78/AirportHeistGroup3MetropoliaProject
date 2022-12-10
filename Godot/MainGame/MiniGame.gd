extends Node2D

var total_success

signal heist_success

func init(speed):
	total_success = 0
		
	for _i in get_children():
		_i.connect("success", self, "_on_success", [_i])
	for _i in get_children():
		_i.init(speed)

func _on_success(arrow):
	
	arrow.disconnect("success", self, "_on_success")
	total_success += 1
	print(total_success)
	if total_success == get_child_count():
		emit_signal("heist_success")
