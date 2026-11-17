# Code Similarity Analysis

This Python project compares pairs of UTF-8 R scripts. The program reads files in one directory, computes two scores for every pair, and ranks the pairs by embedding cosine similarity followed by text similarity.

## Methods

- **Text matching:** Python's `difflib.SequenceMatcher` compares raw character sequences. Comments, whitespace, and naming can affect the score.
- **Embedding similarity:** The script tokenizes each file with the pretrained `bert-base-uncased` model, pads the batch, and truncates each input to 512 tokens including special tokens. It takes the final hidden state of the first token ([CLS]) and uses scikit-learn to compute cosine similarity between file embeddings.

The scores can help prioritize manual review. Similarity can come from common task requirements, shared templates, or common programming idioms. The script compares all pairs and holds the files in memory, so the number of pairwise scores grows quadratically.

## How to run

From this project directory with Python 3.11 and an internet connection for the initial model download:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/code_similarity.py examples
```

The script prints the filename and both scores for each pair. It uses CUDA when available and otherwise runs on CPU. The [notebook](notebooks/code_similarity.ipynb) illustrates the two scores on the same three synthetic R scripts. Run it with `python -m notebook notebooks/code_similarity.ipynb`. Example inputs are synthetic and the notebook is published with empty outputs. The script and notebook were reviewed statically. The pretrained model has not been run for this portfolio.

## Original source

The [original Python script](https://github.com/Taenyoung-Lee/ACC_project/blob/7049886caa1424eb216c79e37f95bbb60d2ccc49/ACC_Code.py) contains both scoring methods. The portfolio script keeps those methods and adds a command-line directory argument. The [original notebook](https://github.com/Taenyoung-Lee/ACC_project/blob/7049886caa1424eb216c79e37f95bbb60d2ccc49/ACC_Code_w_explain.ipynb) informed the new example notebook. The original assignment filenames and saved outputs are omitted.
