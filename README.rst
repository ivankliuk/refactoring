Serpent refactoring
===================

Collection of well known refactoring techniques translated into Python.


**Composing Methods**
 - `Extract Method <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/extract_method.py>`_
 - `Inline Method <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/inline_method.py>`_
 - `Inline Temp <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/inline_temp.py>`_
 - `Replace Temp with Query <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/replace_temp_with_query.py>`_
 - `Introduce Explaining Variable <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/introduce_explaining_variable.py>`_
 - `Split Temporary Variable <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/split_temporary_variable.py>`_
 - `Remove Assignments to Parameters <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/remove_assignments_to_parameters.py>`_
 - `Replace Method with Method Object <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/replace_method_with_method_object.py>`_
 - `Substitute Algorithm <https://github.com/ivankliuk/refactoring/blob/master/composing_methods/substitute_algorithm.py>`_

**Moving Features Between Objects**
 - Move Method
 - Move Field
 - Extract Class
 - Inline Class
 - Hide Delegate
 - Remove Middle Man
 - Introduce Foreign Method
 - Introduce Local Extension

**Organizing Data**
 - Self Encapsulate Field
 - Replace Data Value with Object
 - Change Value to Reference
 - Change Reference to Value
 - Replace Array with Object
 - Duplicate Observed Data
 - Change Unidirectional Association to Bidirectional
 - Change Bidirectional Association to Unidirectional
 - `Replace Magic Number with Symbolic Constant <https://github.com/ivankliuk/refactoring/blob/master/organizing_data/replace_magic_number_with_symbolic_constant.py>`_
 - `Encapsulate Field <https://github.com/ivankliuk/refactoring/blob/master/organizing_data/encapsulate_field.py>`_
 - Encapsulate Collection
 - Replace Record with Data Class
 - Replace Type Code with Class
 - Replace Type Code with Subclasses
 - Replace Type Code with State/Strategy
 - Replace Subclass with Fields

**Simplifying Conditional Expressions**
 - Decompose Conditional
 - Consolidate Conditional Expression
 - Consolidate Duplicate Conditional Fragments
 - Remove Control Flag
 - Replace Nested Conditional with Guard Clauses
 - Replace Conditional with Polymorphism
 - Introduce Null Object
 - Introduce Assertion

**Making Method Calls Simpler**
 - Rename Method
 - Add Parameter
 - Remove Parameter
 - Separate Query from Modifier
 - Parameterize Method
 - Replace Parameter with Explicit Methods
 - Preserve Whole Object
 - Replace Parameter with Method
 - Introduce Parameter Object
 - Remove Setting Method
 - Hide Method
 - Replace Constructor with Factory Method
 - Encapsulate Downcast
 - Replace Error Code with Exception
 - Replace Exception with Test

**Dealing with Generalization**
 - Pull Up Field
 - Pull Up Method
 - Pull Up Constructor Body
 - Push Down Method
 - Push Down Field
 - Extract Subclass
 - Extract Superclass
 - Extract Interface
 - Collapse Hierarchy
 - Form Template Method
 - Replace Inheritance with Delegation
 - Replace Delegation with Inheritance

**Big Refactorings**
 - Tease Apart Inheritance
 - Convert Procedural Design to Objects
 - Separate Domain from Presentation
 - Extract Hierarchy
