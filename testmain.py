##test program

import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append('../..')

from main import DocChat

docchat = DocChat()

docchat.loadvectordb('_chat')
answer = docchat.answer_query('What is Ramukaka retirement requirement?')

print(answer)