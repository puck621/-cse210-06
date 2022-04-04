from game.scripting.action import Action


class StartDrawingAction(Action):

    def __init__(self, video_service):
        """Defines sound and physical queues"""
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Performs visual cues of drawing object then clearing cache"""
        self._video_service.clear_buffer()