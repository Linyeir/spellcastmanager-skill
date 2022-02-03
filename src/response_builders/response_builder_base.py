from abc import ABC, abstractmethod

"""
interface for response builders, that forces the developer to implement get_response correctly
"""


class ResponseBuilderBase(ABC):
    """
    defines interface for ResponseBuilder classes
    """
    @abstractmethod
    def get_response(detail: str, casting_level: str) -> dict:
        pass
