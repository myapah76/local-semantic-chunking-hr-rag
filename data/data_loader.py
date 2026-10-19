import os
import json
import logging
from typing import List, Dict
from data.dataset_schema import HRDocument, GroundTruthQuery, DocumentType

logger = logging.getLogger(__name__)

class DataLoader:
    """
    Utility to load, validate, and manage datasets for RBL benchmarks.
    Supports sample fixtures and custom directories containing real CVs/JDs/Policies.
    """
    def __init__(self, data_dir: str = None):
        if data_dir is None:
            data_dir = os.path.dirname(__file__)
        self.data_dir = data_dir
        self.sample_dir = os.path.join(data_dir, "sample_data")
        self.ground_truth_path = os.path.join(data_dir, "ground_truth.json")

    def load_all_documents(self) -> List[HRDocument]:
        documents: List[HRDocument] = []
        file_mapping = {
            "cv_samples.json": DocumentType.CV,
            "jd_samples.json": DocumentType.JD,
            "policy_samples.json": DocumentType.POLICY
        }

        for filename, expected_type in file_mapping.items():
            filepath = os.path.join(self.sample_dir, filename)
            if not os.path.exists(filepath):
                logger.warning(f"File not found: {filepath}")
                continue

            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    doc = HRDocument(**item)
                    documents.append(doc)

        logger.info(f"Loaded {len(documents)} documents across all categories.")
        return documents

    def load_ground_truth(self) -> List[GroundTruthQuery]:
        if not os.path.exists(self.ground_truth_path):
            raise FileNotFoundError(f"Ground truth file missing: {self.ground_truth_path}")

        with open(self.ground_truth_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            queries = [GroundTruthQuery(**item) for item in data]

        logger.info(f"Loaded {len(queries)} ground truth queries.")
        return queries

    def get_documents_by_type(self) -> Dict[str, List[HRDocument]]:
        docs = self.load_all_documents()
        categorized: Dict[str, List[HRDocument]] = {
            DocumentType.CV.value: [],
            DocumentType.JD.value: [],
            DocumentType.POLICY.value: []
        }
        for d in docs:
            categorized[d.doc_type.value].append(d)
        return categorized

    def get_queries_by_type(self) -> Dict[str, List[GroundTruthQuery]]:
        queries = self.load_ground_truth()
        categorized: Dict[str, List[GroundTruthQuery]] = {
            DocumentType.CV.value: [],
            DocumentType.JD.value: [],
            DocumentType.POLICY.value: []
        }
        for q in queries:
            categorized[q.doc_type.value].append(q)
        return categorized
