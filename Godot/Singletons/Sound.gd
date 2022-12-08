extends Node2D

onready var incorrect =AudioStreamPlayer.new()
onready var correct =AudioStreamPlayer.new()
onready var click =AudioStreamPlayer.new()
onready var transition =AudioStreamPlayer.new()
onready var spy =AudioStreamPlayer.new()
onready var hud =AudioStreamPlayer.new()
onready var pink =AudioStreamPlayer.new()
onready var panic =AudioStreamPlayer.new()
onready var victory =AudioStreamPlayer.new()
onready var deep =AudioStreamPlayer.new()

onready var game_over_music =AudioStreamPlayer.new()


onready var voice_smuggler = AudioStreamPlayer.new()

onready var tween_out_node = Tween
onready var tween_out

var transition_duration = 1.00
var transition_type = 1 # TRANS_SINE
#possible use if music doesn't connect well
var current_music

func fade_out(stream_player):
	# tween music volume down to 0
	tween_out.interpolate_property(stream_player, "volume_db", 0, -80, transition_duration, transition_type, Tween.EASE_IN, 0)
	tween_out.start()
	# when the tween ends, the music will be stopped

func _on_TweenOut_tween_completed(object, key):
	# stop the music -- otherwise it continues to run at silent volume
	object.stop()
	object.volume_db = 0
	print("Completed")

func _ready() -> void:
	add_sounds()
	tween_out = tween_out_node.new()
	tween_out.connect("tween_completed",self,"_on_TweenOut_tween_completed")
	add_child(tween_out)

#adding sound node to root
func add_sounds():

	var sound_spy :AudioStream = preload("res://Sounds/Spy.mp3") 
	var sound_hud :AudioStream = preload("res://Sounds/El_Profesor_-_Bella_Ciao_(HUGEL_Remix)_[Lyric_Video]-jhgJV0Pg54Y.mp3") 
	var sound_pink :AudioStream = preload("res://Sounds/The_Pink_Panther_Theme_Music-lp6z3s1Gig0.mp3") 
	var sound_click :AudioStream = preload("res://Sounds/click.mp3") 
	var sound_panic :AudioStream = preload("res://Sounds/dramatic.mp3") 
	var sound_victory :AudioStream = preload("res://Sounds/victory.mp3") 
	var sound_deep :AudioStream = preload("res://Sounds/deep_echo.mp3") 
	var sound_game_over_music :AudioStream = preload("res://Sounds/game_over_music.mp3") 

	var sound_voice_smuggler :AudioStream = preload("res://Voices/frank_smuggler.mp3") 

	spy.set_stream(sound_spy)
	hud.set_stream(sound_hud)
	pink.set_stream(sound_pink)
	click.set_stream(sound_click)
	panic.set_stream(sound_panic)
	victory.set_stream(sound_victory)
	deep.set_stream(sound_deep)
	game_over_music.set_stream(sound_game_over_music)

	voice_smuggler.set_stream(sound_voice_smuggler)

	add_child(spy)
	add_child(hud)
	add_child(pink)
	add_child(click)
	add_child(panic)
	add_child(victory)
	add_child(deep)
	add_child(game_over_music)

	add_child(voice_smuggler)

func play_spy():
	spy.play()
func stop_spy():
	fade_out(spy)
	#spy.stop()

func play_hud():
	hud.play()
func stop_hud():
	fade_out(hud)
	#hud.stop()

func play_pink():
	pink.play()
func stop_pink():
	fade_out(pink)
	#pink.stop()

func play_click():
	click.play()
func stop_click():
	click.stop()

func play_panic():
	panic.play()
func stop_panic():
	fade_out(panic)
	#panic.stop()

func play_victory():
	victory.play()
func stop_victory():
	fade_out(victory)
	#victory.stop()

func play_deep():
	deep.volume_db = 2
	deep.stream.loop = false
	deep.play()
func stop_deep():
	deep.stop()


func play_game_over_music():
	game_over_music.stream.loop = false
	game_over_music.play()
func stop_game_over_music():
	fade_out(game_over_music)
	#game_over_music.stop()

func play_smuggler_voice():
	voice_smuggler.stream.loop = false
	voice_smuggler.play()

