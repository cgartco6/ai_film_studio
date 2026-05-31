import json
from studio.timeline import Timeline


class Assembler:

    def __init__(self):

        self.timeline = Timeline()

    def add_render(self, render_data):

        self.timeline.add_scene(render_data)

    def build_project(self):

        return self.timeline.build()

    def save_project(
        self,
        path="storage/renders/project.json"
    ):

        project = self.build_project()

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                project,
                f,
                indent=4,
                ensure_ascii=False
            )

        return path
