mkdir -p data/fashion

echo "Downloading Fashion MNIST data"

wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/t10k-images-idx3-ubyte.gz -O data/fashion/t10k-images-idx3-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/t10k-labels-idx1-ubyte.gz -O data/fashion/t10k-labels-idx1-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/train-images-idx3-ubyte.gz -O data/fashion/train-images-idx3-ubyte.gz
wget https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/train-labels-idx1-ubyte.gz -O data/fashion/train-labels-idx1-ubyte.gz

echo "Finished downloading"
