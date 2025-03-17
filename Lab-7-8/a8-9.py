import re
punctuations = r'[.,!?;:()]'
date = r'\d{1,2}[-/]\d{1,2}[-/]\d{3,4}|\d{3,4}[-/]\d{1,2}[-/]\d{1,2}[-/]'
urls = r'https?://[^$\s/.?#].[^\s]'
email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}'
number = r'(\d{1,3}(?:,\d{3})*(?:.\d{1,2})?)'
social_ids = r'@[a-zA-Z0-9_]+'
marathi_text = r'[\u0900-\u097F]+'
pattern = [punctuations,date,urls,email,number,social_ids,marathi_text]
combined_pattern = '|'.join(pattern)
def tokenizer(text):
    tokens = []
    for patterns in pattern:
        matches = re.findall(patterns,text)
        tokens.extend(matches)
    return tokens
text = '''जीवन म्हणजे एक अनंत संग्राम आहे. प्रत्येक क्षणी आपण काहीतरी जिंकतो किंवा हरतो. पण खरी विजयाची खूण म्हणजे 
आपण कितीदा हरलो तरी पुन्हा उठून लढायला तयार होतो. माझा ईमेल आहे karna123@example.com आणि माझी 
जन्मतारीख आहे 15-08-1985. मी कोण आहे, हे मला ठाऊक नाही; पण मी काय आहे, हे मला माहीत आहे. 
मी एक योद्धा आहे, आणि योद्धा कधीच हार मानत नाही. अधिक माहितीसाठी https://mrityunjay.com पहा. माझी ओळख @KarnaWarrior आहे आणि माझी शक्ती 1,234.56 इतकी आहे.'''
tokens = tokenizer(text)
print(tokens)