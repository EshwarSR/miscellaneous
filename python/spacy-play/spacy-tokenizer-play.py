import spacy
import re

# TOKEN_MATCH = re.compile(r"\d{3}-\d{2}-\d{4}", re.UNICODE).match


nlp = spacy.load('en_core_web_sm')
# doc = nlp(u"As an alternative, I suggested adding Crave, Sheeba and Iams to the broader GC story we're also running that week.")

doc = nlp(u"TBD on how things shake out, but either way we'll do ad June wk 5   and crave 123-12-2323-1000 units .")

# doc = nlp("TBD on how things shake out, but either way we'll do Crave June wk 5 and Iams Sheba July wk 1.")
# doc = nlp(u"I want to buy I dream of genie.")
# print([(i.text,i.pos_,i.tag_) for i in doc])


for i in doc:
    print(i.text, i.pos_, i.tag_)

noun_chunks = list(doc.noun_chunks)
print([i.text for i in noun_chunks])


"""
# =============
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

def custom_en_tokenizer(nlp):
    pattern_re = re.compile(r"\d{3}-\d{2}-\d{4}")
    return Tokenizer(nlp.vocab,
                     rules=English.Defaults.tokenizer_exceptions,
                     prefix_search=English.Defaults.prefixes,
                     suffix_search=English.Defaults.suffixes,
                     infix_finditer=English.Defaults.infixes,
                     token_match=pattern_re.match)

nlp = spacy.load('en', create_make_doc=custom_en_tokenizer)
# nlp.tokenizer = custom_en_tokenizer(nlp)

doc = nlp(u"Welcome!Hello!")
for i in doc:
    print(i.text, i.pos_, i.tag_)
"""
"""

import re
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spacy import util

pattern_re = re.compile("[0-9]{3}-[0-9]{2}-[0-9]{4}")

def custom_tokenizer(nlp):
    # infix_re = util.compile_infix_regex(('\\.\\.+',))
    return Tokenizer(nlp.vocab, English.Defaults.tokenizer_exceptions,
                                     English.Defaults.prefixes,
                                     English.Defaults.suffixes,
                                     English.Defaults.infixes,
                                     token_match=pattern_re.match)

nlp = spacy.load('en_core_web_sm')
nlp.tokenizer = custom_tokenizer(nlp)
doc = nlp("The products we are looking for is 123-45-6789 and Crave.")
print([t.text for t in doc])
"""