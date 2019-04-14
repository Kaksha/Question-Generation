import requests
import json
import nltk
from nltk.tag.stanford import CoreNLPNERTagger
from .Questions import Questions

class SubWho(Questions):
	def modify(self):
		url = "http://localhost:9000/tregex"
		request_params = {"pattern":  " NP = n1 > (S = n2 > ROOT) & $++ VP = n3 "  }
		text = self.text
		# print(text)
		r = requests.post(url, data=text, params=request_params)
		json_data = json.loads(r.text)
		text1 = json_data['sentences'][0]['0']['match']
		tree = nltk.Tree.fromstring(text1, read_leaf=lambda x: x.split("/")[0])
		line = tree.leaves()
		sub = ' '.join(line)

		# NER tagging
		classified_text = CoreNLPNERTagger(url='http://localhost:9000').tag(sub.split())

		f = 1
		for i in classified_text:
			if i[1]!='PERSON':
				f = 0
				break
		text2 = text.replace(sub,'Who ')
		Q = text2.replace('.','?')
		return Q


if __name__ == "__main__":
    q = SubWho(input())
    print(q.get_text())
