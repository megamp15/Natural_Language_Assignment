# Natural_Language_Assignment

# **Marathon**/Running **Trainer App Story Generator**

Recently, while looking for a unique training app, we came across an app called **[ZRX: Zombies Run + Marvel Move](https://zrx.app/). **The idea is to run in the real world while making progress through an engaging story. In the zombie story, you can imagine trekking across the land and facing a situation where many zombies are coming after you, prompting you to speed up to a sprint in the real world to reach a safe spot in the story.

Our idea is to use the power of LLMs to create unique stories based on a user’s input, which can dynamically change based on the type and length of the training session specified. We can also do this behind the scenes to generate popular character stories for a future application.

Models tested:

In the models folder, the jupyter notebook filename will have the LLM models name used in that notebook.

The RECURSION script is our idea of having the LLM system understand that it can continue a story even if it has reached the max token limit initially set. This worked quite well!

* [https://huggingface.co/KnutJaegersberg/gpt2-chatbot](https://huggingface.co/KnutJaegersberg/gpt2-chatbot)
* [https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
* [https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
* [https://huggingface.co/mosaicml/mpt-7b-instruct](https://huggingface.co/mosaicml/mpt-7b-instruct)
* [https://huggingface.co/mosaicml/mpt-7b-storywriter](https://huggingface.co/mosaicml/mpt-7b-storywriter)

  Other models not yet tried but looked interesting:
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
7. Open the *models/LLAMA3_RECURSION.ipynb*  jupyter notebook as this holds our best model. Other models can be run in the models folder as well. The code is all the same except that it does not have recursion.
8. If you are using vscode, click select kernel on the upper right corner, select python environments and then the name of the virtual environment you created which should be .venv
9. Change the third cell which holds the messages (instructions) that will be inputted into the LLM.
   * Modify the second json in the messages list with other user prompts. Other examples are held in the *prompts/user_prompts.txt* file.
   * The first json in the messages list is the system prompt which can be seen more clearly in the *prompts/system_prompt.txt* file.
10. If you want to try other genres, the diff_genre_prompts.txt shows a varied number of genres and story descriptions that could be used to generate a full story.
11. The logs folder saves the outputs of the LLM by appending it to the respective file given by the LLM's name.
12. The *final_good_responses* folder has the final 6 stories that we thought did quite well for our idea on two different prompts and 3 different training styles and genres.
