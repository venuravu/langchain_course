from dotenv import load_dotenv
load_dotenv()

def get_text_length(text:str)->int:
    """Returns the length of the text by characters"""
    return len(text)
def main():
    print("Hello from langchain-course!")
    print(get_text_length("DOG"))


if __name__ == "__main__":
    main()
