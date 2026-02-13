from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset
import json

def run_evaluation():
    with open("evaluation/test_dataset.json") as f:
        data = json.load(f)

    dataset = Dataset.from_list(data)

    results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy]
    )

    print(results)
