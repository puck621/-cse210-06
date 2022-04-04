from game.scripting.action import Action


class UnloadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        """Defines sound and physical queues"""
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Starts defined audio and video queues"""
        self._audio_service.unload_sounds()
        self._video_service.unload_fonts()
        self._video_service.unload_images()