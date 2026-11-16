# Master's Thesis Summary
The subject of my master thesis in the beginning is integration of machine learning in public procurement for two objectives: the first is prediction of the winner and the number of candidates, the second is prediction of the specific techniques. 
After integrating into the domain and understanding it (of course after the stage and the stay in the municipality and seeing the domain close up), I found a big problem that is the lack of the data because the municipality of my province was using paper files. I collected this data from the municipality of my province, even though little, I cleaned this data and generated new features needed. After that, I augmented the data and encoded it (because the data is text). I used Sentence Transformers and TF-IDF for the features description, and I used Label Encoder for the others.
Generally, I prepared the data for using. 
In the first, I used the models of machine learning and I stayed in KNN, Random Forest, and Extra Trees. And after, I saw I can use the models of deep learning and natural language processing. For the models of deep learning, I used DNN and GRU, and for the models of NLP, it is RAG and FiD. 
After training all these models, I developed with the framework Flask (backend Python, HTML, CSS, JavaScript in frontend) and I put these models:
- The models of machine learning, I trained them in Google Colab and used directly the model trained in the app.
- The models of deep learning, I put the models directly.
- The models of NLP (RAG and FiD), we can't use the model after training directly because this model should return to the data for retrieval of the documents similar to the example given.
This is my master thesis.
