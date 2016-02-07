# A multi-container `Docker` microservice environment for Python3, OpenCV3 and HDF5

## This microservice environment runs on 2 different `Docker` images both based on `debian:jessie`:
* **`data-only`:** This is a `dockerfile` to build a "data-only" container for persistent storing of data
* **`app`:** This is a `dockerfile` for building the official [Python3](https://github.com/docker-library/python) docker image, [OpenCV](http://opencv.org/),  [HDF5] (https://www.hdfgroup.org/HDF5/) and dependencies, as well as, all the application code

## Build
`docker build --rm -t h5data-only ./data-only`

`docker build --rm -t py-opencv-hdf5 ./app`

## Run

#### Create a `data-only` container called `h5data`:
`docker run -d -t -v /h5data --name h5data h5data-only`

#### Create a `py-opencv-hdf5` container called `app`:
`docker run -d -t --volumes-from h5data --name app py-opencv-hdf5`

## Test

#### Test to make sure that the data is persistent:
* Running `docker exec app ls ../h5data` should show `test1.txt`
* Create a new file in h5data by running `docker exec app touch ../h5data/test2.txt`
* Running `docker exec app ls ../h5data` again should show `test1.txt` and `test2.txt`
* Remove the `app` container: `docker kill app` then `docker rm app`
* Create a new `app2` container: `docker run -d -t --volumes-from h5data --name app2 py-opencv-hdf5`
* Running `docker exec app2 ls ../h5data` again should again show `test1.txt` and `test2.txt`

**Persistent data is working**

#### Further testing with `.h5` files:
* Create a new `app3` container: `docker run -d -t --volumes-from h5data --name app3 py-opencv-hdf5`
* Run `docker exec app3 python hdf5Test.py`
* Kill and remove all `app` containers
* Running `docker exec h5data ls ../h5data` should now show `test1.txt`, `test2.txt`, `pytablesTest.h5` and `h5pyTest.h5`

**Persistent data is working with HDF5**

#### Even further testing with `OpenCV`:
* Create a new `app4` container: `docker run -d -t --volumes-from h5data --name app4 py-opencv-hdf5`
* Run `docker exec app4 python opencvTest.py`
* Kill and remove all `app` containers
* Running `docker exec h5data ls ../h5data` should now show `test1.txt`, `test2.txt`, `pytablesTest.h5`, `h5pyTest.h5` and `opencvTest.h5`

**Everything is completely tested and the Python, OpenCV and HDF5 environment works**
