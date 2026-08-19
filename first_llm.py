from google import genai
def main():
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents ="explain what an llm is in exactly three sentences",
        )
    print(response.text)
if __name__=="__main__":
    main()