
import typing

from grpc import insecure_channel
from ml_metadata.proto import metadata_store_pb2
from ml_metadata.proto import metadata_store_service_pb2
from ml_metadata.proto import metadata_store_service_pb2_grpc
from mr.models.registered_model import RegisteredModel
from mr.service.mapper import from_artifact, to_artifact


channel = insecure_channel('localhost:8080')
store = metadata_store_service_pb2_grpc.MetadataStoreServiceStub(channel)

class ModelService:
  
  type_name = "mlmd.Model"
  
  def __init__(self) -> None:
    req = metadata_store_service_pb2.GetArtifactTypeRequest()
    req.type_name = self.type_name
    resp = store.GetArtifactType(req)
    self.artifact_id = resp.artifact_type.id
  
  def create_registered_model(self, reg_model: RegisteredModel) -> int:
    req = metadata_store_service_pb2.PutArtifactsRequest()
    model_artifact = to_artifact(reg_model, self.artifact_id)
    req.artifacts.MergeFrom([model_artifact])
    
    resp = store.PutArtifacts(req)
    return resp.artifact_ids[0]
    
  def get_registered_models(self) -> typing.List[RegisteredModel]:
    req = metadata_store_service_pb2.GetArtifactsByTypeRequest()
    req.type_name = self.type_name
    
    resp = store.GetArtifactsByType(req)
    return list(map(from_artifact, resp.artifacts))
