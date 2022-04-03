from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideasteroidAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        asteroids = cast.get_actors(ASTEROIDS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for asteroid in asteroids:
            for bullet in bullets:

                if asteroid.get_destroyed() or bullet.get_destroyed():
                  continue

                Bullet_body = bullet.get_body()
                asteroid_body = asteroid.get_body()

                if self._physics_service.has_collided(Bullet_body, asteroid_body):
                    asteroid.destroy()
                    bullet.destroy()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    points = asteroid.get_points()
                    stats.add_points(points)
                    cast.remove_actor(ASTEROIDS_GROUP, asteroid)
                    cast.remove_actor(BULLET_GROUP, bullet)
