

from mr.models.registered_model import RegisteredModel
from ml_metadata.proto import metadata_store_pb2


def to_artifact(registered_model: RegisteredModel, model_type_id: int) -> any:
  model_artifact = metadata_store_pb2.Artifact()
  model_artifact.uri = '/path/to/model'
  model_artifact.name = registered_model.name
  model_artifact.type_id = model_type_id
  return model_artifact

def from_artifact(artifact: any) -> RegisteredModel:
  return RegisteredModel(name=artifact.name)