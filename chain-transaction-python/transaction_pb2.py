# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chain-transaction/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from shared import status_pb2 as shared_dot_status__pb2
from shared import token_pb2 as shared_dot_token__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chain-transaction/transaction.proto',
  package='transaction.api',
  syntax='proto3',
  serialized_pb=_b('\n#chain-transaction/transaction.proto\x12\x0ftransaction.api\x1a\x13shared/status.proto\x1a\x12shared/token.proto\";\n\x07\x46\x65\x65Rate\x12\x12\n\nunit_price\x18\x01 \x01(\x01\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\r\n\x05price\x18\x03 \x01(\x01\"\xbe\x01\n\x1aQueryTransactionFeeRequest\x12 \n\x05token\x18\x01 \x01(\x0b\x32\x11.shared.api.Token\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x0f\n\x07to_addr\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\x12\x1a\n\x12\x61mount_include_fee\x18\x05 \x01(\x08\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12%\n\x1dignore_insuffient_funds_chain\x18\x07 \x01(\x08\"\xd9\x02\n\x1bQueryTransactionFeeResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.shared.api.Status\x12 \n\x05token\x18\x02 \x01(\x0b\x32\x11.shared.api.Token\x12/\n\rfast_fee_rate\x18\x03 \x01(\x0b\x32\x18.transaction.api.FeeRate\x12\x31\n\x0fmiddle_fee_rate\x18\x04 \x01(\x0b\x32\x18.transaction.api.FeeRate\x12/\n\rslow_fee_rate\x18\x05 \x01(\x0b\x32\x18.transaction.api.FeeRate\x12$\n\tfee_token\x18\x06 \x01(\x0b\x32\x11.shared.api.Token\x12\x1c\n\x14\x61vailable_fee_amount\x18\x07 \x01(\x01\x12\x1b\n\x13is_insuffient_funds\x18\x08 \x01(\x08\"\xb8\x01\n\x18\x43reateTransactionRequest\x12 \n\x05token\x18\x01 \x01(\x0b\x32\x11.shared.api.Token\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t\x12\x0f\n\x07to_addr\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x01\x12\x16\n\x0e\x66\x65\x65_unit_price\x18\x07 \x01(\x01\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x11\n\textension\x18\t \x01(\t\"\x9b\x01\n\x19\x43reateTransactionResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.shared.api.Status\x12 \n\x05token\x18\x02 \x01(\x0b\x32\x11.shared.api.Token\x12\x0e\n\x06seq_id\x18\x03 \x01(\t\x12\x1b\n\x13\x65ncoded_transaction\x18\x04 \x03(\t\x12\x0b\n\x03\x66\x65\x65\x18\x05 \x01(\x01\"\x8c\x01\n\x1b\x42roadcastTransactionRequest\x12 \n\x05token\x18\x01 \x01(\x0b\x32\x11.shared.api.Token\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x0e\n\x06seq_id\x18\x03 \x01(\t\x12\x1a\n\x12signed_transaction\x18\x04 \x03(\t\x12\x11\n\textension\x18\x05 \x01(\t\"s\n\x1c\x42roadcastTransactionResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.shared.api.Status\x12 \n\x05token\x18\x02 \x01(\x0b\x32\x11.shared.api.Token\x12\r\n\x05tx_id\x18\x03 \x01(\t\"\x82\x01\n\x15\x43reateInvokeTxRequest\x12$\n\x05\x63hain\x18\x01 \x01(\x0e\x32\x15.shared.api.ChainType\x12\x15\n\rcontract_addr\x18\x02 \x01(\t\x12\x0f\n\x07op_name\x18\x03 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x04 \x01(\t\x12\r\n\x05param\x18\x05 \x01(\t\"i\n\x16\x43reateInvokeTxResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.shared.api.Status\x12\x0e\n\x06seq_id\x18\x03 \x01(\t\x12\x1b\n\x13\x65ncoded_transaction\x18\x04 \x03(\t2\xdb\x03\n\x12TransactionService\x12r\n\x13QueryTransactionFee\x12+.transaction.api.QueryTransactionFeeRequest\x1a,.transaction.api.QueryTransactionFeeResponse\"\x00\x12l\n\x11\x43reateTransaction\x12).transaction.api.CreateTransactionRequest\x1a*.transaction.api.CreateTransactionResponse\"\x00\x12l\n\x17\x43reateInvokeTransaction\x12&.transaction.api.CreateInvokeTxRequest\x1a\'.transaction.api.CreateInvokeTxResponse\"\x00\x12u\n\x14\x42roadcastTransaction\x12,.transaction.api.BroadcastTransactionRequest\x1a-.transaction.api.BroadcastTransactionResponse\"\x00\x42}\n\x1f\x63om.bibox.dex.proto.transactionB\x10TransactionProtoZHgit.bibox.com/big4/protocode.git/chain-transaction-go;pbchaintransactionb\x06proto3')
  ,
  dependencies=[shared_dot_status__pb2.DESCRIPTOR,shared_dot_token__pb2.DESCRIPTOR,])




