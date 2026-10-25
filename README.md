# College Assistant

A simple chatbot that answers questions about college rules, exams, fees and academic policies.
It reads the college documents and answers only from them.

## Built with
- LangChain
- Streamlit
- ChromaDB
- Google Gemini (chat and embeddings)

## Run locally
1. Install packages:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file with:
   ```
   GOOGLE_API_KEY=your_key_here
   ```
3. Start the app:
   ```
   streamlit run app.py
   ```

## Update the documents
1. Add the new files to the documents folder
2. Run `python ingest.py`
3. Push the updated `chroma_db` folder to GitHub
