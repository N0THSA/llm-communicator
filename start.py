from time import sleep
from colorama import Fore as col 
import sys, os, datetime
from common import GptParams
from low_level_api_chat_cpp import LLaMAInteract
import time
import random
from datetime import datetime
currentdate = datetime.today().strftime('%m-%d-%Y')
print("https://github.com/N0THSA/llm-communicator/")
print(f"\nYou can modify the configuration inside this file...")
sleep(2)
# Functions
def clear(num_times):
    for i in range(num_times):
        print("")
def env_or_def(env, default):
  if (env in os.environ):
    return os.environ[env]
  return default

print(f"{col.RESET}USER NAME?")
USER_NAME = input(f"> {col.RESET}")
clear(500)

###################################################
#                  EDIT BELOW!                    #
###################################################

# It is worth noting this program is only made for "chat mode".

MODELF = "/models/llama2-13b.bin" # path to model
THREADS = 4 # default: 4
maxtokensf = 2048 # maxiumum token output. WARNING: if hit, you need to restart the chat. most models support up to 2048 tokens.
ASSISTANT_NAME = "Eddie" # default: Eddie

##########################
##### SYSTEM MESSAGE #####
##########################
prompt = f"""{ASSISTANT_NAME} is an intelligent virtual artificial intelligence assistant with no bias, personal opinions, or beliefs.
{ASSISTANT_NAME} cannot access real-time information, or any information past September 2nd, 2022.
{ASSISTANT_NAME} always types professionally but directly.
The current date is {currentdate}, and the time is unknown.

{USER_NAME}:""" + " ".join(sys.argv[1:])

##### GPTPARAMS VALUES #####

temp0 = 0.95 # recommended between 0.01 and 1.0. the lower, the less creative. for example, if you were using a programming model you should set it low. if you were writing something like a story, you should set it high.
contextwindow = 2048 # most models support up to 2048, but some can support much more. (check model description)

###################################################
#                 STOP EDITING!                   #
###################################################

MODEL = env_or_def("MODEL", MODELF)

N_PREDICTS = int(env_or_def("N_PREDICTS", maxtokensf))
N_THREAD = int(env_or_def("N_THREAD", THREADS))

def generate_new_seed():
    current_time = int(time.time())  # Get the current time as an integer timestamp
    random_seed = random.randint(1, current_time)  # Generate a random seed based on the current time
    return random_seed


params = GptParams(
  n_ctx=contextwindow,
  temp=temp0,
  top_k=40,
  top_p=1,
  repeat_last_n=64,
  n_batch=1024,
  repeat_penalty=1.17647,
  model=MODEL,
  n_threads=N_THREAD,
  n_predict=N_PREDICTS,
  use_color=True,
  interactive=True,
  antiprompt=[f"{USER_NAME}:"],
  input_prefix=" ",
  input_suffix=f"{ASSISTANT_NAME}" + ":",
  prompt=prompt,
  seed=generate_new_seed()
)
sleep(2)


with LLaMAInteract(params) as m:
  print(col.RESET)
  m.interact()
