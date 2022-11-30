<h1 align="center" id="top">0x01.PYTHON</h1>
IF/ELSE, LOOPS, FUNCTIONS.

<h2>Maru Resources</h2>


<h3>Man</h3>
<ul>
  <li>python3</li>
</ul>

<h2>Learning Objectives</h2>
<ul>
<li>Why Python programming is awesome.</li>
<li>Why indentation is so important in Python.</li>
<li>How to use the <code>if, if ... else</code> statements.</li>
<li>How to use comments.</li>
<li>How to affect values to variables.</li>
<li>How to use the <code>while</code> and <code>for</code> loops.</li>
<li>How is Python’s <code>for</code> different from <code>C</code>‘s.</li>
<li>How to use the <code>break</code> and <code>continues</code> statements.</li>
<li>How to use <code>else</code> clauses on loops.</li>
<li>What does the <code>pass</code> statement do, and when to use it.</li>
<li>How to use <code>range</code>.</li>
<li>What is a function and how do you use functions.</li>
<li>What does a function that does not use any <code>return</code> statement return .</li>
<li>Scope of variables.</li>
<li>What’s a traceback.</li>
<li>What are the arithmetic operators and how to use them.</li>
</ul>

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
  <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
  <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).</li>
  <li>All your files should end with a new line.</li>
  <li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code>.</li>
  <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory.</li>
  <li>Your code should use the pycodestyle (version <code>2.8.*</code>).</li>
  <li>All your files must be executable.</li>
  <li>The length of your files will be tested using <code>wc</code>.</li>
</ul>

```

<h2>16. ByteCode -> Python #2</h2>
Write the Python function <code>def magic_calculation(a, b, c):</code> that does exactly the same as the following Python bytecode:<br>


```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

<h2>Notes</h2>
AUTH: <a href="https://github.com/code-mar21">Maru sisay</a> <br>
MSG: "You are free to use the CODE" <br>
SIG: 13; 16

<br><br>
<a href="#top">Back to Top</a>
