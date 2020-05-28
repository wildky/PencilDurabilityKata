# Writer

Writer is a Python library that emulates writing with a pencil and paper.

This is a solution to the [Pencil Durability Kata](https://github.com/PillarTechnology/kata-pencil-durability) described by Pillar Technology. 

## Dependencies
Writer does not have any requirements or external dependencies. Writer can run on Python 2 or 3. 

## Installation
Clone the repository on your local machine:

```bash
git clone https://github.com/wildky/PencilDurabilityKata.git
```

To use writer in your own python project, import the `writer` module found in the repository's root directory to your code:

```python
import writer
```

## Quick Start
In this example, the `writer` module is in the same directory where the python code is being executed. 

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

All tests are contained in the `test_writer.py` file. 

Use the included Makefile task to run unit tests by running this command from the repository's root directory:

```bash
make test
```

If [make](https://www.gnu.org/software/make/) software is not installed, you can directly run the tests from the repository's root direcotry:

```bash
python test_writer.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)