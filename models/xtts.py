class XTTS:

    def synthesize(self, text, output_path):

        with open(output_path, "w") as f:
            f.write(f"XTTS:{text}")

        return output_path
