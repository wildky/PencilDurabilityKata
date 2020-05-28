# Writer

Writer is a Python library that emulates writing with a pencil and paper.

This is a solution to the [Pencil Durability Kata](https://github.com/PillarTechnology/kata-pencil-durability) described by Pillar Technology. 

## Installation
Writer does not have any requirements or external dependencies. Writer can run on Python 2 or 3. 

To use writer in your own project, download or clone the repository and import the `writer` module found in the repository's root directory to your code.


## Quick Start

In this example, the `writer` module is in the same directory as where the pyhton code is being executed. 

```python
from writer.paper import Paper
from writer.pencil import Pencil

pencil = Pencil(max_point_durability = 50, 
                length = 10, 
                eraser_durability = 500)
paper = Paper()

pencil.write("My plants are dying and I am not sure why", paper)
paper.text # returns "My plants are dying and I am not sure why"
pencil.erase("dying", paper) 
paper.text # returns "My plants are       and I am not sure why"
pencil.edit("happy", 14, paper)
paper.text # returns "My plants are happy and I am not sure why"
```

## Testing

All tests are contained in the `test_writer.py` file. Use the included Makefile task to run unit tests:

```bash
make test
```

If [make](https://www.gnu.org/software/make/) software is not installed, you can directly run the tests from the repository's root direcotry:

```bash
python test_writer.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)