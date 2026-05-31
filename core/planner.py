from core.storyboard import (
    Storyboard,
    Scene,
    AudioTrack,
    CameraSettings
)


class Planner:

    def create_storyboard(
        self,
        prompt: str,
        title: str = "Untitled Film"
    ) -> Storyboard:

        storyboard = Storyboard(
            title=title,
            description=prompt,
            genre="cinematic"
        )

        scene = Scene(
            id=1,
            title="Opening Scene",
            duration=8,
            visual_prompt=prompt,
            action="Establishing cinematic shot",
            narration="The story begins.",
            location="Unknown",
            time_of_day="night",
            camera=CameraSettings(
                shot_type="wide",
                movement="slow_pan",
                lens="35mm"
            ),
            audio=AudioTrack(
                music_prompt="epic cinematic score",
                ambience_prompt="wind ambience",
                voice_prompt="cinematic narrator"
            )
        )

        storyboard.add_scene(scene)

        return storyboard
