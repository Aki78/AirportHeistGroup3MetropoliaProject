extends Node2D

onready var incorrect =AudioStreamPlayer.new()
onready var correct =AudioStreamPlayer.new()
onready var click =AudioStreamPlayer.new()
onready var transition =AudioStreamPlayer.new()
onready var spy =AudioStreamPlayer.new()
onready var hud =AudioStreamPlayer.new()
onready var place_holder3 =AudioStreamPlayer.new()
onready var place_holder4 =AudioStreamPlayer.new()
onready var place_holder5 =AudioStreamPlayer.new()
onready var place_holder6 =AudioStreamPlayer.new()
onready var place_holder7 =AudioStreamPlayer.new()
onready var place_holder8 =AudioStreamPlayer.new()
onready var place_holder9 =AudioStreamPlayer.new()
onready var place_holder10 =AudioStreamPlayer.new()
onready var place_holder11 =AudioStreamPlayer.new()

func _ready() -> void:
	add_sounds()

#adding sound node to root
func add_sounds():
	#var sound_incorrect :AudioStream = preload("res://Resources/incorrect.ogg") 
	#var sound_correct :AudioStream = preload("res://Resources/correct.ogg") 
	#var sound_click :AudioStream = preload("res://Resources/Bluezone_BC0268_switch_button_click_small_005.wav") 
	#var sound_transition :AudioStream = preload("res://Resources/transition1.wav") 
	var sound_spy :AudioStream = preload("res://Sounds/41_Minutes_of_Spy_Music_-_Instrumental_Spy_Themes-XZBp0VvuUhQ.mp3") 
	var sound_hud :AudioStream = preload("res://Sounds/El_Profesor_-_Bella_Ciao_(HUGEL_Remix)_[Lyric_Video]-jhgJV0Pg54Y.mp3") 
	#var sound_placeholder3 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder4 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder5 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder6 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder7 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder8 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder9 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder10 :AudioStream = preload("res://Resources/transition1.wav") 
	#var sound_placeholder11 :AudioStream = preload("res://Resources/transition1.wav") 
	#incorrect.set_stream(sound_incorrect)
	#correct.set_stream(sound_correct)
	#click.set_stream(sound_click)
	#transition.set_stream(sound_transition)
	spy.set_stream(sound_spy)
	hud.set_stream(sound_hud)
	#place_holder3.set_stream(sound_placeholder3)
	#place_holder4.set_stream(sound_placeholder4)
	#place_holder5.set_stream(sound_placeholder5)
	#place_holder6.set_stream(sound_placeholder6)
	#place_holder7.set_stream(sound_placeholder7)
	#place_holder8.set_stream(sound_placeholder8)
	#place_holder9.set_stream(sound_placeholder9)
	#place_holder10.set_stream(sound_placeholder10)
	#place_holder11.set_stream(sound_placeholder11)
	#add_child(incorrect)
	#add_child(correct)
	#add_child(click)
	#add_child(transition)
	add_child(spy)
	add_child(hud)
	#add_child(place_holder3)
	#add_child(place_holder4)
	#add_child(place_holder5)
	#add_child(place_holder6)
	#add_child(place_holder7)
	#add_child(place_holder8)
	#add_child(place_holder9)
	#add_child(place_holder10)
	#add_child(place_holder11)

#func play_incorrect():
	#incorrect.play()

#func play_correct():
	#correct.play()

#func play_click():
	#click.play()

#func play_transition():
	#transition.play()

func play_spy():
	spy.play()
func stop_spy():
	spy.stop()


func play_hud():
	hud.play()
func stop_hud():
	hud.stop()
#func play_placeholder2():
	#transition.play()
#func play_placeholder3():
	#transition.play()
#func play_placeholder4():
	#transition.play()
#func play_placeholder5():
	#transition.play()
#func play_placeholder6():
	#transition.play()
#func play_placeholder7():
	#transition.play()
#func play_placeholder8():
	#transition.play()
#func play_placeholder9():
	#transition.play()
#func play_placeholder10():
	#transition.play()
#func play_placeholder11():
	#transition.play()

