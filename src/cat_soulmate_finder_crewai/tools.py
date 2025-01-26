"""Tools."""
from typing import Type

from crewai.tools import BaseTool
from crewai_tools import FileWriterTool
import base64
from langchain_community.tools import TavilySearchResults, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from pydantic import BaseModel, Field




wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=3, doc_content_chars_max=100000, load_all_available_meta=True
    )
)


class WikipediaSearchTool(BaseTool):
    """Search Wikipedia for information about a topic.

    But only one query at a time"""

    name: str = "Wikipedia Search Tool"
    description: str = (
        "Search Wikipedia for information about a topic. But only one query at a time"
    )

    def _run(self, query: str) -> str:
        return wikipedia.run(query)


tavily = TavilySearchResults(
    max_results=5,
    include_answer=True,
)


class WebSearchTool(BaseTool):
    name:str = "Web Search Tool"
    description : str= "Search the web for information. But only one string at a time"

    def _run(self, query: str) -> str:
        return tavily.run(query)