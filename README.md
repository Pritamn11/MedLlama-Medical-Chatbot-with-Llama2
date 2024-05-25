# MedLlama-Medical-Chatbot-with-Llama2

# How to run ?

##  Steps to run the project

## 1. Clone the repository

```bash
https://github.com/Pritamn11/MedLlama-Medical-Chatbot-with-Llama2.git
```

## 2. Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
medenv/Scripts/activate
```

## 3. Activate the virtual environment

```bash
medenv\Scripts\activate
```

## 4. Install the requirements

```bash
pip install -r requirements.txt
```

## 5. Download and store the quantized model from the link provided in the model folder.


```bash
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

## 6. Set up Qdrant Database

**Pull the Qdrant Docker image**

```bash
docker pull qdrant/qdrant
```

**Run the Qdrant Docker container**

```bash
docker run -p 6333:6333 -v .:/qdrant/storage qdrant/qdrant
```

After running these command, you can access the Qdrant service at http://localhost:6333 and any data will be stored in the current directory on your host machine,

## 7. Run the ingest.py script

**To generate embeddings from text chunks and store them in a Qdrant collection named vector_db**
```bash
python ingest.py
```

## 8. Run the application

**Finally, start the Flask application**
```bash
python app.py
```

## 9. Access the application

Open your web browser and navigate to http://localhost:5000 to access the MedLlama-Medical-Chatbot application.



