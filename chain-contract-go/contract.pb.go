// Code generated by protoc-gen-go. DO NOT EDIT.
// source: chain-contract/contract.proto

package pbchaincontract // import "git.bibox.com/big4/protocode.git/chain-contract-go"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import shared_go "git.bibox.com/big4/protocode.git/shared-go"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type InvokeRequest struct {
	Chain                shared_go.ChainType `protobuf:"varint,1,opt,name=chain,proto3,enum=shared.api.ChainType" json:"chain,omitempty"`
	ContractAddr         string              `protobuf:"bytes,2,opt,name=contract_addr,json=contractAddr,proto3" json:"contract_addr,omitempty"`
	OpName               string              `protobuf:"bytes,3,opt,name=op_name,json=opName,proto3" json:"op_name,omitempty"`
	Addr                 string              `protobuf:"bytes,4,opt,name=addr,proto3" json:"addr,omitempty"`
	Param                string              `protobuf:"bytes,5,opt,name=param,proto3" json:"param,omitempty"`
	XXX_NoUnkeyedLiteral struct{}            `json:"-"`
	XXX_unrecognized     []byte              `json:"-"`
	XXX_sizecache        int32               `json:"-"`
}

func (m *InvokeRequest) Reset()         { *m = InvokeRequest{} }
func (m *InvokeRequest) String() string { return proto.CompactTextString(m) }
func (*InvokeRequest) ProtoMessage()    {}
func (*InvokeRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{0}
}
func (m *InvokeRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_InvokeRequest.Unmarshal(m, b)
}
func (m *InvokeRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_InvokeRequest.Marshal(b, m, deterministic)
}
func (dst *InvokeRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_InvokeRequest.Merge(dst, src)
}
func (m *InvokeRequest) XXX_Size() int {
	return xxx_messageInfo_InvokeRequest.Size(m)
}
func (m *InvokeRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_InvokeRequest.DiscardUnknown(m)
}

var xxx_messageInfo_InvokeRequest proto.InternalMessageInfo

func (m *InvokeRequest) GetChain() shared_go.ChainType {
	if m != nil {
		return m.Chain
	}
	return shared_go.ChainType_CHAIN_UNKNOWN
}

func (m *InvokeRequest) GetContractAddr() string {
	if m != nil {
		return m.ContractAddr
	}
	return ""
}

func (m *InvokeRequest) GetOpName() string {
	if m != nil {
		return m.OpName
	}
	return ""
}

func (m *InvokeRequest) GetAddr() string {
	if m != nil {
		return m.Addr
	}
	return ""
}

func (m *InvokeRequest) GetParam() string {
	if m != nil {
		return m.Param
	}
	return ""
}

