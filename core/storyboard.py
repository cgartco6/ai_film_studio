from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
import json


@dataclass
class Character:
    """
    Character definition used throughout the film.
    """

    id: str
    name: str
    description: str = ""
    age: Optional[int] = None
    gender: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CameraSettings:
    """
    Camera configuration for a scene.
    """

    shot_type: str = "medium"
    movement: str = "static"
    lens: str = "50mm"
    framing: str = "center"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AudioTrack:
    """
    Audio generation instructions.
    """

    music_prompt: str = ""
    ambience_prompt: str = ""
    voice_prompt: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Scene:
    """
    Master scene definition.
    Every generation stage uses this object.
    """

    id: int

    title: str

    duration: int

    visual_prompt: str

    dialogue: str = ""

    narration: str = ""

    action: str = ""

    location: str = ""

    time_of_day: str = "day"

    camera: CameraSettings = field(
        default_factory=CameraSettings
    )

    audio: AudioTrack = field(
        default_factory=AudioTrack
    )

    characters: List[Character] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration,
            "visual_prompt": self.visual_prompt,
            "dialogue": self.dialogue,
            "narration": self.narration,
            "action": self.action,
            "location": self.location,
            "time_of_day": self.time_of_day,
            "camera": self.camera.to_dict(),
            "audio": self.audio.to_dict(),
            "characters": [
                c.to_dict()
                for c in self.characters
            ],
            "metadata": self.metadata,
        }


@dataclass
class Storyboard:
    """
    Film storyboard.

    Contains:
    - scenes
    - characters
    - generation metadata
    """

    title: str

    description: str = ""

    genre: str = "cinematic"

    language: str = "en"

    scenes: List[Scene] = field(
        default_factory=list
    )

    characters: List[Character] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    def add_scene(self, scene: Scene):

        self.scenes.append(scene)

    def add_character(self, character: Character):

        self.characters.append(character)

    def total_duration(self) -> int:

        return sum(
            scene.duration
            for scene in self.scenes
        )

    def scene_count(self) -> int:

        return len(self.scenes)

    def to_dict(self) -> Dict[str, Any]:

        return {
            "title": self.title,
            "description": self.description,
            "genre": self.genre,
            "language": self.language,
            "total_duration": self.total_duration(),
            "scene_count": self.scene_count(),
            "characters": [
                c.to_dict()
                for c in self.characters
            ],
            "scenes": [
                s.to_dict()
                for s in self.scenes
            ],
            "metadata": self.metadata,
        }

    def to_json(self) -> str:

        return json.dumps(
            self.to_dict(),
            indent=2,
            ensure_ascii=False
        )

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any]
    ) -> "Storyboard":

        storyboard = cls(
            title=data.get("title", "Untitled"),
            description=data.get(
                "description",
                ""
            ),
            genre=data.get(
                "genre",
                "cinematic"
            ),
            language=data.get(
                "language",
                "en"
            ),
            metadata=data.get(
                "metadata",
                {}
            ),
        )

        for char_data in data.get(
            "characters",
            []
        ):

            storyboard.add_character(
                Character(
                    **char_data
                )
            )

        for scene_data in data.get(
            "scenes",
            []
        ):

            camera = CameraSettings(
                **scene_data.get(
                    "camera",
                    {}
                )
            )

            audio = AudioTrack(
                **scene_data.get(
                    "audio",
                    {}
                )
            )

            characters = [
                Character(**c)
                for c in scene_data.get(
                    "characters",
                    []
                )
            ]

            scene = Scene(
                id=scene_data["id"],
                title=scene_data.get(
                    "title",
                    f"Scene {scene_data['id']}"
                ),
                duration=scene_data.get(
                    "duration",
                    5
                ),
                visual_prompt=scene_data.get(
                    "visual_prompt",
                    ""
                ),
                dialogue=scene_data.get(
                    "dialogue",
                    ""
                ),
                narration=scene_data.get(
                    "narration",
                    ""
                ),
                action=scene_data.get(
                    "action",
                    ""
                ),
                location=scene_data.get(
                    "location",
                    ""
                ),
                time_of_day=scene_data.get(
                    "time_of_day",
                    "day"
                ),
                camera=camera,
                audio=audio,
                characters=characters,
                metadata=scene_data.get(
                    "metadata",
                    {}
                ),
            )

            storyboard.add_scene(scene)

        return storyboard

    @classmethod
    def from_json(
        cls,
        json_string: str
    ) -> "Storyboard":

        return cls.from_dict(
            json.loads(json_string)
        )
