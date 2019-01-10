#!/bin/bash

set -e

mkdir -p data/fashion

echo "Downloading Fashion MNIST data"

wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/t10k-images-idx3-ubyte.gz -O data/fashion/t10k-images-idx3-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/t10k-labels-idx1-ubyte.gz -O data/fashion/t10k-labels-idx1-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/train-images-idx3-ubyte.gz -O data/fashion/train-images-idx3-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/train-labels-idx1-ubyte.gz -O data/fashion/train-labels-idx1-ubyte.gz

echo "Finished downloading"

echo "Validating checksums"
echo '8d4fb7e6c68d591d4c3dfef9ec88bf0d data/fashion/train-images-idx3-ubyte.gz' | md5sum -c
echo '25c81989df183df01b3e8a0aad5dffbe data/fashion/train-labels-idx1-ubyte.gz' | md5sum -c
echo 'bef4ecab320f06d8554ea6380940ec79 data/fashion/t10k-images-idx3-ubyte.gz' | md5sum -c
echo 'bb300cfdad3c16e7a12a480ee83cd310 data/fashion/t10k-labels-idx1-ubyte.gz' | md5sum -c
echo "Validation completed: No errors"

echo "Unzipping data"
# gzip -dv data/fashion/*.gz
echo "Finished unzipping"
