# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Spoilers-Suck-4fce979a45e5.json

def entities_text(text, ent_dict):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')


    for entity in entities:
        if entity_type[entity.type] != 'PERSON' or entity.name[0] >= 'A' and entity.name[0] <= 'Z':
            weight = entity.salience
            if entity_type[entity.type] == 'PERSON':
                weight = 1
                #break multiword names into 2
                if ' ' in entity.name:
                    name = entity.name.lower().split(' ')
                    for key in name:
                        if not key in ent_dict or ent_dict[key] < 0.33:
                            ent_dict[key] = 0.33

            elif entity_type[entity.type] == 'EVENT' or entity_type[entity.type] == 'LOCATION':
                if entity.name[0] >= 'A' and entity.name[0] <= 'Z':
                    weight = 0.5 + 2 * entity.salience
                else:
                    weight = 0.2 + entity.salience
            else:
                if entity.name[0] >= 'A' and entity.name[0] <= 'Z':
                    weight = 0.1 + entity.salience
            
            if not entity.name.lower() in ent_dict or ent_dict[entity.name.lower()] < weight:
                ent_dict[entity.name.lower()] = weight

    ent_dict['game of thrones'] = 1

def compare_sentence(text, model):
    client = language.LanguageServiceClient()

    text = text.decode('utf-8')

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities

    #track total salience within the document
    salience_sum = 0
    tokens_hit = 0

    for entity in entities:
        if entity.name.lower() in model:
            tokens_hit += 1

            salience = model[entity.name.lower()] 
            if salience == 1:
                return True
            
            salience_sum += salience

    print salience_sum
    print tokens_hit
    print len(entities)
    

entities = {}

for i in range(1, 8):
    f = open ('S'+str(i)+'.txt', 'r')
    entities_text(f.read(), entities)

compare_sentence("At Winterfell, Arya Stark talks to her sister Sansa Stark about borrowing Bran Stark's bow and arrow. She tells Sansa that she practiced several times until she finally hit the bullseye. Arya recalls that their father Eddard Stark had been watching and clapped his hands in praise of her accomplishments. Arya reasons that their father knew that the rules were wrong but that his daughter was in the right. She then confronts Sansa about her alleged role in their father's death. ", entities)

