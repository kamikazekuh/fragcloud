from colors import Color,RED
from entities.entity import Entity
from events import Event
from listeners import OnEntityDeleted, OnEntityCreated
from messages import Shake, Fade
from players.entity import Player
from stringtables import string_tables


fade_color = Color(255, 11, 11)
fade_message = Fade(duration=1, hold_time=1, color=fade_color.with_alpha(150))

@OnEntityDeleted
def on_entity_deleted(base_entity):
    if base_entity.classname in ['npc_grenade_frag','grenade_ar2']:
        create_particle(base_entity.origin, "fire_large_01",5.0)
        create_light(base_entity.origin,5.0)
        


@Event('player_death')
def player_death(ev):
    if ev['attacker'] != 0 and ev['userid'] != 0:
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
        
        
def create_particle(position,particle_name,duration):
    entity = Entity.create("info_particle_system")
    entity.effect_name = particle_name
    entity.effect_index = string_tables.ParticleEffectNames.add_string(particle_name)
    entity.origin = position
    entity.start()
    entity.delay(duration,entity.call_input,("Kill",))
    
def create_light(position,duration):
    entity = Entity.create("light_dynamic")
    entity.inner_cone = 0
    entity.cone = 80
    entity.brightness = 1
    entity.spotlight_radius = 240.0
    entity.distance = 300.0
    entity.color = Color(255,100,10)
    entity.pitch = -90
    entity.style = 5
    entity.origin = position
    entity.spawn()
    entity.call_input("TurnOn")
    entity.delay(duration,entity.call_input,("Kill",))
