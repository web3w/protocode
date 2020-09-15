# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chain_query import query_pb2 as chain__query_dot_query__pb2


class ChainQueryServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetBalance = channel.unary_unary(
        '/chainquery.api.ChainQueryService/GetBalance',
        request_serializer=chain__query_dot_query__pb2.GetBalanceRequest.SerializeToString,
        response_deserializer=chain__query_dot_query__pb2.GetBalanceResponse.FromString,
        )
    self.ListUnspent = channel.unary_unary(
        '/chainquery.api.ChainQueryService/ListUnspent',
        request_serializer=chain__query_dot_query__pb2.ListUnspentRequest.SerializeToString,
        response_deserializer=chain__query_dot_query__pb2.ListUnspentResponse.FromString,
        )
    self.ListTransaction = channel.unary_unary(
        '/chainquery.api.ChainQueryService/ListTransaction',
        request_serializer=chain__query_dot_query__pb2.ListTransactionRequest.SerializeToString,
        response_deserializer=chain__query_dot_query__pb2.ListTransactionResponse.FromString,
        )
    self.QueryTransaction = channel.unary_unary(
        '/chainquery.api.ChainQueryService/QueryTransaction',
        request_serializer=chain__query_dot_query__pb2.QueryTransactionRequest.SerializeToString,
        response_deserializer=chain__query_dot_query__pb2.QueryTransactionResponse.FromString,
        )
    self.GetTokensBalance = channel.unary_unary(
        '/chainquery.api.ChainQueryService/GetTokensBalance',
        request_serializer=chain__query_dot_query__pb2.GetTokensBalanceRequest.SerializeToString,
        response_deserializer=chain__query_dot_query__pb2.GetTokensBalanceResponse.FromString,
        )


class ChainQueryServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetBalance(self, request, context):
    """获取钱包余额
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUnspent(self, request, context):
    """获取钱包全部未花费的UTXO
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTransaction(self, request, context):
    """获取钱包全部的交易
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryTransaction(self, request, context):
    """查询交易
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokensBalance(self, request, context):
    """查询钱包拥有的代币种类及数量
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChainQueryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetBalance,
          request_deserializer=chain__query_dot_query__pb2.GetBalanceRequest.FromString,
          response_serializer=chain__query_dot_query__pb2.GetBalanceResponse.SerializeToString,
      ),
      'ListUnspent': grpc.unary_unary_rpc_method_handler(
          servicer.ListUnspent,
          request_deserializer=chain__query_dot_query__pb2.ListUnspentRequest.FromString,
          response_serializer=chain__query_dot_query__pb2.ListUnspentResponse.SerializeToString,
      ),
      'ListTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.ListTransaction,
          request_deserializer=chain__query_dot_query__pb2.ListTransactionRequest.FromString,
          response_serializer=chain__query_dot_query__pb2.ListTransactionResponse.SerializeToString,
      ),
      'QueryTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.QueryTransaction,
          request_deserializer=chain__query_dot_query__pb2.QueryTransactionRequest.FromString,
          response_serializer=chain__query_dot_query__pb2.QueryTransactionResponse.SerializeToString,
      ),
      'GetTokensBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokensBalance,
          request_deserializer=chain__query_dot_query__pb2.GetTokensBalanceRequest.FromString,
          response_serializer=chain__query_dot_query__pb2.GetTokensBalanceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chainquery.api.ChainQueryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
