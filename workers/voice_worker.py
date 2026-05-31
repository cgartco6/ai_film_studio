from models.xtts import XTTS


class VoiceWorker:

    def __init__(self):

        self.tts = XTTS()

    def render_voice(self, scene):

        output_path = (
            f"storage/renders/voice_scene_{scene.id}.wav"
        )

        text = scene.dialogue

        if not text:
            text = scene.narration

        self.tts.synthesize(
            text=text,
            output_path=output_path
        )

        return output_path
