import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from google_api_key import GOOGLE_API_KEY
import os
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

class DarkPatternClassifier:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1)
        template = """
        based on the content present on  website's which may or may not be malacious
        classify it into one of the dark_pattern and explain why and name the type of dark pattern
        from the list of dark_pattern
<content>
{content}
</content>
<website>
{website}
</website>
<dark_pattern>
{dark_pattern}
</dark_pattern>
"""
        self.chain = (
            PromptTemplate.from_template(template)
            | self.model
            | StrOutputParser()
        )
        self.dark_patterns = [
            'Bait and Switch', 'Hidden Costs', 'Forced Continuity', 'Confirm Shaming',
            'Disguised ads', 'Trigerred Fear', 'Social Proof', 'Triggering FOMO','Infinite Scroll Misdirection',
            'Trick Questions','Hidden Subscription','Sneak into Basket'
        ]

    def classify_dark_pattern(self, defects, website):
        answer = self.chain.invoke({"content": defects, "website": website, "dark_pattern": self.dark_patterns})
        return answer

def extract_arrays_from_input_string(input_string):
    # Extract content and dark patterns using regular expressions
    content_match = re.search(r"<content>(.*?)</content>", input_string, re.DOTALL)
    dark_pattern_match = re.search(r"<dark_pattern>(.*?)</dark_pattern>", input_string, re.DOTALL)

    if content_match and dark_pattern_match:
        content_str = content_match.group(1).replace('\n', '').strip()
        dark_pattern_str = dark_pattern_match.group(1).replace('\n', '').strip()

        # Convert content and dark pattern strings to arrays
        content = eval(content_str)
        dark_patterns = eval(dark_pattern_str)

        return content, dark_patterns
    else:
        return None, None
