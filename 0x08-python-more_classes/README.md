# 0x08-python-more_classes

This project entails more examples on how use classes in Python.

## 0-rectangle.py

An empty class ``` Rectangle ``` that defines a rectangle.

## 1-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
	* property ``` def width(self): ``` to retrieve it
	* property setter ``` def width(self, value): ``` to set it:
		- ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
		- if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
	* property ``` def height(self): ``` to retrieve it
	* property setter ``` def height(self, value): ``` to set it:
		- ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
		- if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```

## 2-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
	* if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*

## 3-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
	* if ``` width ``` or ``` height ``` is equal to *0*, return an empty string

## 4-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```

## 5-rectangle.py

A class Rectangle that defines a rectangle by:
- Private instance attribute: ``` width ```:
        * property ``` def width(self): ``` to retrieve it
        * property setter ``` def width(self, value): ``` to set it:
                - ``` width ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` width must be an integer ``` is raised.
                - if ``` width ``` is less than *0*, a ``` ValueError ``` exception with the message ``` width must be >= 0 ``` is raised.
- Private instance attribute: ``` height ```:
        * property ``` def height(self): ``` to retrieve it
        * property setter ``` def height(self, value): ``` to set it:
                - ``` height ``` must be an integer, otherwise a ``` TypeError ``` exception with the message ``` height must be an integer ``` is raised.
                - if ``` height ``` is less than *0*, a ``` ValueError ``` exception with the message ``` height must be >= 0 ``` is raised.
- Instantiation with optional *width* and *height*: ``` def __init__(self, width=0, height=0): ```
- Public instance method: ``` def area(self): ``` that returns the rectangle area.
- Public instance method: ``` def perimeter(self): ``` that returns the rectangle perimeter:
        * if ``` width ``` or ``` height ``` is equal to *0*, perimeter is equal to *0*
- ``` print() ``` and  ``` str() ``` should print the rectangle with the character #:
        * if ``` width ``` or ``` height ``` is equal to *0*, return an empty string
- ``` repr() ``` should return a string representation of the rectangle to be able to recreate a new instance by using ``` eval() ```
- Print the message ``` Bye rectangle... (... are 3 dots not ellipsis) when an instance of Rectangle is deleted.

