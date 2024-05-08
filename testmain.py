##test program

import sys
sys.path.append('../..')

from main import DocChat

docchat = DocChat()

docchat.loadvectordb('_chat')
answer = docchat.answer_query('What is the guidance on credit card points?')

print(answer)