class Timeline:

    def __init__(self):

        self.tracks = []

    def add_scene(self, render_data):

        self.tracks.append(render_data)

    def build(self):

        timeline = []

        current_time = 0

        for item in self.tracks:

            timeline.append(
                {
                    "scene_id": item["scene_id"],
                    "start": current_time,
                    "video": item["video"],
                    "music": item["music"],
                    "voice": item["voice"]
                }
            )

            current_time += 1

        return timeline
