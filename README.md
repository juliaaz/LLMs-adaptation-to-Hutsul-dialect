# 🤖 Large Language Models adaptation to Hutsul dialect representation 🗣️

👩🏻‍🎓 This is the official implementation of Yuliia Maksymiuk's undergraduate thesis, supervised by Roman Kyslyi. It was submitted to fulfill the requirements for a Bachelor of Science degree in the Department of Computer Sciences and Information Technologies at the Faculty of Applied Sciences.

## 🔧 Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Repository Organization

This repository is organized into several directories, each serving a specific function. Below is a description of each directory:

## 🦾 finetune-llms
This directory contains the source code for fine-tuning LLMs with parameter-efficient fine-tuning approach LoRA.

- `finetune-data`: Directory with data used during training.
- `Fine_tune_Gemma_7B.ipynb`: Notebook for fine-tuning Google Gemma 7B model with 7B parameters.
- `Fine_tune_LLaMA-3.ipynb`: Notebook for fine-tuning the LLaMA-3 model.
- `Fine_tune_Mistral_7B.ipynb`: Notebook containing the fine-tuning code for the Mistral 7B model.

## 🗂️ hutsul-ukrainian-data
- **Description**: Houses all the Hutsul-Ukrainian datasets and data-related files used by the project. 

## 🧞‍♂️ rag-synthetic-data-generation
This directory contains all the logic for RAG pipeline for generating Hutsul-Ukrainian synthetic data. 
- `create-hutsul-base`: Directory with data and code for creating Hutsul knowledge base, which will be utilized in RAG pipeline.
- `get-sentences-from-ubertext`: Directory with algorithms to extract sentences from which synthetic Hutsul sentences will be created. We utilize fiction subcorpora from [UberText2.0](https://lang.org.ua/en/ubertext/) corpus by Dmytro Chaplynskyi.
- `rag-data`: Directory containing data utilized in RAG pipeline steps.
- `rag_synthetic.ipynb`: Notebook containing the logic for RAG pipeline, which generates Hutsul synthetic data.

## 🧰 utils
This directory contains additional files, that were utilized for creating Hutsul-Ukrainian parallel corpora, as well as splitting the data for future training. One important directory to mention is:
- `word_alignment_analysis`: Directory containing notebooks that analyzes Hutsul-Ukrainian sentence structure similarity for generated synthetic data, and original Hutsul-Ukrainian corpora.

## Pretrained Models

You can download pretrained models for future usage here:

- [LLaMA-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)
- [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- [Gemma-7B](https://huggingface.co/google/gemma-7b)

> ℹ️ Before utilizing these models, you have to check whether you have been granted access to the model, otherwise you will get errors.

## 🎭 Set-up

To get started with exploring this repository on your local machine, you can clone it using the following command:

```
git clone https://github.com/juliaaz/LLMs-adaptation-to-Hutsul-dialect.git
```

## 📩 Contributors

- [Yuliia Maksymiuk](https://www.linkedin.com/in/yulia-maksymiuk)
- [Roman Kyslyi](https://ua.linkedin.com/in/romankyslyi)
