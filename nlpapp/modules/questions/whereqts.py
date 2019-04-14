import spacy
import requests
import json
import nltk
from .Questions import Questions


class Where(Questions):
    def modify(self):
        nlp = spacy.load('en_core_web_sm')
        url = "http://localhost:9000/tregex"
        request_params = {"pattern":  "  NP = n1 > (S = n2 > ROOT) & $++ VP = n3 "  }
        text = self.text
        r = requests.post(url, data=text, params=request_params)
        json_data = json.loads(r.text)
        text1 = json_data['sentences'][0]['0']['match']
        tree = nltk.Tree.fromstring(text1, read_leaf=lambda x: x.split("/")[0])
        str1 = tree.leaves()

        sub = ' '.join(str1)
        doc = nlp(sub)
        for ent in doc.ents:
            sub_ent = ent.label_
        if sub_ent == 'GPE' or sub_ent == 'LOC':
            text2 = text.replace(sub,'Where')
            Q = text2.replace('.','?')
        return Q


if __name__ == "__main__":
    q = Where(input())
    print(q.get_text())
