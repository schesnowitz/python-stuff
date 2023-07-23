from translate import Translator
with open("./english.txt", mode='r') as f:
    text = f.read()
    print(text)
    

    translator = Translator(to_lang="es")
    translation = translator.translate(text)
    with open('./myfile.txt', 'a') as f:
        f.write(translation) 
        # print(type(text))
        # print(translation)

    # text = f.readline()
    # print(text.strip())
    # translator = Translator(from_lang="english",to_lang="spanish")
    # translation = translator.translate(text)

# print(translation) 