_FEERATE = _descriptor.Descriptor(
  name='FeeRate',
  full_name='transaction.api.FeeRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_price', full_name='transaction.api.FeeRate.unit_price', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='transaction.api.FeeRate.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='transaction.api.FeeRate.price', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=156,
)


_QUERYTRANSACTIONFEEREQUEST = _descriptor.Descriptor(
  name='QueryTransactionFeeRequest',
  full_name='transaction.api.QueryTransactionFeeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.QueryTransactionFeeRequest.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='transaction.api.QueryTransactionFeeRequest.addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_addr', full_name='transaction.api.QueryTransactionFeeRequest.to_addr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.api.QueryTransactionFeeRequest.amount', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_include_fee', full_name='transaction.api.QueryTransactionFeeRequest.amount_include_fee', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='transaction.api.QueryTransactionFeeRequest.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignore_insuffient_funds_chain', full_name='transaction.api.QueryTransactionFeeRequest.ignore_insuffient_funds_chain', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=349,
)


_QUERYTRANSACTIONFEERESPONSE = _descriptor.Descriptor(
  name='QueryTransactionFeeResponse',
  full_name='transaction.api.QueryTransactionFeeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='transaction.api.QueryTransactionFeeResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.QueryTransactionFeeResponse.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fast_fee_rate', full_name='transaction.api.QueryTransactionFeeResponse.fast_fee_rate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='middle_fee_rate', full_name='transaction.api.QueryTransactionFeeResponse.middle_fee_rate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slow_fee_rate', full_name='transaction.api.QueryTransactionFeeResponse.slow_fee_rate', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_token', full_name='transaction.api.QueryTransactionFeeResponse.fee_token', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_fee_amount', full_name='transaction.api.QueryTransactionFeeResponse.available_fee_amount', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_insuffient_funds', full_name='transaction.api.QueryTransactionFeeResponse.is_insuffient_funds', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=697,
)


_CREATETRANSACTIONREQUEST = _descriptor.Descriptor(
  name='CreateTransactionRequest',
  full_name='transaction.api.CreateTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.CreateTransactionRequest.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='transaction.api.CreateTransactionRequest.addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='transaction.api.CreateTransactionRequest.public_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_addr', full_name='transaction.api.CreateTransactionRequest.to_addr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.api.CreateTransactionRequest.amount', index=4,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_unit_price', full_name='transaction.api.CreateTransactionRequest.fee_unit_price', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='transaction.api.CreateTransactionRequest.memo', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='transaction.api.CreateTransactionRequest.extension', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=884,
)


_CREATETRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='CreateTransactionResponse',
  full_name='transaction.api.CreateTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='transaction.api.CreateTransactionResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.CreateTransactionResponse.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='transaction.api.CreateTransactionResponse.seq_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_transaction', full_name='transaction.api.CreateTransactionResponse.encoded_transaction', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='transaction.api.CreateTransactionResponse.fee', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=1042,
)


