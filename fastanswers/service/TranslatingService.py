from googletrans import Translator


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 21:24
# Version: 1.0.0
# Description: This is the class for the translating service
#

class TranslatingService():

    # gets the limits of the string which are translatable
    @classmethod
    def getCodeOffsets(cls, answer):
        o = []
        for i in range(len(answer)):
            # if it finds <code>
            if answer[i] == '<' and answer[i + 1] == 'c':
                for j in range(i, len(answer)):
                    # it will go on and search for the end
                    if answer[j] == '<' and answer[j + 1] == "/" and answer[j + 2] == "c":
                        o.append({
                            'start': i,
                            'end': j + 7
                        })
                        break
        return o

    # gets the limits of the string which aren't translatable
    @classmethod
    def getWordsOffsets(cls, codeOffsets: list):
        o: list = codeOffsets
        newO = []
        for i in range(len(o)):
            # if i is equal to 0, it will put 0 to the start
            if i == 0:
                newO.append({
                    'start': 0,
                    'end': (o[i].get('start')) - 1
                })
            else:
                newO.append({
                    'start': o[i - 1].get('end') + 1,
                    'end': (o[i].get('start')) - 1
                })
        return newO

    # creates a string using the given offsets and translate
    @classmethod
    def join(cls, answer, language):
        codeOffsets = cls.getCodeOffsets(answer)
        wordsOffsets = cls.getWordsOffsets(codeOffsets)
        newAnswer = []
        newCode = []
        result = ""
        for offset in wordsOffsets:
            newAnswer.append(answer[offset.get('start'):offset.get('end')])
        for offset in codeOffsets:
            newCode.append(answer[offset.get('start'):offset.get('end')])

        if len(wordsOffsets) > len(codeOffsets):
            for i in range(len(wordsOffsets)):
                result += cls.translate(newAnswer[i], language) + newCode[i]
        else:
            for i in range(len(codeOffsets)):
                result += cls.translate(newAnswer[i], language) + newCode[i]
        return result

    @classmethod
    def translate(cls, text, language):
        translator = Translator()
        return translator.translate(text, dest=language).text
