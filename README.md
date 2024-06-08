# Natural_Language_Assignment

# Our Project Name `<TBD>`

## Overview

This project is blah...

## Models:

* [https://huggingface.co/KnutJaegersberg/gpt2-chatbot](https://huggingface.co/KnutJaegersberg/gpt2-chatbot)
* [https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
* [https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
* [https://huggingface.co/mosaicml/mpt-7b-instruct](https://huggingface.co/mosaicml/mpt-7b-instruct)
* [https://huggingface.co/mosaicml/mpt-7b-storywriter](https://huggingface.co/mosaicml/mpt-7b-storywriter)
* [https://huggingface.co/Blackroot/Nous-Hermes-Llama2-13b-Storywriter-GPTQ](https://huggingface.co/Blackroot/Nous-Hermes-Llama2-13b-Storywriter-GPTQ)
* [https://huggingface.co/Blackroot/Chronos-Hermes-2-Storywriter](https://huggingface.co/Blackroot/Chronos-Hermes-2-Storywriter)
* [https://huggingface.co/Blackroot/Llama-2-13B-Storywriter-LORA](https://huggingface.co/Blackroot/Llama-2-13B-Storywriter-LORA)

##### How to run the code

1. Install Python. I used version 11.9
2. Create a virtual env: `python3.11 -m venv .venv`
3. In terminal activate the virtual env by following the path to the activate file:
   * Linux: `source .venv/bin/activate`
   * Windows: `.venv\Scripts\activate`
4. In the same terminal run the following command: `pip3 install ipykernel ipywidgets matplotlib accelerate`
5. Follow the steps on the [pytorch](https://pytorch.org/get-started/locally/) website to install additional libraries like torchvision and to use CUDA if available on your device.
6. Run `pip3 install -r requirements.txt` to finish installing any other libraries.
7. Open the GPT2_.ipynb_ jupyter notebook
8. If you are using vscode, click select kernel on the upper right corner, select python environments and then the name of the virtual environment you created which should be .venv
