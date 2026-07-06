from openai import OpenAI
from vermithor.config import Config

class ReconAnalyzer:
    def __init__(self):
        self.client = OpenAI()
        self.model = Config.get_llm_model("recon")

    def analyze(self, recon_data):
        """
        Analyzes raw reconnaissance data using AI to identify high-value targets and attack surface.
        """
        system_prompt = "You are an expert bug bounty hunter and reconnaissance specialist. Your task is to analyze raw reconnaissance data (subdomains, live hosts, technologies, open ports) to identify high-value assets, unusual configurations, and potential entry points. Focus on identifying assets that align with common bug bounty program scopes, prioritize targets based on potential impact and ease of exploitation, and suggest next steps for deeper investigation, including potential attack surface expansion and specific manual checks. Consider OWASP methodologies and common bug bounty trends (e.g., API endpoints, cloud assets, authentication flows)."
        user_prompt = f"Analyze the following reconnaissance data and provide a structured summary with target prioritization and next-step suggestions:\n\n{recon_data}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_schema", "json_schema": {
                    "name": "recon_analysis",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "summary": {"type": "string"},
                            "prioritized_targets": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "target": {"type": "string"},
                                        "reason": {"type": "string"},
                                        "priority": {"type": "string", "enum": ["high", "medium", "low"]}
                                    },
                                    "required": ["target", "reason", "priority"],
                                    "additionalProperties": False
                                }
                            },
                            "next_steps": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["summary", "prioritized_targets", "next_steps"],
                        "additionalProperties": False
                    }
                }}
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during AI analysis: {str(e)}"
