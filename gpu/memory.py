import torch


class MemoryManager:

    @staticmethod
    def clear():
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    @staticmethod
    def allocated():
        if not torch.cuda.is_available():
            return 0

        return torch.cuda.memory_allocated()

    @staticmethod
    def reserved():
        if not torch.cuda.is_available():
            return 0

        return torch.cuda.memory_reserved()
