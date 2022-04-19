import os
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

root = os.path.dirname(os.path.abspath(__file__))
download_dir = os.path.join(root, 'nltk_data')
# os.chdir(download_dir)
nltk.data.path.append(download_dir)



import datetime

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<string:input>/')
def hello(input):
    tokenized = sent_tokenize(input)
    tagged = []
    for i in tokenized:
        
        # Word tokenizers is used to find the words and punctuation in a string
        wordsList = nltk.word_tokenize(i)
    
        # removing stop words from wordList
        # wordsList = [w for w in wordsList if not w in stop_words]
    
        # Tagger
        tagged.append(nltk.pos_tag(wordsList))

    """
    CC coordinating conjunction 
    CD cardinal digit 
    DT determiner 
    EX existential there (like: “there is” … think of it like “there exists”) 
    FW foreign word 
    IN preposition/subordinating conjunction 
    JJ adjective – ‘big’ 
    JJR adjective, comparative – ‘bigger’ 
    JJS adjective, superlative – ‘biggest’ 
    LS list marker 1) 
    MD modal – could, will 
    NN noun, singular ‘- desk’ 
    NNS noun plural – ‘desks’ 
    NNP proper noun, singular – ‘Harrison’ 
    NNPS proper noun, plural – ‘Americans’ 
    PDT predeterminer – ‘all the kids’ 
    POS possessive ending parent’s 
    PRP personal pronoun –  I, he, she 
    PRP$ possessive pronoun – my, his, hers 
    RB adverb – very, silently, 
    RBR adverb, comparative – better 
    RBS adverb, superlative – best 
    RP particle – give up 
    TO – to go ‘to’ the store. 
    UH interjection – errrrrrrrm 
    VB verb, base form – take 
    VBD verb, past tense – took 
    VBG verb, gerund/present participle – taking 
    VBN verb, past participle – taken 
    VBP verb, sing. present, non-3d – take 
    VBZ verb, 3rd person sing. present – takes 
    WDT wh-determiner – which 
    WP wh-pronoun – who, what 
    WP$ possessive wh-pronoun, eg- whose 
    WRB wh-adverb, eg- where, when
    """
    criteriaList = ["NN", "NNS", "NNPS"]
    output = ""

    for i in tagged:
        for j in i:
            # print(j)
            if any(map(j.__contains__,criteriaList)):
                output += "bloody" + " "
                output += j[0] + " "
            else:output += j[0] + " "

    # print(output)
    output = output.replace(" .",".")
    output = output.replace(" ,",",")
    output = output.replace(" !","!")
    output = output.replace(" \'","\'")
    output = output.replace(". bloody",". Bloody")
    output = output.replace(", bloody",", Bloody")
    output = output.replace("! bloody","! Bloody")
    output = output.replace("is n\'t","isn\'t")
    output = output.replace("was n\'t","wasn\'t")
    return jsonify(
        original=input,
        bloodied=output,
    )


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)