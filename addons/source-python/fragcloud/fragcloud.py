from colors import Color
from entities.entity import Entity
from events import Event
from messages import Shake, Fade
from players.entity import Player

fade_color = Color(255, 11, 11)
fade_message = Fade(duration=1, hold_time=1, color=fade_color.with_alpha(150))

@Event('player_death')
def player_death(ev):
    victim = Player.from_userid(ev['userid'])
    attacker = Player.from_userid(ev['attacker'])
    if ev['weapon'] == "combine_ball":
        fade_message.send(attacker.index)
        Shake(amplitude=5, duration=1, frequency=7).send(attacker.index)
        ar2 = Entity.create('env_ar2explosion') 
        ar2.material = "materials/orbsmoke1.vmt"
        ar2.origin = victim.origin
        ar2.spawn()
        ar2.call_input("Explode")
        ar2.call_input("Kill")
    if ev['weapon'] == "smg1_grenade":
        fade_message.send(attacker.index)
        Shake(amplitude=5, duration=1, frequency=7).send(attacker.index)
        ar2 = Entity.create('env_ar2explosion') 
        ar2.material = "materials/orbsmoke5.vmt"
        ar2.origin = victim.origin
        ar2.spawn()
        ar2.call_input("Explode")
        ar2.call_input("Kill")
    if ev['weapon'] == "grenade_frag":
        fade_message.send(attacker.index)
        Shake(amplitude=5, duration=1, frequency=7).send(attacker.index)
        ar2 = Entity.create('env_ar2explosion') 
        ar2.material = "materials/smokeball2.vmt"
        ar2.origin = victim.origin
        ar2.spawn()
        ar2.call_input("Explode")
        ar2.call_input("Kill")
    if ev['weapon'] == "rpg_missile":
        fade_message.send(attacker.index)
        Shake(amplitude=5, duration=1, frequency=7).send(attacker.index)
        ar2 = Entity.create('env_ar2explosion') 
        ar2.material = "materials/smoke.vmt"
        ar2.origin = victim.origin
        ar2.spawn()
        ar2.call_input("Explode")
        ar2.call_input("Kill")
