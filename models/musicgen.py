class MusicGen:

    def generate(self, prompt, output_path):

        with open(output_path, "w") as f:
            f.write(f"MUSICGEN:{prompt}")

        return output_path
