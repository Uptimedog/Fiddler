# MIT License
#
# Copyright (c) 2024 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    ):
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function,
            is_separator_regex=is_separator_regex,
        )

    def split(self, document):
        return self._text_splitter.create_documents([document])


class HTMLSplitter:

    def __init__(self):
        pass


class CodeSplitter:

    def __init__(self):
        pass


class CharacterSplitter:

    def __init__(self):
        pass


class JSONSplitter:

    def __init__(self):
        pass


class MarkdownSplitter:

    def __init__(self):
        pass


class TokenSplitter:

    def __init__(self):
        pass


class SematicTextSplitter:

    def __init__(self):
        pass


if __name__ == "__main__":

    from langchain_text_splitters import RecursiveJsonSplitter

    # Suppose the json is quite big
    json_data = {
        "_id": "66e9b61eb99fa03ee481c5df",
        "greeting": "Hello, Kari Wyatt! You have 4 unread messages.",
        "favoriteFruit": "strawberry",
    }
    splitter = RecursiveJsonSplitter(max_chunk_size=1)
    json_chunks = splitter.split_json(json_data=json_data)
    print(json_chunks)
