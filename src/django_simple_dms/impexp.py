from abc import ABC, abstractmethod

class Importer(ABC):
    @abstractmethod
    def import_file(self, file_path, *args, **kwargs):
        pass