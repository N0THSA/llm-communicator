# llm-communicator
Better version of the LLM Model TUI. Yes, it got so bad I had to just rewrite it under a whole seperate name.
Lots of code borrowed from [this repository.](https://github.com/abetlen/llama-cpp-python/tree/main/examples)

# Guide
Basic guide for usage.
## Downloading the program
Run the following commands:

<code>$ git clone https://github.com/N0THSA/llm-communicator.git && cd llm-communicator
$ python3 check_dependencies.py (or check_dependencies_windows.py if you're on windows)
$ python3 start.py</code>

## Installing models
1. Make a folder at the root of your harddrive and name it "models".
2. Go to https://huggingface.co/ and look for GGML models by "TheBloke" (https://huggingface.co/TheBloke) You can also look for GGML models from elsewhere, but TheBloke is usually the easiest choice. Typically, the more parameters (3b, 7b, 13b etc) the higher the file size and the higher the system requirements. Anything above 13b is discouraged.
   
3. On the model page, there will be multiple files typically ranging from 2_K to 8_0. Only get one. The lower the value, the less stable. The higher the value, the more stable. However, the higher the longer it takes to generate. It's also worth noting this will affect performance. Typically, 4_0 to 4_1 is a good stable range.
4. Place the model you download inside the "models" folder you created earlier at the root of your harddrive. Name it something simple.
5. Launch the program and go through the wizard, specifying the model to use.

It is worth noting that anything above 13b will be basically impossible to run under 32gb of ram, and 13b 8_0 usually needs more than 16gb of ram as well.

## Running the program
1. Run the following command:
   <code>python3 start.py</code>
   
2. Follow the guide and fill in all applicable forms. Some are optional, such as information about you.
3. Set the model path to the place you downloaded your GGML model.
4. Enjoy!
