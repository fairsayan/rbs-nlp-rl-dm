# Transformers Text Classification Lab

This lab demonstrates how to use pre-trained Transformer models for text classification using Hugging Face Transformers.

## Setup

1. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Start Jupyter Lab:
```bash
jupyter lab
```

### Alternative Setup (Manual)

If you prefer to set up manually:

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Jupyter Lab:
```bash
jupyter lab
```

## Lab Contents

- **transformer_text_classification_lab.ipynb**: Main lab notebook
- **setup.sh**: Environment setup script
- **requirements.txt**: Python dependencies
- **README.md**: This file

## Prerequisites

- Python 3.8+
- 4GB+ RAM
- GPU recommended but not required

Make sure `requirements.txt` is in the same directory as `setup.sh`.

## Dataset

The lab uses a simulated customer support tickets dataset with 4 categories:
- Technical Issue
- Billing
- Account Management
- General Inquiry

## Model

We use DistilBERT, an optimized version of BERT that maintains ~97% of performance with 40% fewer parameters.

## Key Features

- Complete text classification pipeline
- Fine-tuning with Hugging Face Transformers
- Performance evaluation and visualization
- Inference on new data
- Error analysis and optimization tips

## Requirements

- Python 3.8+
- 4GB+ RAM
- GPU recommended but not required

## Learning Objectives

By completing this lab, you will learn:
- How to load and preprocess text data
- How to use pre-trained Transformer models
- How to fine-tune models for specific tasks
- How to evaluate model performance
- How to deploy models for inference

## Additional Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)
- [BERT Paper](https://arxiv.org/abs/1810.04805)

## Author
Domenico Pontari <fairsayan@gmail.com>