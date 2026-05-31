from models.musicgen import MusicGen


class AudioWorker:

    def __init__(self):

        self.music = MusicGen()

    def render_music(self, scene):

        output_path = (
            f"storage/renders/music_scene_{scene.id}.wav"
        )

        self.music.generate(
            prompt=scene.audio.music_prompt,
            output_path=output_path
        )

        return output_path
