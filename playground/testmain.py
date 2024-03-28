##test program

import sys
sys.path.append('../..')

from chatengine import DocChat

docchat = DocChat()

docchat.loadvectordb('_chat')
docchat.answer_query('What is the guidance on credit card points?')