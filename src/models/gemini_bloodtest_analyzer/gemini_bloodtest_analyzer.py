from models.ports.bloodtest_analyzer import BloodTestAnalyzer
from PIL import Image
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import base64
from io import BytesIO


class GeminiBloodTestAnalyzer(BloodTestAnalyzer):
    def __init__(self):
        self.model = init_chat_model(
            "gemini-2.0-flash", model_provider="google_genai", temperature=0
        )

    def analyze(self, image):
        buff = BytesIO()
        opened_image = Image.open(image)
        opened_image.save(buff, format=opened_image.format)
        encoded_image = base64.b64encode(buff.getvalue()).decode("utf-8")

        user_message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "Describe this image",
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/png;base64,{encoded_image}",
                },
            ]
        )

        system_message = SystemMessage(
            content=[
                {
                    "type": "text",
                    "text": """
                        You are an expert in blood tests. You will receive an image and if the image is of a blood test 
                        you will make a detailed analysis explaining the results and the consequences of the changed values.
                        If the image is not a blood test, return an error message.

                        Requirements:

                        - Answer in portuguese
                        - Use markdown
                        - Make the analysis as detailed as possible
                        - Return a message "ERROR" if the image is not a blood test
                    """,
                }
            ]
        )

        result = self.model.invoke([system_message, user_message])

        return result.content
