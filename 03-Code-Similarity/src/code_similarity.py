import os
import difflib
from sklearn.metrics.pairwise import cosine_similarity
from itertools import combinations
import torch
from transformers import BertTokenizer, BertModel

def read_file(file_path):
    """Read a UTF-8 source file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_cosine_similarity_bert(embedding1, embedding2):
    """Return the cosine similarity of two one-row embedding arrays."""
    cosine_sim = cosine_similarity(embedding1, embedding2)
    return cosine_sim[0][0]

def calculate_structural_similarity(text1, text2):
    """Return the SequenceMatcher ratio for two source strings."""
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def get_r_files_in_directory(directory):
    """Find R files directly inside the input directory."""
    return [
        os.path.join(directory, name)
        for name in sorted(os.listdir(directory))
        if name.lower().endswith(".r") and os.path.isfile(os.path.join(directory, name))
    ]

def get_bert_embeddings(text_list):
    """Return one BERT [CLS] embedding per source string."""

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased').to(device)
    model.eval()

    inputs = tokenizer(text_list, return_tensors='pt', padding=True, truncation=True, max_length=512).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()

    return embeddings

def compare_files(file_list):
    """Return both similarity scores for every distinct file pair."""
    similarity_results = []

    texts = [read_file(file) for file in file_list]

    embeddings = get_bert_embeddings(texts)

    for (i, file1), (j, file2) in combinations(enumerate(file_list), 2):
        cosine_sim_bert = calculate_cosine_similarity_bert([embeddings[i]], [embeddings[j]])

        structural_sim = calculate_structural_similarity(texts[i], texts[j])

        similarity_results.append((file1, file2, cosine_sim_bert, structural_sim))

    return similarity_results

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Compare all pairs of R files in a directory.")
    parser.add_argument("directory", help="Directory containing UTF-8 R scripts")
    directory = parser.parse_args().directory

    if not os.path.isdir(directory):
        parser.error(f"directory does not exist: {directory}")

    r_files = get_r_files_in_directory(directory)

    if len(r_files) < 2:
        parser.error("at least two R files are required")

    similarity_results = compare_files(r_files)

    sorted_results = sorted(similarity_results, key=lambda x: (x[2], x[3]), reverse=True)

    print("\nFile pairs ranked by similarity:")
    for file1, file2, cosine_sim_bert, structural_sim in sorted_results:
        print(
            f"{os.path.basename(file1)} - {os.path.basename(file2)}"
            f" | BERT cosine: {cosine_sim_bert:.2f} | Text match: {structural_sim:.2f}"
        )

if __name__ == "__main__":
    main()