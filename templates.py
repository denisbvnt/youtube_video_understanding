from langchain_core.prompts import ChatPromptTemplate


def define_prompt_template(model):
    system_prompt = "You are a helpful virtual assistant and you must answer a query based on a video transcript, which will be provided below. Answer only what was asked and nothing more than that."
    inputs = "Query: {query} \n Transcription: {transcription} \n Chat history: {chat_history}"
    if 'huggingface' in str(model.__class__).lower():
        user_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>".format(inputs)
    else:
        user_prompt = "{}".format(inputs)

    prompt_template = ChatPromptTemplate.from_messages([("system", system_prompt), ("user", user_prompt)])
    return prompt_template