import os
import time

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('GPT_API_KEY'))

# list all of our assistants
def list_assistants(client, limit=100):
    return client.beta.assistants.list(order='desc', limit=str(limit))

# delete an assistant
def delete_assistant(client, assistant_id):
    try:
        response = client.beta.assistants.delete(assistant_id=assistant_id)
        print(f'Deleted: {assistant_id}')
        return response

    except Exception as e:
        print(f'Error deleting {assistant_id}: {e}')

# savings some assistants
do_not_delete_ids = {'', ''}

# get assistants list 
my_assistants = list_assistants(client)

# delete all assistants not in list
for assistant in my_assistants.data:
    if assistant.id not in do_not_delete_ids:
        delete_assistant(client, assistant.id)
        time.sleep(.2)
    else:
        print(f'Not deleting: {assistant.id}')