type InvokeResponse struct {
	Status               *shared_go.Status `protobuf:"bytes,1,opt,name=status,proto3" json:"status,omitempty"`
	Result               string            `protobuf:"bytes,2,opt,name=result,proto3" json:"result,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *InvokeResponse) Reset()         { *m = InvokeResponse{} }
func (m *InvokeResponse) String() string { return proto.CompactTextString(m) }
func (*InvokeResponse) ProtoMessage()    {}
func (*InvokeResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{1}
}
func (m *InvokeResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_InvokeResponse.Unmarshal(m, b)
}
func (m *InvokeResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_InvokeResponse.Marshal(b, m, deterministic)
}
func (dst *InvokeResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_InvokeResponse.Merge(dst, src)
}
func (m *InvokeResponse) XXX_Size() int {
	return xxx_messageInfo_InvokeResponse.Size(m)
}
func (m *InvokeResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_InvokeResponse.DiscardUnknown(m)
}

var xxx_messageInfo_InvokeResponse proto.InternalMessageInfo

func (m *InvokeResponse) GetStatus() *shared_go.Status {
	if m != nil {
		return m.Status
	}
	return nil
}

func (m *InvokeResponse) GetResult() string {
	if m != nil {
		return m.Result
	}
	return ""
}

type TransferRequest struct {
	Token                *shared_go.Token `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
	Addr                 string           `protobuf:"bytes,2,opt,name=addr,proto3" json:"addr,omitempty"`
	Toaddr               string           `protobuf:"bytes,3,opt,name=toaddr,proto3" json:"toaddr,omitempty"`
	Amount               float64          `protobuf:"fixed64,4,opt,name=amount,proto3" json:"amount,omitempty"`
	Remark               string           `protobuf:"bytes,5,opt,name=remark,proto3" json:"remark,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *TransferRequest) Reset()         { *m = TransferRequest{} }
func (m *TransferRequest) String() string { return proto.CompactTextString(m) }
func (*TransferRequest) ProtoMessage()    {}
func (*TransferRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{2}
}
func (m *TransferRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TransferRequest.Unmarshal(m, b)
}
func (m *TransferRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TransferRequest.Marshal(b, m, deterministic)
}
func (dst *TransferRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TransferRequest.Merge(dst, src)
}
func (m *TransferRequest) XXX_Size() int {
	return xxx_messageInfo_TransferRequest.Size(m)
}
func (m *TransferRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_TransferRequest.DiscardUnknown(m)
}

var xxx_messageInfo_TransferRequest proto.InternalMessageInfo

func (m *TransferRequest) GetToken() *shared_go.Token {
	if m != nil {
		return m.Token
	}
	return nil
}

func (m *TransferRequest) GetAddr() string {
	if m != nil {
		return m.Addr
	}
	return ""
}

func (m *TransferRequest) GetToaddr() string {
	if m != nil {
		return m.Toaddr
	}
	return ""
}

func (m *TransferRequest) GetAmount() float64 {
	if m != nil {
		return m.Amount
	}
	return 0
}

func (m *TransferRequest) GetRemark() string {
	if m != nil {
		return m.Remark
	}
	return ""
}

type TransferResponse struct {
	Status               *shared_go.Status `protobuf:"bytes,1,opt,name=status,proto3" json:"status,omitempty"`
	Txid                 string            `protobuf:"bytes,2,opt,name=txid,proto3" json:"txid,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *TransferResponse) Reset()         { *m = TransferResponse{} }
func (m *TransferResponse) String() string { return proto.CompactTextString(m) }
func (*TransferResponse) ProtoMessage()    {}
func (*TransferResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{3}
}
func (m *TransferResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TransferResponse.Unmarshal(m, b)
}
func (m *TransferResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TransferResponse.Marshal(b, m, deterministic)
}
func (dst *TransferResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TransferResponse.Merge(dst, src)
}
func (m *TransferResponse) XXX_Size() int {
	return xxx_messageInfo_TransferResponse.Size(m)
}
func (m *TransferResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_TransferResponse.DiscardUnknown(m)
}

var xxx_messageInfo_TransferResponse proto.InternalMessageInfo

func (m *TransferResponse) GetStatus() *shared_go.Status {
	if m != nil {
		return m.Status
	}
	return nil
}

func (m *TransferResponse) GetTxid() string {
	if m != nil {
		return m.Txid
	}
	return ""
}

type GetBalanceRequest struct {
	Token                *shared_go.Token `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
	Addr                 string           `protobuf:"bytes,2,opt,name=addr,proto3" json:"addr,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *GetBalanceRequest) Reset()         { *m = GetBalanceRequest{} }
func (m *GetBalanceRequest) String() string { return proto.CompactTextString(m) }
func (*GetBalanceRequest) ProtoMessage()    {}
func (*GetBalanceRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{4}
}
func (m *GetBalanceRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetBalanceRequest.Unmarshal(m, b)
}
func (m *GetBalanceRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetBalanceRequest.Marshal(b, m, deterministic)
}
func (dst *GetBalanceRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetBalanceRequest.Merge(dst, src)
}
func (m *GetBalanceRequest) XXX_Size() int {
	return xxx_messageInfo_GetBalanceRequest.Size(m)
}
func (m *GetBalanceRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetBalanceRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetBalanceRequest proto.InternalMessageInfo

func (m *GetBalanceRequest) GetToken() *shared_go.Token {
	if m != nil {
		return m.Token
	}
	return nil
}

func (m *GetBalanceRequest) GetAddr() string {
	if m != nil {
		return m.Addr
	}
	return ""
}

type GetBalanceResponse struct {
	Status               *shared_go.Status `protobuf:"bytes,1,opt,name=status,proto3" json:"status,omitempty"`
	Amount               float64           `protobuf:"fixed64,2,opt,name=amount,proto3" json:"amount,omitempty"`
	Extension            string            `protobuf:"bytes,3,opt,name=extension,proto3" json:"extension,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *GetBalanceResponse) Reset()         { *m = GetBalanceResponse{} }
func (m *GetBalanceResponse) String() string { return proto.CompactTextString(m) }
func (*GetBalanceResponse) ProtoMessage()    {}
func (*GetBalanceResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_contract_d3333334553f07df, []int{5}
}
func (m *GetBalanceResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetBalanceResponse.Unmarshal(m, b)
}
func (m *GetBalanceResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetBalanceResponse.Marshal(b, m, deterministic)
}
func (dst *GetBalanceResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetBalanceResponse.Merge(dst, src)
}
func (m *GetBalanceResponse) XXX_Size() int {
	return xxx_messageInfo_GetBalanceResponse.Size(m)
}
func (m *GetBalanceResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetBalanceResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetBalanceResponse proto.InternalMessageInfo

func (m *GetBalanceResponse) GetStatus() *shared_go.Status {
	if m != nil {
		return m.Status
	}
	return nil
}

func (m *GetBalanceResponse) GetAmount() float64 {
	if m != nil {
		return m.Amount
	}
	return 0
}

func (m *GetBalanceResponse) GetExtension() string {
	if m != nil {
		return m.Extension
	}
	return ""
}

func init() {
	proto.RegisterType((*InvokeRequest)(nil), "contract.api.InvokeRequest")
	proto.RegisterType((*InvokeResponse)(nil), "contract.api.InvokeResponse")
	proto.RegisterType((*TransferRequest)(nil), "contract.api.TransferRequest")
	proto.RegisterType((*TransferResponse)(nil), "contract.api.TransferResponse")
	proto.RegisterType((*GetBalanceRequest)(nil), "contract.api.GetBalanceRequest")
	proto.RegisterType((*GetBalanceResponse)(nil), "contract.api.GetBalanceResponse")
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// ChainContractServiceClient is the client API for ChainContractService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type ChainContractServiceClient interface {
	// 通用合约操作
	Invoke(ctx context.Context, in *InvokeRequest, opts ...grpc.CallOption) (*InvokeResponse, error)
	// transfer
	Transfer(ctx context.Context, in *TransferRequest, opts ...grpc.CallOption) (*TransferResponse, error)
	// GetBalance
	GetBalance(ctx context.Context, in *GetBalanceRequest, opts ...grpc.CallOption) (*GetBalanceResponse, error)
}

type chainContractServiceClient struct {
	cc *grpc.ClientConn
}

func NewChainContractServiceClient(cc *grpc.ClientConn) ChainContractServiceClient {
	return &chainContractServiceClient{cc}
}

func (c *chainContractServiceClient) Invoke(ctx context.Context, in *InvokeRequest, opts ...grpc.CallOption) (*InvokeResponse, error) {
	out := new(InvokeResponse)
	err := c.cc.Invoke(ctx, "/contract.api.ChainContractService/Invoke", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *chainContractServiceClient) Transfer(ctx context.Context, in *TransferRequest, opts ...grpc.CallOption) (*TransferResponse, error) {
	out := new(TransferResponse)
	err := c.cc.Invoke(ctx, "/contract.api.ChainContractService/Transfer", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *chainContractServiceClient) GetBalance(ctx context.Context, in *GetBalanceRequest, opts ...grpc.CallOption) (*GetBalanceResponse, error) {
	out := new(GetBalanceResponse)
	err := c.cc.Invoke(ctx, "/contract.api.ChainContractService/GetBalance", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ChainContractServiceServer is the server API for ChainContractService service.
type ChainContractServiceServer interface {
	// 通用合约操作
	Invoke(context.Context, *InvokeRequest) (*InvokeResponse, error)
	// transfer
	Transfer(context.Context, *TransferRequest) (*TransferResponse, error)
	// GetBalance
	GetBalance(context.Context, *GetBalanceRequest) (*GetBalanceResponse, error)
}

func RegisterChainContractServiceServer(s *grpc.Server, srv ChainContractServiceServer) {
	s.RegisterService(&_ChainContractService_serviceDesc, srv)
}

func _ChainContractService_Invoke_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InvokeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ChainContractServiceServer).Invoke(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/contract.api.ChainContractService/Invoke",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ChainContractServiceServer).Invoke(ctx, req.(*InvokeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ChainContractService_Transfer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TransferRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ChainContractServiceServer).Transfer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/contract.api.ChainContractService/Transfer",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ChainContractServiceServer).Transfer(ctx, req.(*TransferRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ChainContractService_GetBalance_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetBalanceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ChainContractServiceServer).GetBalance(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/contract.api.ChainContractService/GetBalance",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ChainContractServiceServer).GetBalance(ctx, req.(*GetBalanceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _ChainContractService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "contract.api.ChainContractService",
	HandlerType: (*ChainContractServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Invoke",
			Handler:    _ChainContractService_Invoke_Handler,
		},
		{
			MethodName: "Transfer",
			Handler:    _ChainContractService_Transfer_Handler,
		},
		{
			MethodName: "GetBalance",
			Handler:    _ChainContractService_GetBalance_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "chain-contract/contract.proto",
}

func init() {
	proto.RegisterFile("chain-contract/contract.proto", fileDescriptor_contract_d3333334553f07df)
}

var fileDescriptor_contract_d3333334553f07df = []byte{
	// 503 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xac, 0x54, 0x4f, 0x6f, 0xd3, 0x4e,
	0x10, 0xfd, 0x39, 0xbf, 0xc4, 0xd0, 0x81, 0x14, 0x3a, 0x94, 0x12, 0x99, 0x14, 0x22, 0x73, 0xa0,
	0x02, 0xd5, 0x96, 0x02, 0x37, 0x4e, 0xa4, 0x42, 0x08, 0x21, 0xa1, 0xe2, 0xe6, 0xc4, 0xa5, 0x5a,
	0xdb, 0x43, 0x6a, 0xa5, 0xde, 0x75, 0xd7, 0x9b, 0x28, 0x7c, 0x11, 0x3e, 0x01, 0x5f, 0x13, 0x09,
	0x79, 0x77, 0xed, 0xd8, 0x40, 0x2f, 0x15, 0xb7, 0x9d, 0x37, 0x7f, 0xfc, 0xde, 0xdb, 0x59, 0xc3,
	0x61, 0x72, 0xc1, 0x32, 0x7e, 0x9c, 0x08, 0xae, 0x24, 0x4b, 0x54, 0x58, 0x1f, 0x82, 0x42, 0x0a,
	0x25, 0xf0, 0x6e, 0x13, 0xb3, 0x22, 0xf3, 0x1e, 0x94, 0x17, 0x4c, 0x52, 0x1a, 0x96, 0x8a, 0xa9,
	0x55, 0x69, 0x4a, 0x3c, 0xb4, 0xa0, 0x12, 0x4b, 0xe2, 0x06, 0xf3, 0x7f, 0x38, 0x30, 0xfc, 0xc0,
	0xd7, 0x62, 0x49, 0x11, 0x5d, 0xad, 0xa8, 0x54, 0xf8, 0x12, 0x06, 0xfa, 0x4b, 0x23, 0x67, 0xe2,
	0x1c, 0xed, 0x4e, 0x1f, 0x06, 0xa6, 0xab, 0x1a, 0x1b, 0x9c, 0x54, 0x89, 0xf9, 0xb7, 0x82, 0x22,
	0x53, 0x83, 0xcf, 0x60, 0x58, 0x7f, 0xf7, 0x9c, 0xa5, 0xa9, 0x1c, 0xf5, 0x26, 0xce, 0xd1, 0x4e,
	0xd4, 0x90, 0x79, 0x9b, 0xa6, 0x12, 0x1f, 0xc1, 0x2d, 0x51, 0x9c, 0x73, 0x96, 0xd3, 0xe8, 0x7f,
	0x9d, 0x76, 0x45, 0xf1, 0x89, 0xe5, 0x84, 0x08, 0x7d, 0xdd, 0xd4, 0xd7, 0xa8, 0x3e, 0xe3, 0x3e,
	0x0c, 0x0a, 0x26, 0x59, 0x3e, 0x1a, 0x68, 0xd0, 0x04, 0xfe, 0x1c, 0x76, 0x6b, 0x96, 0x65, 0x21,
	0x78, 0x49, 0xf8, 0x02, 0x5c, 0x23, 0x4e, 0xf3, 0xbc, 0x33, 0xc5, 0x36, 0xcf, 0x33, 0x9d, 0x89,
	0x6c, 0x05, 0x1e, 0x80, 0x2b, 0xa9, 0x5c, 0x5d, 0x2a, 0x4b, 0xcf, 0x46, 0xfe, 0x77, 0x07, 0xee,
	0xcd, 0x25, 0xe3, 0xe5, 0x57, 0x92, 0xb5, 0xfc, 0xe7, 0x30, 0xd0, 0xfe, 0xd8, 0xb1, 0x7b, 0xed,
	0xb1, 0xf3, 0x2a, 0x11, 0x99, 0x7c, 0x43, 0xbe, 0xd7, 0x22, 0x7f, 0x00, 0xae, 0x12, 0x1a, 0xb5,
	0x42, 0x4d, 0x54, 0xe1, 0x2c, 0x17, 0x2b, 0xae, 0xb4, 0x54, 0x27, 0xb2, 0x91, 0x21, 0x96, 0x33,
	0xb9, 0xb4, 0x6a, 0x6d, 0xe4, 0x47, 0x70, 0x7f, 0xcb, 0xeb, 0x06, 0x82, 0x11, 0xfa, 0x6a, 0x93,
	0xa5, 0x35, 0xb7, 0xea, 0xec, 0x9f, 0xc2, 0xde, 0x7b, 0x52, 0x33, 0x76, 0xc9, 0x78, 0x42, 0xff,
	0x42, 0xad, 0xbf, 0x06, 0x6c, 0x4f, 0xbc, 0xd9, 0xc5, 0x58, 0x5f, 0x7a, 0x1d, 0x5f, 0xc6, 0xb0,
	0x43, 0x1b, 0x45, 0xbc, 0xcc, 0x04, 0xb7, 0x56, 0x6e, 0x81, 0xe9, 0x4f, 0x07, 0xf6, 0xf5, 0x26,
	0x9e, 0xd8, 0x2d, 0x3b, 0x23, 0xb9, 0xce, 0x12, 0xc2, 0x77, 0xe0, 0x9a, 0x2d, 0xc1, 0xc7, 0x41,
	0xfb, 0x39, 0x04, 0x9d, 0x0d, 0xf7, 0xc6, 0x7f, 0x4f, 0x1a, 0xfe, 0xfe, 0x7f, 0xf8, 0x11, 0x6e,
	0xd7, 0xee, 0xe3, 0x61, 0xb7, 0xf6, 0xb7, 0x6d, 0xf1, 0x9e, 0x5c, 0x97, 0x6e, 0x86, 0x7d, 0x06,
	0xd8, 0x9a, 0x84, 0x4f, 0xbb, 0xf5, 0x7f, 0x5c, 0x88, 0x37, 0xb9, 0xbe, 0xa0, 0x1e, 0x39, 0xbb,
	0x82, 0x71, 0x22, 0xf2, 0x20, 0xce, 0x62, 0xb1, 0x09, 0x52, 0xda, 0x98, 0xa7, 0xdc, 0x34, 0xce,
	0x86, 0xb5, 0x2f, 0xa7, 0x15, 0xfe, 0x65, 0xb6, 0xc8, 0x94, 0x2d, 0x4e, 0x44, 0x1e, 0xc6, 0xd9,
	0xe2, 0x75, 0xa8, 0x3b, 0x12, 0x91, 0x52, 0xb0, 0xc8, 0x54, 0xd8, 0xfd, 0xb3, 0x1c, 0x2f, 0xc4,
	0x9b, 0x22, 0xd6, 0x58, 0x0d, 0xc5, 0xae, 0x6e, 0x78, 0xf5, 0x2b, 0x00, 0x00, 0xff, 0xff, 0x32,
	0xc1, 0x06, 0xb9, 0x85, 0x04, 0x00, 0x00,
}