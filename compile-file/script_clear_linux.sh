pip uninstall -y torch torchvision torchaudio tensorflow tensorflow-cpu llama-cpp-python

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip install tensorflow-cpu

CMAKE_ARGS="-DGGML_CUDA=off" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir --no-binary llama-cpp-python

python -c "import torch; print(torch.cuda.is_available()); import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"