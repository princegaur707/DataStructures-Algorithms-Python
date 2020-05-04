from collections import deque

graph = { "Alice":  ["Bob", "Claire", "Frank"],
      "Bob":    ["Alice"],
      "Claire": ["Alice", "Dennis", "Esther", "Frank"],
      "Dennis": ["Claire", "Esther", "George"],
      "Esther": ["Claire", "Dennis"],
      "Frank":  ["Alice", "Claire", "George"],
      "George": ["Dennis", "Frank"]
    }


