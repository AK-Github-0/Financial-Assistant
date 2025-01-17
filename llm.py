from vllm import LLM, SamplingParams


llm = LLM(model="facebook/opt-125m")

def generate_response(prompt: str) -> str:
    params = SamplingParams(temperature=0.7, max_tokens=100)
    output = llm.generate(prompt, params)
    return output[0].text.strip()
