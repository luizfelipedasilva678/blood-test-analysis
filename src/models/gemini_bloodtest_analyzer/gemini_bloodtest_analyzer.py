from models.ports.bloodtest_analyzer import BloodTestAnalyzer
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from PIL import Image
from google import genai
from os import environ

PROMPT = (
    "Make a blood test analysis of this image and answer in portuguese. If the image is not a blood test, answer in portuguese that it is not a blood test.",
)


class GeminiBloodTestAnalyzer(BloodTestAnalyzer):
    def __init__(self):
        self.client = genai.Client(api_key=environ["GEMINI_API_KEY"])
        self.search_tool = Tool(google_search=GoogleSearch())
        self.prompt = PROMPT

    def analyze(self, image):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                Image.open(image),
                self.prompt,
            ],
            config=GenerateContentConfig(
                tools=[self.search_tool],
                response_modalities=["TEXT"],
            ),
        )

        return response.text
