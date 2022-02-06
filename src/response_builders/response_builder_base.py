from abc import ABC, abstractmethod

class ResponseBuilderBase(ABC):
    """
    defines an interface for response builders, that forces the developer to implement get_response correctly
    """
    
    @abstractmethod
    def get_response(detail: str, casting_level: str) -> dict:
        pass
