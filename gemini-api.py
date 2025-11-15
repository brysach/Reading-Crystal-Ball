from google import genai
import os
from os import listdir

# print("GEMINI_API_KEY =", repr(os.getenv("GEMINI_API_KEY")))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

folder_dir = "./images"

images_array = []

def generateFantasyStory():
    global folder_dir
    images_array.clear()
    for image_name in os. listdir(folder_dir):
        if image_name.endswith(".png"):
           images_array.append(os.path.join(folder_dir, image_name))

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = ["Can you make up a five-paragraph fantasy story based off these images", str(images_array)]
    )

    story_text = response.text

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(story_text)

    return response

generateFantasyStory()
