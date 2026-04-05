import spacy 

nlp = spacy.load('en_core_web_sm')


def extract_info(text):

    doc = nlp(text)

    actor = None
    actions = []
    objects = []
    conditions = []

    for token in doc:
        if token.dep_ == 'nsubj':
            actor = ' '.join([t.text for t in token.subtree])

        if token.pos_ == 'VERB':
            actions.append(token.lemma_)

        if token.dep_ in ('dobj', 'pobj'):
            objects.append(token.text)

    for sent in doc.sents:
        if any(token.text.lower() == 'if' for token in sent):
            conditions.append(sent.text)

    return {
        'actor': actor,
        'actions': actions,
        'objects': objects,
        'conditions': conditions,
    }

# text = ' the user can login using email and password'
# print(extract_info(text))
