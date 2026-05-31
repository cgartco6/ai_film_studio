import torch


class DeviceManager:

    @staticmethod
    def get_device() -> str:
        return "cuda" if torch.cuda.is_available() else "cpu"

    @staticmethod
    def gpu_count() -> int:
        return torch.cuda.device_count()

    @staticmethod
    def gpu_name(index: int = 0) -> str:
        if not torch.cuda.is_available():
            return "CPU"

        return torch.cuda.get_device_name(index)
