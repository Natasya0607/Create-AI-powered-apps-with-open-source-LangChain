from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

# Inisialisasi model
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=""
)

# Fungsi untuk menjalankan chatbot
def chatbot(prompt):
    # Menentukan template
    template = """
    Question: {question}
    Silakan berikan langkah demi langkah jawaban:
    1. Langkah pertama
    2. Langkah kedua
    3. Langkah ketiga
    """
    # Membuat objek prompt dari template
    prompt_template = PromptTemplate(template=template, input_variables=["question"])
    formatted_prompt = prompt_template.format(question=str(prompt))
    return openai.invoke(formatted_prompt).content

# Membuat antarmuka Gradio untuk chatbot
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)
