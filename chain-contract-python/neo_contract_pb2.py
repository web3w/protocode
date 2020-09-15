# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chain-contract/neo-contract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from shared import token_pb2 as shared_dot_token__pb2
from shared import status_pb2 as shared_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chain-contract/neo-contract.proto',
  package='contract.api',
  syntax='proto3',
  serialized_pb=_b('\n!chain-contract/neo-contract.proto\x12\x0c\x63ontract.api\x1a\x12shared/token.proto\x1a\x13shared/status.proto\"<\n\x08NeoAsset\x12 \n\x05token\x18\x01 \x01(\x0b\x32\x11.shared.api.Token\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\"9\n\x0bNeoAttrbute\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05usage\x18\x03 \x01(\t\"+\n\x0cNeoInvokeArg\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xb5\x02\n\x0eNeoInvokeParam\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.shared.api.InvokeType\x12(\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x1a.contract.api.NeoInvokeArg\x12.\n\x0e\x61ttachedAssets\x18\x03 \x03(\x0b\x32\x16.contract.api.NeoAsset\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\x01\x12-\n\nattributes\x18\x05 \x03(\x0b\x32\x19.contract.api.NeoAttrbute\x12\x0e\n\x06seq_id\x18\x06 \x01(\t\x12\x1a\n\x12signed_transaction\x18\x07 \x03(\t\x12\x12\n\npublic_key\x18\x08 \x01(\t\x12\x14\n\x0cspendAddress\x18\t \x01(\t\x12\x11\n\ttoAddress\x18\n \x01(\t\"\xac\x01\n\x0fNeoInvokeResult\x12\x0e\n\x06script\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x14\n\x0cgas_consumed\x18\x03 \x01(\t\x12)\n\x05stack\x18\x04 \x03(\x0b\x32\x1a.contract.api.NeoInvokeArg\x12\x0e\n\x06seq_id\x18\x05 \x01(\t\x12\x1b\n\x13\x65ncoded_transaction\x18\x06 \x03(\t\x12\x0c\n\x04txid\x18\x07 \x01(\tBt\n\x1c\x63om.bibox.dex.proto.contractB\x10NeoContractProtoZBgit.bibox.com/big4/protocode.git/chain-contract-go;pbchaincontractb\x06proto3')
  ,
  dependencies=[shared_dot_token__pb2.DESCRIPTOR,shared_dot_status__pb2.DESCRIPTOR,])




_NEOASSET = _descriptor.Descriptor(
  name='NeoAsset',
  full_name='contract.api.NeoAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='contract.api.NeoAsset.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='contract.api.NeoAsset.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=92,
  serialized_end=152,
)


_NEOATTRBUTE = _descriptor.Descriptor(
  name='NeoAttrbute',
  full_name='contract.api.NeoAttrbute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='contract.api.NeoAttrbute.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='contract.api.NeoAttrbute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usage', full_name='contract.api.NeoAttrbute.usage', index=2,
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
  serialized_start=154,
  serialized_end=211,
)


_NEOINVOKEARG = _descriptor.Descriptor(
  name='NeoInvokeArg',
  full_name='contract.api.NeoInvokeArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='contract.api.NeoInvokeArg.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='contract.api.NeoInvokeArg.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=213,
  serialized_end=256,
)


_NEOINVOKEPARAM = _descriptor.Descriptor(
  name='NeoInvokeParam',
  full_name='contract.api.NeoInvokeParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='contract.api.NeoInvokeParam.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='contract.api.NeoInvokeParam.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attachedAssets', full_name='contract.api.NeoInvokeParam.attachedAssets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='contract.api.NeoInvokeParam.fee', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='contract.api.NeoInvokeParam.attributes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='contract.api.NeoInvokeParam.seq_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_transaction', full_name='contract.api.NeoInvokeParam.signed_transaction', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='contract.api.NeoInvokeParam.public_key', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spendAddress', full_name='contract.api.NeoInvokeParam.spendAddress', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toAddress', full_name='contract.api.NeoInvokeParam.toAddress', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=259,
  serialized_end=568,
)


_NEOINVOKERESULT = _descriptor.Descriptor(
  name='NeoInvokeResult',
  full_name='contract.api.NeoInvokeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='contract.api.NeoInvokeResult.script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='contract.api.NeoInvokeResult.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_consumed', full_name='contract.api.NeoInvokeResult.gas_consumed', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack', full_name='contract.api.NeoInvokeResult.stack', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='contract.api.NeoInvokeResult.seq_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_transaction', full_name='contract.api.NeoInvokeResult.encoded_transaction', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txid', full_name='contract.api.NeoInvokeResult.txid', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=571,
  serialized_end=743,
)

_NEOASSET.fields_by_name['token'].message_type = shared_dot_token__pb2._TOKEN
_NEOINVOKEPARAM.fields_by_name['type'].enum_type = shared_dot_status__pb2._INVOKETYPE
_NEOINVOKEPARAM.fields_by_name['args'].message_type = _NEOINVOKEARG
_NEOINVOKEPARAM.fields_by_name['attachedAssets'].message_type = _NEOASSET
_NEOINVOKEPARAM.fields_by_name['attributes'].message_type = _NEOATTRBUTE
_NEOINVOKERESULT.fields_by_name['stack'].message_type = _NEOINVOKEARG
DESCRIPTOR.message_types_by_name['NeoAsset'] = _NEOASSET
DESCRIPTOR.message_types_by_name['NeoAttrbute'] = _NEOATTRBUTE
DESCRIPTOR.message_types_by_name['NeoInvokeArg'] = _NEOINVOKEARG
DESCRIPTOR.message_types_by_name['NeoInvokeParam'] = _NEOINVOKEPARAM
DESCRIPTOR.message_types_by_name['NeoInvokeResult'] = _NEOINVOKERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NeoAsset = _reflection.GeneratedProtocolMessageType('NeoAsset', (_message.Message,), dict(
  DESCRIPTOR = _NEOASSET,
  __module__ = 'chain_contract.neo_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NeoAsset)
  ))
_sym_db.RegisterMessage(NeoAsset)

NeoAttrbute = _reflection.GeneratedProtocolMessageType('NeoAttrbute', (_message.Message,), dict(
  DESCRIPTOR = _NEOATTRBUTE,
  __module__ = 'chain_contract.neo_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NeoAttrbute)
  ))
_sym_db.RegisterMessage(NeoAttrbute)

NeoInvokeArg = _reflection.GeneratedProtocolMessageType('NeoInvokeArg', (_message.Message,), dict(
  DESCRIPTOR = _NEOINVOKEARG,
  __module__ = 'chain_contract.neo_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NeoInvokeArg)
  ))
_sym_db.RegisterMessage(NeoInvokeArg)

NeoInvokeParam = _reflection.GeneratedProtocolMessageType('NeoInvokeParam', (_message.Message,), dict(
  DESCRIPTOR = _NEOINVOKEPARAM,
  __module__ = 'chain_contract.neo_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NeoInvokeParam)
  ))
_sym_db.RegisterMessage(NeoInvokeParam)

NeoInvokeResult = _reflection.GeneratedProtocolMessageType('NeoInvokeResult', (_message.Message,), dict(
  DESCRIPTOR = _NEOINVOKERESULT,
  __module__ = 'chain_contract.neo_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NeoInvokeResult)
  ))
_sym_db.RegisterMessage(NeoInvokeResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.bibox.dex.proto.contractB\020NeoContractProtoZBgit.bibox.com/big4/protocode.git/chain-contract-go;pbchaincontract'))
# @@protoc_insertion_point(module_scope)
