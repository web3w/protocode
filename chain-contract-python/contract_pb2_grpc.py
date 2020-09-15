# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chain_contract import contract_pb2 as chain__contract_dot_contract__pb2


class ChainContractServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Invoke = channel.unary_unary(
        '/contract.api.ChainContractService/Invoke',
        request_serializer=chain__contract_dot_contract__pb2.InvokeRequest.SerializeToString,
        response_deserializer=chain__contract_dot_contract__pb2.InvokeResponse.FromString,
        )
    self.Transfer = channel.unary_unary(
        '/contract.api.ChainContractService/Transfer',
        request_serializer=chain__contract_dot_contract__pb2.TransferRequest.SerializeToString,
        response_deserializer=chain__contract_dot_contract__pb2.TransferResponse.FromString,
        )
    self.GetBalance = channel.unary_unary(
        '/contract.api.ChainContractService/GetBalance',
        request_serializer=chain__contract_dot_contract__pb2.GetBalanceRequest.SerializeToString,
        response_deserializer=chain__contract_dot_contract__pb2.GetBalanceResponse.FromString,
        )


class ChainContractServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Invoke(self, request, context):
    """通用合约操作
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Transfer(self, request, context):
    """transfer
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBalance(self, request, context):
    """GetBalance
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChainContractServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Invoke': grpc.unary_unary_rpc_method_handler(
          servicer.Invoke,
          request_deserializer=chain__contract_dot_contract__pb2.InvokeRequest.FromString,
          response_serializer=chain__contract_dot_contract__pb2.InvokeResponse.SerializeToString,
      ),
      'Transfer': grpc.unary_unary_rpc_method_handler(
          servicer.Transfer,
          request_deserializer=chain__contract_dot_contract__pb2.TransferRequest.FromString,
          response_serializer=chain__contract_dot_contract__pb2.TransferResponse.SerializeToString,
      ),
      'GetBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetBalance,
          request_deserializer=chain__contract_dot_contract__pb2.GetBalanceRequest.FromString,
          response_serializer=chain__contract_dot_contract__pb2.GetBalanceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'contract.api.ChainContractService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
