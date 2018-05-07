# CaffeModel

Run caffenet on this data

http://caffe.berkeleyvision.org/gathered/examples/mnist.html

# Setup ProtoBuf

Download Protobuf

    cd /home/mamun/Development/environment
    wget https://github.com/google/protobuf/releases/download/v3.5.1/protobuf-all-3.5.1.tar.gz
    tar -xvf protobuf-all-3.5.1.tar.gz 
    mv protobuf-3.5.1 protobuf
    cd protobuf
    
Install Protobuf

    ./configure
    make
    make check
    sudo make install
    sudo ldconfig # refresh shared library cache
    
For use in python

    cd python
    python setup.py install    
    PROTO_ROOT=/home/mamun/Development/environment/protobuf

# Make Caffe

    cd /home/mamun/Development/environment
    git clone https://github.com/BVLC/caffe
    cp Makefile.config.example Makefile.config
    
**Note**: Adjust Makefile.config (for example, if using Anaconda Python, or if cuDNN is desired)
    
For CPU-only Caffe, uncomment CPU_ONLY := 1 in Makefile.config.
    
    make clean
    make all
    make test
    make runtest
    
To compile the Python and MATLAB wrappers do 

    make pycaffe
    
To MATLAB wrappers do 
    
    make matcaffe

**Note**: Be sure to set your MATLAB and Python paths in Makefile.config first!

Export CaffeRoot

    export CAFFE_ROOT=/home/mamun/Development/environment/caffe

# Export PythonPath

    export PYTHONPATH=$CAFFE_ROOT/python:$PROTO_ROOT/python:$PYTHONPATH