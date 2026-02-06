# Importing the needed modules
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from Utils.Agents import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam
import os
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def _pick_report_path() -> str:
    """
    Pick a medical report file to run.

    - If REPORT_PATH is set, use it (relative paths are resolved from project root).
    - Otherwise, pick the first .txt file inside `Medical Reports/`.
    """
    project_root = os.path.dirname(__file__)
    reports_dir = os.path.join(project_root, "Medical Reports")

    configured = os.getenv("REPORT_PATH")
    if configured:
        return configured if os.path.isabs(configured) else os.path.join(project_root, configured)

    if not os.path.isdir(reports_dir):
        raise FileNotFoundError(f"Missing reports folder: {reports_dir}")

    candidates = sorted(
        f for f in os.listdir(reports_dir) if f.lower().endswith(".txt")
    )
    if not candidates:
        raise FileNotFoundError(f"No .txt reports found in: {reports_dir}")

    return os.path.join(reports_dir, candidates[0])


def main():
    # Loading API key from a dotenv file.
    load_dotenv(dotenv_path="apikey.env")

    # Read the medical report (Windows-safe paths)
    report_path = _pick_report_path()
    print(f"Using medical report: {os.path.basename(report_path)}")
    with open(report_path, "r", encoding="utf-8") as file:
        medical_report = file.read()

    agents = {
        "Cardiologist": Cardiologist(medical_report),
        "Psychologist": Psychologist(medical_report),
        "Pulmonologist": Pulmonologist(medical_report),
    }

    # Function to run each agent and get their response
    def get_response(agent_name, agent):
        response = agent.run()
        return agent_name, response

    # Run the agents concurrently and collect responses
    responses = {}
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(get_response, name, agent): name
            for name, agent in agents.items()
        }

        for future in as_completed(futures):
            agent_name, response = future.result()
            responses[agent_name] = response

    team_agent = MultidisciplinaryTeam(
        cardiologist_report=responses.get("Cardiologist"),
        psychologist_report=responses.get("Psychologist"),
        pulmonologist_report=responses.get("Pulmonologist"),
    )

    # Run the MultidisciplinaryTeam agent to generate the final diagnosis
    final_diagnosis = team_agent.run()
    if final_diagnosis is None:
        final_diagnosis = "Diagnosis could not be generated due to agent failure."

    final_diagnosis_text = "### Final Diagnosis:\n\n" + final_diagnosis
    report_name = os.path.splitext(os.path.basename(report_path))[0]
    txt_output_path = os.path.join("Results", f"{report_name} - Diagnosis.txt")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(txt_output_path), exist_ok=True)

    # Write the final diagnosis to the text file
    with open(txt_output_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(final_diagnosis_text)

    print(f"Final diagnosis has been saved to {txt_output_path}")


if __name__ == "__main__":
    main()
