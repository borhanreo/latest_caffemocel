# CaffeModel

Run caffenet on this data

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