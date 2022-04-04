from game.scripting.action import Action
from constants import *

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        """Defines sound and physical queues"""
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Loads sound from assests folder"""
        self._audio_service.load_sounds(ROOT + "/assets/sounds")
        self._video_service.load_fonts(ROOT + "/assets/fonts")
        self._video_service.load_images(ROOT + "/assets/images")