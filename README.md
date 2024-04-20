# Text Condensation using Transformers Hugging Face API

This project focuses on Text Condensation giving a summary of the entire conversation in this case dialogues, future integration may include Machine Learning Operations (MLOps) practices and Data Version Control (DVC) for efficient project management and versioning. The core of the solution is built around the [Transformers](https://jalammar.github.io/illustrated-transformer/). Pytorch library with [Transformers Hugging Face API with Google model](google/pegasus-cnn_dailymail) is used for efficient model training. It is trained on both C4 and HugeNews and is trained for 1.5M to observe slower convergence on pretraining complexity. [Dataset source](https://huggingface.co/datasets/samsum). 


## How to run?

### Clone the repository

    ```
    git clone https://github.com/Shreyansh-1998/TextCondenserAI.git
    ```
### Create a conda environment
    ```
    conda create -n your_env_name -python=3.8 -y
    ```
    ```
    conda activate your_env_name
    ```
### Install the requirements
    ```
    pip install -r requirements.txt
    ```
### Run the main file

    ```
    python main.py
    ```