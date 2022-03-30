from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        Bullet = cast.get_first_actor(BULLET_GROUP)
        body = Bullet.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            cast.remove_actor(BULLET_GROUP, Bullet)

        elif x >= (FIELD_RIGHT - BULLET_WIDTH):
            cast.remove_actor(BULLET_GROUP, Bullet)

        if y < FIELD_TOP:
            cast.remove_actor(BULLET_GROUP, Bullet)

        elif y >= (FIELD_BOTTOM - BULLET_WIDTH):
            cast.remove_actor(BULLET_GROUP, Bullet)

            #stats = cast.get_first_actor(STATS_GROUP)
            #stats.lose_life()
            
           # if stats.get_lives() > 0:
            #    callback.on_next(TRY_AGAIN) 
            #else:
             #   callback.on_next(GAME_OVER)
              #  self._audio_service.play_sound(over_sound)