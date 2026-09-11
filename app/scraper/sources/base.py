from abc import ABC, abstractmethod


class PropertySource(ABC):

    @abstractmethod
    def fetch(self, url):
        pass