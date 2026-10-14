# W11D4 — RAG Evaluation and Optimization with Ragas

##  Project Overview

This project implements and evaluates a Retrieval-Augmented Generation (RAG) pipeline using a local language model. The system retrieves relevant information from a knowledge base and uses it to generate answers to user questions.

The Ragas framework is used to evaluate the quality of the generated answers and the retrieved context. A retrieval optimization experiment is also performed by increasing the number of retrieved chunks from **k = 3 to k = 5**.

##  Objectives

- Build a functional RAG pipeline.
- Prepare a knowledge base containing machine learning and RAG-related concepts.
- Create and evaluate 10 question-and-answer examples.
- Measure RAG performance using four Ragas metrics.
- Optimize retrieval settings and compare the initial and optimized scores.
- Export evaluation results and comparison reports as CSV files.

##  Technologies Used

- **Python** — implementation and data processing
- **Google Colab** — notebook execution environment
- **LangChain** — document processing and retrieval
- **ChromaDB** — vector storage and similarity search
- **Hugging Face Transformers** — local language model
- **Qwen2.5-0.5B-Instruct** — answer generation and local evaluation
- **Sentence Transformers (`all-MiniLM-L6-v2`)** — text embeddings
- **Ragas** — RAG evaluation
- **Pandas** — result analysis and CSV export

##  System Workflow

1. Create a knowledge base containing machine learning and RAG concepts.
2. Split documents into smaller chunks using `RecursiveCharacterTextSplitter`.
3. Generate embeddings using `all-MiniLM-L6-v2`.
4. Store the document chunks in ChromaDB.
5. Retrieve relevant chunks for each question.
6. Generate answers using the local Qwen2.5-0.5B-Instruct model.
7. Evaluate the initial pipeline using four Ragas metrics.
8. Increase the retrieval parameter from `k = 3` to `k = 5`.
9. Re-generate answers and evaluate the optimized pipeline.
10. Save and compare the evaluation results.

##  Evaluation Metrics

| Metric | Description |
|---|---|
| Faithfulness | Measures whether the generated answer is supported by the retrieved context. |
| Answer Relevancy | Measures how relevant the generated answer is to the question. |
| Context Precision | Evaluates whether relevant information is ranked appropriately among the retrieved context. |
| Context Recall | Measures how much of the information needed to answer the question is captured by the retrieved context. |

Scores are compared before and after retrieval optimization to identify changes in performance.

##  Optimization Experiment

The initial pipeline uses **k = 3**, meaning it retrieves up to three document chunks for a question. The optimized pipeline uses **k = 5**, allowing it to retrieve up to five chunks.

The evaluation scores are compared to determine whether retrieving additional context improves answer quality and retrieval performance. Increasing `k` is an experiment, so improvements should be reported based on the actual results.

##  Output Files

The notebook generates the following CSV files:

| File | Purpose |
|---|---|
| `w11d4_rag_answers_initial.csv` | Initial generated answers, retrieved contexts, and ground-truth answers |
| `w11d4_ragas_initial_scores.csv` | Initial Ragas evaluation results |
| `w11d4_rag_answers_optimized.csv` | Answers generated using the optimized retriever |
| `w11d4_ragas_optimized_scores.csv` | Ragas evaluation results after optimization |
| `w11d4_ragas_comparison.csv` | Comparison of initial and optimized mean metric scores |

##  How to Run

1. Open the W11D4 notebook in Google Colab.
2. Run the notebook cells in order.
3. Allow the document embeddings, ChromaDB vector store, and local language model to load.
4. Generate the initial RAG answers and evaluate them with Ragas.
5. Run the retrieval optimization experiment.
6. Review the comparison table and download the generated CSV files.

##  Expected Outcome

The project produces a working RAG evaluation workflow, initial and optimized evaluation results, and a CSV report comparing the four Ragas metrics.

The experiment helps demonstrate how retrieval settings can affect answer generation and RAG system performance.

##  Learning Outcomes

- Understanding the Retrieval-Augmented Generation workflow.
- Using vector embeddings and similarity search for document retrieval.
- Evaluating RAG systems with faithfulness, answer relevancy, context precision, and context recall.
- Performing retrieval optimization through parameter tuning.
- Comparing model evaluation results and exporting them for analysis.

##  Conclusion

This project demonstrates an end-to-end RAG evaluation and optimization workflow using a local language model, ChromaDB, LangChain, and Ragas. It provides a structured approach to measuring RAG quality and examining the effects of retrieval configuration changes.
