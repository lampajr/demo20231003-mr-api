import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from mr.models.registered_model import RegisteredModel  # noqa: E501
from mr import util
from mr.service.model_service import ModelService

model_service = ModelService()

def create_registered_model():  # noqa: E501
    """Create a RegisteredModel

    Creates a new instance of a &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registered_model: A new &#x60;RegisteredModel&#x60; to be created.
    :type registered_model: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        registered_model = RegisteredModel.from_dict(connexion.request.get_json())  # noqa: E501
        model_service.create_registered_model(registered_model)
        return None, 200
    return 'Invalid request body', 400


def delete_registered_model():  # noqa: E501
    """Delete a RegisteredModel

    Deletes an existing &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registeredmodel_id: A unique identifier for a &#x60;RegisteredModel&#x60;.
    :type registeredmodel_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_registered_model():  # noqa: E501
    """Get a RegisteredModel

    Gets the details of a single instance of a &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registeredmodel_id: A unique identifier for a &#x60;RegisteredModel&#x60;.
    :type registeredmodel_id: str

    :rtype: Union[RegisteredModel, Tuple[RegisteredModel, int], Tuple[RegisteredModel, int, Dict[str, str]]
    """
    return 'Not yet implemented', 500


def get_registered_models():  # noqa: E501
    """List All RegisteredModels

    Gets a list of all &#x60;RegisteredModel&#x60; entities. # noqa: E501


    :rtype: Union[List[RegisteredModel], Tuple[List[RegisteredModel], int], Tuple[List[RegisteredModel], int, Dict[str, str]]
    """
    return model_service.get_registered_models()


def update_registered_model():  # noqa: E501
    """Update a RegisteredModel

    Updates an existing &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registeredmodel_id: A unique identifier for a &#x60;RegisteredModel&#x60;.
    :type registeredmodel_id: str
    :param registered_model: Updated &#x60;RegisteredModel&#x60; information.
    :type registered_model: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        registered_model = RegisteredModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'Not yet implemented', 500
