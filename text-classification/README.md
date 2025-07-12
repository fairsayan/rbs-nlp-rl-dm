# Text Classification with Transformers

This laboratory demonstrates how to use pre-trained Transformer models for text classification using Hugging Face Transformers. The lab includes a complete example of fine-tuning DistilBERT for customer support ticket classification.

### Unified Environment Setup (Recommended)
This laboratory is part of a unified course environment. From the repository root:

```bash
# Initial setup for all laboratories (first time only)
./setup.sh

# Activate the shared environment
source .venv/bin/activate

# Navigate to the lab and start Jupyter
cd text-classification/
jupyter notebook transformer_text_classification_lab.ipynb
```

### Alternative Local Setup
If you prefer to set up only this laboratory:

```bash
python3 -m venv venv
source venv/bin/activate
pip install transformers datasets torch scikit-learn pandas matplotlib seaborn numpy accelerate
jupyter notebook transformer_text_classification_lab.ipynb
```

## Dataset and Model

### Dataset
The laboratory uses a simulated customer support tickets dataset with 4 categories:
- **Technical Issue**
- **Billing**
- **Account Management**
- **General Inquiry**

### Dataset Statistics
- **Train set**: 138 examples
- **Validation set**: 30 examples
- **Test set**: 30 examples
- **Batch size**: 8
- **Training epochs**: 5

### Model
Uses **DistilBERT** (`distilbert-base-uncased`), an optimized version of BERT that maintains ~97% of performance with 40% fewer parameters.

## Results Achieved

The fine-tuned model achieved the following performance on the test set:
- **Accuracy**: 93.3%
- **F1-Score**: 93.3%

Detailed results are saved in `results/results_summary.json`.

## Lab Contents

The notebook `transformer_text_classification_lab.ipynb` covers:

1. **Setup and Imports** - Installation and import of necessary libraries
2. **Dataset Loading and Exploration** - Input data analysis
3. **Data Preprocessing** - Preparation for training
4. **Pre-trained Model Loading** - DistilBERT setup
5. **Fine-tuning** - Model training on specific data
6. **Evaluation** - Performance metrics and visualizations
7. **Inference on New Data** - Testing the trained model
8. **Conclusions** - Summary and final considerations

## Technical Requirements

- **Python**: 3.8+
- **RAM**: 4GB+ recommended
- **GPU**: Recommended but not required
- **Storage**: ~500MB for models and checkpoints

## Main Libraries

- `transformers` - Hugging Face Transformer models
- `datasets` - Dataset management
- `torch` - PyTorch framework
- `scikit-learn` - Evaluation metrics
- `pandas` - Data manipulation
- `matplotlib/seaborn` - Visualizations

## Using the Trained Model

The fine-tuned model is saved in `fine_tuned_model/` and can be used for inference:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load the trained model
tokenizer = AutoTokenizer.from_pretrained('./fine_tuned_model')
model = AutoModelForSequenceClassification.from_pretrained('./fine_tuned_model')

# Create classification pipeline
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

# Classify new text
result = classifier("My account has been locked")
print(result)
```

## Learning Objectives

By completing this laboratory, you will learn:
- How to load and preprocess text data
- How to use pre-trained Transformer models
- How to fine-tune models for specific tasks
- How to evaluate model performance
- How to use the model for inference on new data
- Error analysis and optimization techniques

## Additional Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [Transformers Fine-tuning Guide](https://huggingface.co/docs/transformers/training)

## Author
Domenico Pontari <fairsayan@gmail.com>