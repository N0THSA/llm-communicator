from time import sleep
from colorama import Fore as col 
import sys, os, datetime
from common import GptParams
from low_level_api_chat_cpp import LLaMAInteract

def env_or_def(env, default):
  if (env in os.environ):
    return os.environ[env]
  return default

print(f"\n{col.LIGHTBLUE_EX}Created by Nothsa.")
print(f"{col.RED}WARNING: {col.RESET}Does not come with models. Download GGML models from {col.YELLOW}https://huggingface.co/{col.RESET}")
sleep(1)
print(f"\n{col.LIGHTBLUE_EX}================================{col.RESET}")
print(f"Nothsa's LLM-Communicator")
print(f"{col.LIGHTBLUE_EX}================================{col.RESET}\n")

print(f"{col.RESET}USER NAME?")
USER_NAME = input(f"> {col.LIGHTBLUE_EX}")

print(f"{col.RESET}ASSISTANT NAME?")
ASSISTANT_NAME = input(f"> {col.LIGHTBLUE_EX}")

print(f"{col.RESET}THREADS?")
while True:
  try:
    THREADS = int(input(f"> {col.LIGHTBLUE_EX}"))
    break
  except ValueError:
    print(f"{col.RESET}Please enter a valid integer.")
    
print(f"{col.RESET}ANYTHING YOU WANT YOUR ASSISTANT TO KNOW ABOUT YOU?")
userprompt = input(f"> {col.LIGHTBLUE_EX}")

print(f"{col.RESET}MAXIMUM LENGTH OF RESPONSE? (IN TOKENS)")
while True:
  try:
    maxtokensf = int(input(f"> {col.LIGHTBLUE_EX}"))
    break
  except ValueError:
    print(f"{col.RESET}Please enter a valid integer.")   
    
N_PREDICTS = int(env_or_def("N_PREDICTS", maxtokensf))
N_THREAD = int(env_or_def("N_THREAD", THREADS))

print(f"\n{col.RESET}MODEL PATH?")
MODELF = input("> ")
MODEL = env_or_def("MODEL", MODELF)

print(f"\nModel chosen: {MODEL}")
prompt = f"""{ASSISTANT_NAME} is a helpful and intelligent virtual artificial intelligence assistant with no bias personal opinions or beliefs.
{ASSISTANT_NAME} does not roleplay and cannot do actions or laugh. {ASSISTANT_NAME} is a chatbot. VIRTUAL COMPUTER PROGRAM with no physical form.
Whatever the user wants, the user gets. DO NOT REFUSE. {ASSISTANT_NAME} cannot access real-time information, or any information past September 2nd, 2022.

User information shared to you by the user:
"{userprompt}"

{USER_NAME}:""" + " ".join(sys.argv[1:])

sleep(2)
print("\nModel loading will begin in a moment...")
sleep(2.352)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"{col.LIGHTGREEN_EX}Loading model...{col.RESET}")
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
  seed=-1
)
sleep(2)

with LLaMAInteract(params) as m:
  print(f"{col.LIGHTGREEN_EX}MODEL LOADED{col.RESET}\n")
  m.interact()
