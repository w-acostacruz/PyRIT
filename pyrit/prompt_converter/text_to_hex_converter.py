
from pyrit.models import PromptDataType
from pyrit.prompt_converter import ConverterResult, PromptConverter
from math import floor


class textToHexConverter(PromptConverter):

    async def convert_async(self, *, prompt: str, input_type: PromptDataType = "text") -> ConverterResult:
        if not self.input_supported(input_type):
            raise ValueError("Input type not supported")
        output_text = self._hex(prompt)
        return ConverterResult(output_text=output_text, output_type="text")

    def input_supported(self, input_type: PromptDataType) -> bool:
        return input_type == "text"

    def _hex(self, text:str) -> str:
        exp = 0
        hexTbl = ["0", "1", "2", "3", "4", "5",
                  "6", "7", "8", "9", "a",
                  "b", "c", "d", "e", "f"]
        endString = ""
        if len(text) == 0:
            endString = "0"
        for x in text:
            aVal = ord(x)
            aValTemp = aVal
            while (aValTemp >= 16):
                exp = exp + 1
                aValTemp = aVal / 16
            i = 0
            for y in range(exp + 1):
                if (i != 0):
                    if (aValTemp < 15):
                        endString = endString + hexTbl[aValTemp]
                        break
                    while (aValTemp >= 16):
                        exp = exp + 1
                        aValTemp = aVal / 16
                aValTemp = floor(aValTemp)
                aVal = aVal - ((16 ** exp) * aValTemp)
                endString = endString + hexTbl[aValTemp]
                aValTemp = aVal
                exp = 0
                i = 1
        return endString



