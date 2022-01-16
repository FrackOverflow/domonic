"""
    domonic.webapi.xpath
    ====================================
    https://developer.mozilla.org/en-US/docs/Glossary/XPath

"""

from typing import Any, Callable, Dict, List, Optional, Union

import json
import os
import sys


class XPathEvaluator:

    def __init__(self) -> None:
        pass


class XPathException:

    def __init__(self) -> None:
        pass


class XPathExpression:

    def __init__(self) -> None:
        pass


class XPathNSResolver:

    def __init__(self) -> None:
        pass


class XPathResult:

    ANY_TYPE = 0
    NUMBER_TYPE = 1
    STRING_TYPE = 2
    BOOLEAN_TYPE = 3
    UNORDERED_NODE_ITERATOR_TYPE = 4
    ORDERED_NODE_ITERATOR_TYPE = 5
    UNORDERED_NODE_SNAPSHOT_TYPE = 6
    ORDERED_NODE_SNAPSHOT_TYPE = 7
    ANY_UNORDERED_NODE_TYPE = 8
    FIRST_ORDERED_NODE_TYPE = 9

    def __init__(self) -> None:
        pass

    # def snapshotItem(i):
        # pass
