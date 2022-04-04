from game.scripting.action import Action


class EndDrawingAction(Action):

    def __init__(self, video_service):
        """Defines sound and physical cue"""
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """End the use of an image"""
        self._video_service.flush_buffer()