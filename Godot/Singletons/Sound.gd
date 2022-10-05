extends Node2D

onready var incorrect =AudioStreamPlayer.new()
onready var correct =AudioStreamPlayer.new()
onready var click =AudioStreamPlayer.new()
onready var transition =AudioStreamPlayer.new()
onready var spy =AudioStreamPlayer.new()
onready var hud =AudioStreamPlayer.new()
onready var pink =AudioStreamPlayer.new()
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

	var sound_spy :AudioStream = preload("res://Sounds/41_Minutes_of_Spy_Music_-_Instrumental_Spy_Themes-XZBp0VvuUhQ.mp3") 
	var sound_hud :AudioStream = preload("res://Sounds/El_Profesor_-_Bella_Ciao_(HUGEL_Remix)_[Lyric_Video]-jhgJV0Pg54Y.mp3") 
	var sound_pink :AudioStream = preload("res://Sounds/The_Pink_Panther_Theme_Music-lp6z3s1Gig0.mp3") 

	spy.set_stream(sound_spy)
	hud.set_stream(sound_hud)
	pink.set_stream(sound_pink)

	add_child(spy)
	add_child(hud)
	add_child(pink)

func play_spy():
	spy.play()
func stop_spy():
	spy.stop()

func play_hud():
	hud.play()
func stop_hud():
	hud.stop()

func play_pink():
	pink.play()
func stop_pink():
	pink.stop()

