from workers.video_worker import VideoWorker
from workers.audio_worker import AudioWorker
from workers.voice_worker import VoiceWorker


class Director:

    def __init__(self):

        self.video_worker = VideoWorker()
        self.audio_worker = AudioWorker()
        self.voice_worker = VoiceWorker()

    def execute_scene(self, scene):

        video = self.video_worker.render_scene(scene)

        music = self.audio_worker.render_music(scene)

        voice = self.voice_worker.render_voice(scene)

        return {
            "scene_id": scene.id,
            "video": video,
            "music": music,
            "voice": voice
        }

    def execute_storyboard(self, storyboard):

        results = []

        for scene in storyboard.scenes:

            results.append(
                self.execute_scene(scene)
            )

        return results
