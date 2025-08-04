import json
import pandas as pd
from v1_agent import executor
from judge import judge_check

# Load questions
with open("module_a_questions.json", "r") as f:
    questions = json.load(f)

# Load validation data
validation_df = pd.read_excel("validation_dataset.xlsx")

def get_expected(question):
    row = validation_df[validation_df["Question"].str.contains(question[:20], na=False)]
    return row["ExpectedInterpretation"].values[0] if not row.empty else "Not found"

for q in questions:
    print("\nMINI Agent:", q)
    user_input = input("Patient: ")
    prompt = f"Question: {q}\nPatient says: {user_input}"
    
    result = executor.run(prompt)
    print("🤖 Interpretation:", result)

    qa = judge_check(user_input, result)
    print("🧠 Judge:", qa)

    expected = get_expected(q)
    print("📊 Expected (from dataset):", expected)
