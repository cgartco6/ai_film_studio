class Wav2Lip:

    def apply(self, video, audio, output):

        with open(output, "w") as f:
            f.write(f"LIPSYNC:{video}+{audio}")

        return output
