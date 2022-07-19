#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import List, Any, Iterable


def flatten_recursive(lst: List[Any]) -> Iterable[Any]:
    """Flatten a list using recursion."""
    for item in lst:
        if isinstance(item, list):
            yield from flatten_recursive(item)
        else:
            yield item

def test_flatten_recursive():
    lst = [[1, 3], [2, 5], 1]

    assert list(flatten_recursive(lst)) == [1, 3, 2, 5, 1]

