###################################################
#                  EDIT BELOW!                    #
###################################################

# It is worth noting this program is only made for "chat mode".
# Now exclusively works for GGUF files. I will include a script to convert GGML models to GGUF models.

MODELF = "/models/model.gguf" # path to model
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
