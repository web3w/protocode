# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chain-contract/nuls-contract.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chain-contract/nuls-contract.proto',
  package='contract.api',
  syntax='proto3',
  serialized_pb=_b('\n\"chain-contract/nuls-contract.proto\x12\x0c\x63ontract.api\x1a\x13shared/status.proto\"\xb1\x01\n\x13NulsInvokeExtension\x12\x0f\n\x07\x63hainId\x18\x01 \x01(\x05\x12\x15\n\rsenderBalance\x18\x02 \x01(\t\x12\r\n\x05nonce\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x12\x10\n\x08gasLimit\x18\x05 \x01(\t\x12\x12\n\nmethodDesc\x18\x06 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x07 \x03(\t\x12\x10\n\x08\x61rgsType\x18\x08 \x03(\t\x12\x0e\n\x06remark\x18\t \x01(\t\"\xa6\x01\n\x0fNulsInvokeParam\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.shared.api.InvokeType\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x19\n\x11signedTransaction\x18\x04 \x01(\t\x12\x34\n\textension\x18\x05 \x01(\x0b\x32!.contract.api.NulsInvokeExtension\"<\n\x10NulsInvokeResult\x12\x1a\n\x12\x65ncodedTransaction\x18\x01 \x03(\t\x12\x0c\n\x04txId\x18\x02 \x01(\tBu\n\x1c\x63om.bibox.dex.proto.contractB\x11NulsContractProtoZBgit.bibox.com/big4/protocode.git/chain-contract-go;pbchaincontractb\x06proto3')
  ,
  dependencies=[shared_dot_status__pb2.DESCRIPTOR,])




_NULSINVOKEEXTENSION = _descriptor.Descriptor(
  name='NulsInvokeExtension',
  full_name='contract.api.NulsInvokeExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chainId', full_name='contract.api.NulsInvokeExtension.chainId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='senderBalance', full_name='contract.api.NulsInvokeExtension.senderBalance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='contract.api.NulsInvokeExtension.nonce', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='contract.api.NulsInvokeExtension.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gasLimit', full_name='contract.api.NulsInvokeExtension.gasLimit', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methodDesc', full_name='contract.api.NulsInvokeExtension.methodDesc', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='contract.api.NulsInvokeExtension.args', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='argsType', full_name='contract.api.NulsInvokeExtension.argsType', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='contract.api.NulsInvokeExtension.remark', index=8,
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
  serialized_start=74,
  serialized_end=251,
)


_NULSINVOKEPARAM = _descriptor.Descriptor(
  name='NulsInvokeParam',
  full_name='contract.api.NulsInvokeParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='contract.api.NulsInvokeParam.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='contract.api.NulsInvokeParam.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='contract.api.NulsInvokeParam.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signedTransaction', full_name='contract.api.NulsInvokeParam.signedTransaction', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='contract.api.NulsInvokeParam.extension', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=254,
  serialized_end=420,
)


_NULSINVOKERESULT = _descriptor.Descriptor(
  name='NulsInvokeResult',
  full_name='contract.api.NulsInvokeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encodedTransaction', full_name='contract.api.NulsInvokeResult.encodedTransaction', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txId', full_name='contract.api.NulsInvokeResult.txId', index=1,
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
  serialized_start=422,
  serialized_end=482,
)

_NULSINVOKEPARAM.fields_by_name['type'].enum_type = shared_dot_status__pb2._INVOKETYPE
_NULSINVOKEPARAM.fields_by_name['extension'].message_type = _NULSINVOKEEXTENSION
DESCRIPTOR.message_types_by_name['NulsInvokeExtension'] = _NULSINVOKEEXTENSION
DESCRIPTOR.message_types_by_name['NulsInvokeParam'] = _NULSINVOKEPARAM
DESCRIPTOR.message_types_by_name['NulsInvokeResult'] = _NULSINVOKERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NulsInvokeExtension = _reflection.GeneratedProtocolMessageType('NulsInvokeExtension', (_message.Message,), dict(
  DESCRIPTOR = _NULSINVOKEEXTENSION,
  __module__ = 'chain_contract.nuls_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NulsInvokeExtension)
  ))
_sym_db.RegisterMessage(NulsInvokeExtension)

NulsInvokeParam = _reflection.GeneratedProtocolMessageType('NulsInvokeParam', (_message.Message,), dict(
  DESCRIPTOR = _NULSINVOKEPARAM,
  __module__ = 'chain_contract.nuls_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NulsInvokeParam)
  ))
_sym_db.RegisterMessage(NulsInvokeParam)

NulsInvokeResult = _reflection.GeneratedProtocolMessageType('NulsInvokeResult', (_message.Message,), dict(
  DESCRIPTOR = _NULSINVOKERESULT,
  __module__ = 'chain_contract.nuls_contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.api.NulsInvokeResult)
  ))
_sym_db.RegisterMessage(NulsInvokeResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.bibox.dex.proto.contractB\021NulsContractProtoZBgit.bibox.com/big4/protocode.git/chain-contract-go;pbchaincontract'))
# @@protoc_insertion_point(module_scope)