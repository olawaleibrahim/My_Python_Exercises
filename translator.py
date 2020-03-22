from translate import Translator
print('HEEEELLOOOOOOOO')
translator = Translator(to_lang='fr')
translation = translator.translate('This is a boy: Ibrahim Olawale')
print(translation)
print(Translator)

with open('scared.txt', mode='r') as my_story:
    story = my_story.read()
    print(story)
    translated_story = translator.translate(story)
    print(translated_story)

with open('translated_story.txt', mode='w') as my_translated_story:
    text = my_translated_story.write(translated_story)
    print(text)

    #text = my_story.write('The End.')
    #translated_text = translator.translate(my_story)
    # print(text)
    # print(my_story.readlines())
    # print(my_story)
