# DataRoamers
 
## Install Pre-requirements

1. Ubuntu Linux Installed
2. Run apt-get update, and apt-get upgrade.
3. Installed the following:
sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

4. Created virtual environment:
sudo apt-get install python3-venv
mkdir kivyenv
cd kivyenv
python3 -m venv env
source env/bin/activate

5. Installed Cython and Wheels
pip install Cython==0.23
pip install wheel

6. Installed Kivy
pip install kivy==1.91

## NO2 Analysis:
 Requirements: Python3, Numpy, Matplotlib, BaseMap,NetCD4 <br/>
 Data Source: NO2 data is extracted from the Level 2 Sentinel 5P data accessed from https://s5phub.copernicus.eu/dhus/

