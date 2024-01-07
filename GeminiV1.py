
import textwrap
import google.generativeai as genai

#INSERT API KEY HERE
genai.configure(api_key='')

def format_text(text):
    return textwrap.fill(text, width=80)

model = genai.GenerativeModel('gemini-pro')

while True:
    user_input = input("Enter a prompt (type 'END GEMINI' to exit): ")
    
    if user_input.upper() == 'END GEMINI':
        print("Exiting Gemini...")
        break
    
    response = model.generate_content(user_input)
    formatted_text = format_text(response.text)
    print(formatted_text)

