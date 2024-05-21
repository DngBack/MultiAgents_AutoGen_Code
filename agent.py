# Import packages and libraries 
import autogen
from autogen import AssistantAgent , UserProxyAgent
from autogen.code_utils import extract_code

TIMEOUT = 60

# set config
config_list = autogen.config_list_from_json("./OAI_CONFIG_LIST.json")

def _is_termination_msg(message):
    """
    Function to check the message is the end of conversation
    Args: 
        message: str 
    Return: 
        boolean 
    """
    if isinstance(message, dict): 
        """
        Check message with dict 
        """
        message = message.get("content") # Get content key from message
        if message is None: 
            return False 
    
    cb = extract_code(message)
    contain_code = False
    for c in cb: 
        if c[0] == "python": 
            contain_code = True
            break 
    return not contain_code


def initialize_agents():
    assistant = AssistantAgent(
        name = "assistant",
        max_consecutive_auto_reply=5,
        llm_config={
            "timeout": TIMEOUT, 
            "config_list":config_list,
        }
    )

    userproxy = UserProxyAgent(
        name="userproxy", 
        human_input_mode="NEVER",
        is_termination_msg=_is_termination_msg,
        max_consecutive_auto_reply=5, 
        code_execution_config={
            "work_dir": "coding", 
            "use_docker":False,
        }
    )

    return assistant, userproxy
