Running the project:

1. In corenlp folder:
    ` java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000`
2. In django server folder:
    `python manage.py runserver`
3. Should be running in localhost:8000