from __future__ import division
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


import store

#Spoilers-Suck-4fce979a45e5.json

class TextTest:

    def __init__(self, show_name, seasons):
        print 'Initializing TextTest for %s' % show_name
        self.name = show_name
        self.entities = TextTest.load_keywords(show_name, seasons)
        print 'loaded %d entities from file' % len(self.entities)
        if len(self.entities) <= 0:
            TextTest.generate_keywords(show_name, seasons, self.entities)
    
    def test_content(self, content):
        return TextTest.compare_sentence(content, self.entities)
        

    @staticmethod
    def entities_text(text, ent_dict, show_name):
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

        ent_dict[show_name] = 1

    @staticmethod
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
        entity_count = len(entities)
        print len(entities)

        average_score = salience_sum /  entity_count

        if average_score > 0.5:
            return True
        else:
            return False

    @staticmethod
    def generate_keywords(show_name, seasons):
        ent_dict = {}
        print "generating keywords"
        for i in range(seasons):
            f = open ('storage/text/'+show_name+'/S'+str(i+1)+'.txt', 'r')
            TextTest.entities_text(f.read(), ent_dict, show_name)
        
        store.save_to_file(show_name, ent_dict)
        return ent_dict
    
    @staticmethod
    def load_keywords(show_name, seasons):
        print "loading keywords"
        save_data = store.load_from_file(show_name)
        if save_data != None:
            return save_data["entities"]
        else:
            return TextTest.generate_keywords(show_name, seasons)

    
