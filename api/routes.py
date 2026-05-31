from fastapi import APIRouter

from core.planner import Planner
from pipeline.director import Director
from studio.assembler import Assembler


router = APIRouter()

planner = Planner()
director = Director()


@router.get("/health")
def health():

    return {
        "status": "ok"
    }


@router.post("/generate")
def generate(prompt: str):

    storyboard = planner.create_storyboard(
        prompt=prompt,
        title="Generated Film"
    )

    renders = director.execute_storyboard(
        storyboard
    )

    assembler = Assembler()

    for render in renders:
        assembler.add_render(render)

    project_file = assembler.save_project()

    return {
        "success": True,
        "project": project_file,
        "scene_count": len(
            storyboard.scenes
        )
    }
