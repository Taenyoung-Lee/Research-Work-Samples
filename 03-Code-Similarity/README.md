# Code Similarity Analysis

I wrote this Python script to compare R files in a directory. It gives each pair two scores and sorts by BERT cosine similarity, using the text-matching score to break ties.

## Methods

- **Text matching:** Python's `difflib.SequenceMatcher` compares raw character sequences. Comments, whitespace, and naming can affect the score.
- **Embedding similarity:** The script tokenizes each file with the pretrained `bert-base-uncased` model, pads the batch, and truncates each input to 512 tokens including special tokens. It takes the final hidden state of the first token ([CLS]) and uses scikit-learn to compute cosine similarity between file embeddings.

I use the scores to decide which pairs to read first. Two files can score highly because they solve the same problem or use the same template. The script compares all pairs and holds the files in memory, so the number of pairwise scores grows quadratically.

## How to run

From this project directory with Python 3.11 and an internet connection for the initial model download:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/code_similarity.py examples
```

The script prints the filename and both scores for each pair. It uses CUDA when available and otherwise runs on CPU. The [notebook](notebooks/code_similarity.ipynb) runs both comparisons on three synthetic R scripts. Open it with `python -m notebook notebooks/code_similarity.ipynb`. I haven’t run the BERT example in this version, so the notebook has no saved scores.

## Original source

The [original Python script](https://github.com/Taenyoung-Lee/ACC_project/blob/7049886caa1424eb216c79e37f95bbb60d2ccc49/ACC_Code.py) contains both scoring methods. The portfolio script keeps those methods and adds a command-line directory argument. The [original notebook](https://github.com/Taenyoung-Lee/ACC_project/blob/7049886caa1424eb216c79e37f95bbb60d2ccc49/ACC_Code_w_explain.ipynb) uses the same two approaches. Here I use synthetic scripts so the example can be shared.
