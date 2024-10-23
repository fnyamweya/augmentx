import random
import nltk
from nltk.corpus import wordnet
from transformers import MarianMTModel, MarianTokenizer

# Ensure you have WordNet and MarianMT models installed
nltk.download('wordnet')

# Synonym Replacement
def synonym_replacement(sentence, n=1):
    words = sentence.split()
    new_sentence = []
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms and random.random() < n / len(words):
            synonym = random.choice(synonyms).lemmas()[0].name()
            new_sentence.append(synonym)
        else:
            new_sentence.append(word)
    return ' '.join(new_sentence)

# Random Word Insertion
def random_insertion(sentence, n=1):
    words = sentence.split()
    for _ in range(n):
        synonym = None
        while not synonym:
            random_word = random.choice(words)
            synonyms = wordnet.synsets(random_word)
            if synonyms:
                synonym = random.choice(synonyms).lemmas()[0].name()
        insert_position = random.randint(0, len(words))
        words.insert(insert_position, synonym)
    return ' '.join(words)

# Random Word Deletion
def random_deletion(sentence, p=0.1):
    words = sentence.split()
    new_sentence = [word for word in words if random.random() > p]
    return ' '.join(new_sentence) if new_sentence else random.choice(words)

# Back-translation (English -> Target -> English)
def back_translation(sentence, src_lang='en', tgt_lang='fr'):
    # Load MarianMT Model for translation
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Translate sentence to target language
    translated = model.generate(**tokenizer(sentence, return_tensors="pt", padding=True))
    tgt_sentence = tokenizer.decode(translated[0], skip_special_tokens=True)

    # Back-translate to source language
    back_model_name = f"Helsinki-NLP/opus-mt-{tgt_lang}-{src_lang}"
    back_tokenizer = MarianTokenizer.from_pretrained(back_model_name)
    back_model = MarianMTModel.from_pretrained(back_model_name)

    back_translated = back_model.generate(**back_tokenizer(tgt_sentence, return_tensors="pt", padding=True))
    final_sentence = back_tokenizer.decode(back_translated[0], skip_special_tokens=True)

    return final_sentence

# Text augmentation pipeline
def augment_text(text, synonym=False, insertion=False, deletion=False, back_translation=False):
    if synonym:
        text = synonym_replacement(text)
    if insertion:
        text = random_insertion(text)
    if deletion:
        text = random_deletion(text)
    if back_translation:
        text = back_translation(text)

    return text
