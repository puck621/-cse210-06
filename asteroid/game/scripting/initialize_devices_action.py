from game.scripting.action import Action


class InitializeDevicesAction(Action):

    def __init__(self, audio_service, video_service):
        """Defines sound and physical queues"""
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Defines the location of the sound and image cues"""
        self._audio_service.initialize()
        self._video_service.initialize()