class AnimateDiffEngine:

    def generate(self, prompt, output_path):

        # REAL: diffusers AnimateDiff pipeline goes here

        with open(output_path, "w") as f:
            f.write(f"ANIMATEDIFF_VIDEO:{prompt}")

        return output_path