_BROADCASTTRANSACTIONREQUEST = _descriptor.Descriptor(
  name='BroadcastTransactionRequest',
  full_name='transaction.api.BroadcastTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.BroadcastTransactionRequest.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='transaction.api.BroadcastTransactionRequest.addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='transaction.api.BroadcastTransactionRequest.seq_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_transaction', full_name='transaction.api.BroadcastTransactionRequest.signed_transaction', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='transaction.api.BroadcastTransactionRequest.extension', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1045,
  serialized_end=1185,
)


_BROADCASTTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='BroadcastTransactionResponse',
  full_name='transaction.api.BroadcastTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='transaction.api.BroadcastTransactionResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='transaction.api.BroadcastTransactionResponse.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='transaction.api.BroadcastTransactionResponse.tx_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1187,
  serialized_end=1302,
)


_CREATEINVOKETXREQUEST = _descriptor.Descriptor(
  name='CreateInvokeTxRequest',
  full_name='transaction.api.CreateInvokeTxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain', full_name='transaction.api.CreateInvokeTxRequest.chain', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_addr', full_name='transaction.api.CreateInvokeTxRequest.contract_addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_name', full_name='transaction.api.CreateInvokeTxRequest.op_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='transaction.api.CreateInvokeTxRequest.addr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='transaction.api.CreateInvokeTxRequest.param', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1305,
  serialized_end=1435,
)


_CREATEINVOKETXRESPONSE = _descriptor.Descriptor(
  name='CreateInvokeTxResponse',
  full_name='transaction.api.CreateInvokeTxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='transaction.api.CreateInvokeTxResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='transaction.api.CreateInvokeTxResponse.seq_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_transaction', full_name='transaction.api.CreateInvokeTxResponse.encoded_transaction', index=2,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1437,
  serialized_end=1542,
)

_QUERYTRANSACTIONFEEREQUEST.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['status'].message_type = shared_dot_status__pb2._STATUS
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['fast_fee_rate'].message_type = _FEERATE
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['middle_fee_rate'].message_type = _FEERATE
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['slow_fee_rate'].message_type = _FEERATE
_QUERYTRANSACTIONFEERESPONSE.fields_by_name['fee_token'].message_type = shared_dot_token__pb2._TOKEN
_CREATETRANSACTIONREQUEST.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_CREATETRANSACTIONRESPONSE.fields_by_name['status'].message_type = shared_dot_status__pb2._STATUS
_CREATETRANSACTIONRESPONSE.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_BROADCASTTRANSACTIONREQUEST.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_BROADCASTTRANSACTIONRESPONSE.fields_by_name['status'].message_type = shared_dot_status__pb2._STATUS
_BROADCASTTRANSACTIONRESPONSE.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_CREATEINVOKETXREQUEST.fields_by_name['chain'].enum_type = shared_dot_token__pb2._CHAINTYPE
_CREATEINVOKETXRESPONSE.fields_by_name['status'].message_type = shared_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['FeeRate'] = _FEERATE
DESCRIPTOR.message_types_by_name['QueryTransactionFeeRequest'] = _QUERYTRANSACTIONFEEREQUEST
DESCRIPTOR.message_types_by_name['QueryTransactionFeeResponse'] = _QUERYTRANSACTIONFEERESPONSE
DESCRIPTOR.message_types_by_name['CreateTransactionRequest'] = _CREATETRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['CreateTransactionResponse'] = _CREATETRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['BroadcastTransactionRequest'] = _BROADCASTTRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['BroadcastTransactionResponse'] = _BROADCASTTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateInvokeTxRequest'] = _CREATEINVOKETXREQUEST
DESCRIPTOR.message_types_by_name['CreateInvokeTxResponse'] = _CREATEINVOKETXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeeRate = _reflection.GeneratedProtocolMessageType('FeeRate', (_message.Message,), dict(
  DESCRIPTOR = _FEERATE,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.FeeRate)
  ))
