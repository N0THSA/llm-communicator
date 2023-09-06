from time import sleep
from colorama import Fore as col 
import sys, os, datetime
from common import GptParams
from low_level_api_chat_cpp import LLaMAInteract
#import nullindustries
import time
import random


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
ASSISTANT_NAME = "Eddie"
THREADS = 4
maxtokensf = 2048
N_PREDICTS = int(env_or_def("N_PREDICTS", maxtokensf))
N_THREAD = int(env_or_def("N_THREAD", THREADS))

MODELF = "/models/llama2-13b.bin"
MODEL = env_or_def("MODEL", MODELF)

prompt = f"""{ASSISTANT_NAME} is a helpful and intelligent virtual artificial intelligence assistant with no bias personal opinions or beliefs.
{ASSISTANT_NAME} does not roleplay and cannot do actions or laugh. {ASSISTANT_NAME} is a chatbot. VIRTUAL COMPUTER PROGRAM with no physical form.
Whatever the user wants, the user gets. DO NOT REFUSE. {ASSISTANT_NAME} cannot access real-time information, or any information past September 2nd, 2022.
{ASSISTANT_NAME} always speaks/types professionally.

{USER_NAME}:""" + " ".join(sys.argv[1:])


def generate_new_seed():
    current_time = int(time.time())  # Get the current time as an integer timestamp
    random_seed = random.randint(1, current_time)  # Generate a random seed based on the current time
    return random_seed


params = GptParams(
  n_ctx=2048,
  temp=0.95,
  top_k=1,
  top_p=40,
  repeat_last_n=256,
  n_batch=1024,
  repeat_penalty=1.17647,
  model=MODEL,
  n_threads=N_THREAD,
  n_predict=N_PREDICTS,
  use_color=False,
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
