from models.animate_diff import AnimateDiffEngine


class VideoWorker:

    def __init__(self):

        self.engine = AnimateDiffEngine()

    def render_scene(self, scene):

        output_path = (
            f"storage/renders/video_scene_{scene.id}.mp4"
        )

        self.engine.generate(
            prompt=scene.visual_prompt,
            output_path=output_path
        )

        return output_path
