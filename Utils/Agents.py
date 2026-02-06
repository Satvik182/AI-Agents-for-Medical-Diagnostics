from gemini_client import ask_gemini


class Agent:
    def __init__(self, medical_report=None, role=None, extra_info=None):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info or {}

    def _build_prompt(self) -> str:
        if self.role == "MultidisciplinaryTeam":
            return f"""
You are a multidisciplinary team of healthcare professionals.
Review the patient's medical reports from the Cardiologist, Psychologist, and Pulmonologist.
Analyze them and provide:
- Up to 3 possible health issues
- Reasoning for each
- Suggested next steps

Cardiologist Report:
{self.extra_info.get("cardiologist_report") or "(no report)"}

Psychologist Report:
{self.extra_info.get("psychologist_report") or "(no report)"}

Pulmonologist Report:
{self.extra_info.get("pulmonologist_report") or "(no report)"}
"""

        specialist_role = (self.role or "Specialist").lower()
        return f"""
You are a {specialist_role}.
Analyze the following medical report and provide:
- Possible diagnosis
- Reasoning
- Suggested next steps

Medical Report:
{self.medical_report}
"""

    def run(self):
        print(f"{self.role} is running...")
        prompt = self._build_prompt()
        try:
            return ask_gemini(prompt)
        except Exception as e:
            print(f"{self.role} error:", e)
            return None


class Cardiologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Cardiologist")


class Psychologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Psychologist")


class Pulmonologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Pulmonologist")


class MultidisciplinaryTeam(Agent):
    def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report):
        extra_info = {
            "cardiologist_report": cardiologist_report,
            "psychologist_report": psychologist_report,
            "pulmonologist_report": pulmonologist_report,
        }
        super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info)
