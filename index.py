import pyttsx3

def set_voice_by_language(engine, language, person_name):
    voices = engine.getProperty('voices')
    
    for voice in voices:
        name = voice.name
        languages = voice.languages
        id = voice.id
        print(f"{name}-{languages}")
    


    for voice in voices:
        name = voice.name
        languages = voice.languages
        id = voice.id
        if(name == person_name): 
            engine.setProperty('voice', voice.id);
            break
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        return text

    except Exception as e:
        print(f"Error reading the file: {e}")
        return None





def main():
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 160) 

    # Ngôn ngữ bạn muốn sử dụng (ví dụ: Vietnamese)
    person_name = 'Kathy'
    desired_language = 'en'


    # Đặt giọng đọc tiếng cho ngôn ngữ mong muốn
    set_voice_by_language(engine, desired_language, person_name)

    # Văn bản bạn muốn đọc


    text_to_speak = read_text_from_file('text.txt')

    # Đọc văn bản
    engine.say(text_to_speak)
    engine.runAndWait()

if __name__ == "__main__":

    main()