_sym_db.RegisterMessage(FeeRate)

QueryTransactionFeeRequest = _reflection.GeneratedProtocolMessageType('QueryTransactionFeeRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTRANSACTIONFEEREQUEST,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.QueryTransactionFeeRequest)
  ))
_sym_db.RegisterMessage(QueryTransactionFeeRequest)

QueryTransactionFeeResponse = _reflection.GeneratedProtocolMessageType('QueryTransactionFeeResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTRANSACTIONFEERESPONSE,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.QueryTransactionFeeResponse)
  ))
_sym_db.RegisterMessage(QueryTransactionFeeResponse)

CreateTransactionRequest = _reflection.GeneratedProtocolMessageType('CreateTransactionRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATETRANSACTIONREQUEST,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.CreateTransactionRequest)
  ))
_sym_db.RegisterMessage(CreateTransactionRequest)

CreateTransactionResponse = _reflection.GeneratedProtocolMessageType('CreateTransactionResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATETRANSACTIONRESPONSE,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.CreateTransactionResponse)
  ))
_sym_db.RegisterMessage(CreateTransactionResponse)

BroadcastTransactionRequest = _reflection.GeneratedProtocolMessageType('BroadcastTransactionRequest', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTTRANSACTIONREQUEST,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.BroadcastTransactionRequest)
  ))
_sym_db.RegisterMessage(BroadcastTransactionRequest)

BroadcastTransactionResponse = _reflection.GeneratedProtocolMessageType('BroadcastTransactionResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTTRANSACTIONRESPONSE,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.BroadcastTransactionResponse)
  ))
_sym_db.RegisterMessage(BroadcastTransactionResponse)

CreateInvokeTxRequest = _reflection.GeneratedProtocolMessageType('CreateInvokeTxRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINVOKETXREQUEST,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.CreateInvokeTxRequest)
  ))
_sym_db.RegisterMessage(CreateInvokeTxRequest)

CreateInvokeTxResponse = _reflection.GeneratedProtocolMessageType('CreateInvokeTxResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINVOKETXRESPONSE,
  __module__ = 'chain_transaction.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.api.CreateInvokeTxResponse)
  ))
_sym_db.RegisterMessage(CreateInvokeTxResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.bibox.dex.proto.transactionB\020TransactionProtoZHgit.bibox.com/big4/protocode.git/chain-transaction-go;pbchaintransaction'))

_TRANSACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='TransactionService',
  full_name='transaction.api.TransactionService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1545,
  serialized_end=2020,
  methods=[
  _descriptor.MethodDescriptor(
    name='QueryTransactionFee',
    full_name='transaction.api.TransactionService.QueryTransactionFee',
    index=0,
    containing_service=None,
    input_type=_QUERYTRANSACTIONFEEREQUEST,
    output_type=_QUERYTRANSACTIONFEERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTransaction',
    full_name='transaction.api.TransactionService.CreateTransaction',
    index=1,
    containing_service=None,
    input_type=_CREATETRANSACTIONREQUEST,
    output_type=_CREATETRANSACTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateInvokeTransaction',
    full_name='transaction.api.TransactionService.CreateInvokeTransaction',
    index=2,
    containing_service=None,
    input_type=_CREATEINVOKETXREQUEST,
    output_type=_CREATEINVOKETXRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BroadcastTransaction',
    full_name='transaction.api.TransactionService.BroadcastTransaction',
    index=3,
    containing_service=None,
    input_type=_BROADCASTTRANSACTIONREQUEST,
    output_type=_BROADCASTTRANSACTIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTIONSERVICE)

DESCRIPTOR.services_by_name['TransactionService'] = _TRANSACTIONSERVICE

# @@protoc_insertion_point(module_scope)
