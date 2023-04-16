from papercast.base import BaseProcessor
from papercast.base import Production
from langchain.chains import LLMChain


class LLMChainProcessor(BaseProcessor):
    input_types = {"text": str}
    output_types = {"text": str}

    def __init__(
        self,
        chain: LLMChain,
    ):
        self.chain = chain

    def process(self, production: Production, **kwargs) -> Production:
        setattr(production, "text", self.chain(getattr(production, "text")))
        return production
