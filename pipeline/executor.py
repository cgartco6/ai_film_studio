from models.animate_diff import AnimateDiffEngine
from models.xtts import XTTS
from models.musicgen import MusicGen
from models.wav2lip import Wav2Lip


class Executor:

    def __init__(self):

        self.video = AnimateDiffEngine()
        self.voice = XTTS()
        self.music = MusicGen()
        self.lipsync = Wav2Lip()

    def run_scene(self, scene):

        v = f"storage/renders/v_{scene['id']}.mp4"
        a = f"storage/renders/a_{scene['id']}.wav"
        m = f"storage/renders/m_{scene['id']}.wav"
        f = f"storage/renders/f_{scene['id']}.mp4"

        audio = self.voice.synthesize(scene["dialogue"], a)
        video = self.video.generate(scene["visual"], v)
        music = self.music.generate(scene["music"], m)

        final = self.lipsync.apply(video, audio, f)

        return final
