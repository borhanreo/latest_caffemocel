import caffe
import numpy as np
import sys

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( 'dogvscat_mean.binaryproto' , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save( 'dogvscat_mean.npy' , out )
