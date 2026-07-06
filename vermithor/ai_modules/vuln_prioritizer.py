from openai import OpenAI
from vermithor.config import Config

class VulnPrioritizer:
    def __init__(self):
        self.client = OpenAI()
        self.model = Config.get_llm_model("prioritize")

    def prioritize(self, scan_results):
        """
        Analyzes vulnerability scan results using AI to prioritize findings and reduce false positives.
        """
        system_prompt = "You are an expert security analyst. Analyze the provided vulnerability scan results to prioritize findings, identify potential false positives, and suggest manual verification steps."
        user_prompt = f"Analyze the following scan results and provide a prioritized list of vulnerabilities with impact assessments and manual test suggestions:\n\n{scan_results}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_schema", "json_schema": {
                    "name": "vuln_prioritization",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "vulnerabilities": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "severity": {"type": "string", "enum": ["critical", "high", "medium", "low", "info"]},
                                        "impact": {"type": "string"},
                                        "confidence": {"type": "integer", "description": "Confidence score from 0 to 100"},
                                        "manual_verification": {"type": "string"}
                                    },
                                    "required": ["name", "severity", "impact", "confidence", "manual_verification"],
                                    "additionalProperties": False
                                }
                            },
                            "potential_chains": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["vulnerabilities", "potential_chains"],
                        "additionalProperties": False
                    }
                }}
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during AI prioritization: {str(e)}"
