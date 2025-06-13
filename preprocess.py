import os
import pandas as pd
import xml.etree.ElementTree as ET

def load_medquad_xml(folder_path='data/MedQuAD-master'):
    records = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".xml"):
                path = os.path.join(root, file)
                try:
                    tree = ET.parse(path)
                    root_elem = tree.getroot()
                    question_text = root_elem.findtext(".//question/text")
                    answer_text = root_elem.findtext(".//answer/text")
                    if question_text and answer_text:
                        records.append({
                            "question": question_text.strip(),
                            "answer": answer_text.strip()
                        })
                except Exception as e:
                    print(f"Skipping {file}: {e}")
    return pd.DataFrame(records)
