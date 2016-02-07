FROM python:3.5

ENV HOME /root

# Install dependencies
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y build-essential
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y cmake
RUN apt-get install -y python-matplotlib
RUN apt-get install -y python-scipy
RUN apt-get install -y subversion

# Install Python packages
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install bottleneck
RUN pip install boto3
#RUN pip install -U scikit-image

# Build OpenCV and dependencies
RUN cd && wget https://github.com/Itseez/opencv/archive/3.0.0.zip \
  && git clone https://github.com/Itseez/opencv_contrib.git \
	&& unzip 3.0.0.zip \
	&& cd opencv-3.0.0 && mkdir build && cd build \
	&& cmake -DOPENCV_EXTRA_MODULES_PATH=../../modules -DBUILD_opencv_legacy=OFF .. \
  && make -j2 && make install \
	&& cd && rm -rf opencv-3.0.0 && rm 3.0.0.zip

# Build HDF5
RUN cd ; wget https://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.16.tar.gz
RUN cd ; tar zxf hdf5-1.8.16.tar.gz
RUN cd ; mv hdf5-1.8.16 hdf5-setup
RUN cd ; cd hdf5-setup ; ./configure --prefix=/usr/local/
RUN cd ; cd hdf5-setup ; make && make install

# Cleanup
RUN cd ; rm -rf hdf5-setup
RUN apt-get -yq autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python packages with dependencies on HDF5
RUN pip install tables
RUN pip install h5py

# Update environment and directories
ENV PYTHONUNBUFFERED 1
ENV HDF5_DIR /usr/bin/ld
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 5000
