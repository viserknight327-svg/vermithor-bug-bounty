from openai import OpenAI
from vermithor.config import Config

class ReportGenerator:
    def __init__(self):
        self.client = OpenAI()
        self.model = Config.get_llm_model("report")

    def generate_report(self, finding_data, platform="hackerone"):
        """
        Generates a professional bug bounty report based on finding data.
        """
        system_prompt = f"You are a professional security researcher. Generate a high-quality, clear, and concise bug bounty report for the {platform} platform."
        user_prompt = f"Generate a report for the following finding data:\n\n{finding_data}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during report generation: {str(e)}"
