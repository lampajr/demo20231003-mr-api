import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from mr.models.registered_model import RegisteredModel  # noqa: E501
from mr.models.versioned_model import VersionedModel  # noqa: E501
from mr import util


def create_registered_model(registered_model):  # noqa: E501
    """Create a RegisteredModel

    Creates a new instance of a &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registered_model: A new &#x60;RegisteredModel&#x60; to be created.
    :type registered_model: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        registered_model = RegisteredModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_versioned_model(versioned_model):  # noqa: E501
    """Create a VersionedModel

    Creates a new instance of a &#x60;VersionedModel&#x60;. # noqa: E501

    :param versioned_model: A new &#x60;VersionedModel&#x60; to be created.
    :type versioned_model: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        versioned_model = VersionedModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_registered_model(registeredmodel_id):  # noqa: E501
    """Delete a RegisteredModel

    Deletes an existing &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registeredmodel_id: A unique identifier for a &#x60;RegisteredModel&#x60;.
    :type registeredmodel_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_versioned_model(versionedmodel_id):  # noqa: E501
    """Delete a VersionedModel

    Deletes an existing &#x60;VersionedModel&#x60;. # noqa: E501

    :param versionedmodel_id: A unique identifier for a &#x60;VersionedModel&#x60;.
    :type versionedmodel_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_registered_model(registeredmodel_id):  # noqa: E501
    """Get a RegisteredModel

    Gets the details of a single instance of a &#x60;RegisteredModel&#x60;. # noqa: E501

    :param registeredmodel_id: A unique identifier for a &#x60;RegisteredModel&#x60;.
    :type registeredmodel_id: str

    :rtype: Union[RegisteredModel, Tuple[RegisteredModel, int], Tuple[RegisteredModel, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_registered_models():  # noqa: E501
    """List All RegisteredModels

    Gets a list of all &#x60;RegisteredModel&#x60; entities. # noqa: E501


    :rtype: Union[List[RegisteredModel], Tuple[List[RegisteredModel], int], Tuple[List[RegisteredModel], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_versioned_model(versionedmodel_id):  # noqa: E501
    """Get a VersionedModel

    Gets the details of a single instance of a &#x60;VersionedModel&#x60;. # noqa: E501

    :param versionedmodel_id: A unique identifier for a &#x60;VersionedModel&#x60;.
    :type versionedmodel_id: str

    :rtype: Union[VersionedModel, Tuple[VersionedModel, int], Tuple[VersionedModel, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_versioned_models():  # noqa: E501
    """List All VersionedModels

    Gets a list of all &#x60;VersionedModel&#x60; entities. # noqa: E501


    :rtype: Union[List[VersionedModel], Tuple[List[VersionedModel], int], Tuple[List[VersionedModel], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_registered_model(registeredmodel_id, registered_model):  # noqa: E501
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
    return 'do some magic!'


def update_versioned_model(versionedmodel_id, versioned_model):  # noqa: E501
    """Update a VersionedModel only on updatable fields

    Updates an existing &#x60;VersionedModel&#x60; only on updatable fields. # noqa: E501

    :param versionedmodel_id: A unique identifier for a &#x60;VersionedModel&#x60;.
    :type versionedmodel_id: str
    :param versioned_model: Updated &#x60;VersionedModel&#x60; information.
    :type versioned_model: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        versioned_model = VersionedModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
