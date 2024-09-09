#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, stringVal):
        if isinstance(stringVal, str):
            self._value = stringVal
        else:
            raise ValueError("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        
        normalized_value = self._value.replace('!', '.').replace('?', '.')
        
        
        sentences = [segment for segment in normalized_value.split('.') if segment.strip()]
        
        return len(sentences)
