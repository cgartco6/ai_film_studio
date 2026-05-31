import subprocess


class FFmpegEngine:

    def render(self, inputs, output="final_movie.mp4"):

        cmd = ["ffmpeg", "-y"]

        for i in inputs:
            cmd += ["-i", i]

        cmd += ["-filter_complex", "concat=n=1:v=1:a=1", output]

        subprocess.run(cmd)

        return output
