# Introduction to Python

Wellcome to the **Applied Machine Learning** course. During this course, we will use [Python](https://www.python.org) programming language to perform matrix computations, image manipulation and retrieval tasks. As a number of people have not worked with Python before, we start the course with an introduction to the language. 

Python is a very popular high-level programming language with an emphasis on code readability and writing with a minimal amount of lines. The Python programming language contains a number of features that make it easy to learn. Most notably:

- It has a dynamic type system (so you don't have to explicitly give the type to a variable, like `int` or `float` or `string`. Python will figure it out by itself).
- It has automatic memory management (so you don't have to worry that much about freeing the memory and worrying about pointers).
- There is a rich set of libraries ready to import that will make your life easier (from simple math libraries to a whole 2D game engine).

We start with an introduction to Python and a few very useful libraries for this course. Please take care to fully understand what is happening in this introduction and feel very free to mess around with the language in order to understand how it works. We expect that the people unfamiliar with Python will quickly come to like the language. 

### Installation

We recommend you to use Python 3.6 or newer. The easiest way to install Python interpreter, as well as the required packages, is to use **Anaconda** - scientific Python distributions. It comes with virtual environment manager, popular libraries and utils. Just [download](https://www.anaconda.com/download/) the proper version of **Anaconda** and follow the instructions. Linux/macOS users also have to add `anaconda/bin` to `PATH` variable. 

```
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc 
source .bashrc
``` 

There are other ways of installing Python, creating the environment and managing the packages. The above-stated method is not the best one, however, it will allow us to help you with possible troubles during the course.

### How to run

There is a number of ways how to create and run python programs. One way is to create a `.py` file and run it from the command line: `python <name of a file>`. It is also possible to open a Python interpreter by simply typing `python` in the command line. In the interpreter, you can type individual commands, which is very useful when you want to test short code lines. 

For the rest of this course, however, you will be using the **Jupyter Notebook**. It combines the Python interpreter, Markdown and visualization tools (and even more). It can be run just by typing `jupyter notebook` in a terminal/cmd. The Jupyter Notebook is a bit similar to the Python interpreter, but with a number of advantages. Namely, it also serves as a browser-based notebook (so we can explain the assignments and you can write down your own notes) and you can easily print and plot results. 

<!--### Materials
Each week, you will be presented with a new notebook containing some explanation as well as a number of assignments. The notebooks can be used to write and test your code for yourself and for the assignments. We also created a [repository](https://github.com/ISosnovik/UVA_AML17) on GitHub where you can get the materials for this course. You can download them from Piazza as well.-->

### Q&A
**Q: Are there alternative methods of launching Jupyter Notebook?**

A: The latest versions of Anaconda provide users with the GUI launchers. Just double-click the icon to launch the application.

**Q: I have Anaconda with the previous version of Python and I would like to switch to the newer one. How to do it?**

A: You can [create](https://conda.io/docs/user-guide/tasks/manage-environments.html) a new virtual environment with the version of Python you like. And then [add](https://ipython.readthedocs.io/en/latest/install/kernel_install.html) this kernel to Jupyter Notebook. 

```
conda create -n py36 python=3.6.3
source activate py36
python -m ipykernel install --name py36
source deactivate
```

**Q: I created a new virtual environment. How can I install all the required packages?**

A: You can install them with `conda` and/or `pip`. We will use *numpy, scipy, matplotlib* and *scikit-learn* for the assignments. We will use *requests* as well.

```
source activate py36 (or just `activate py36` for win)
conda install -c anaconda numpy
conda install -c anaconda scipy 
conda install scikit-learn
conda install -c conda-forge matplotlib
conda install -c anaconda requests
source deactivate (or just `deactivate` for win)
```

**Q: How can I get the materials from GitHub?**

A: There are several ways of downloading the files from GitHub: 

* The first one and the simplest one is just to visit the repository and download `.zip` archive.
* You can [download](https://desktop.github.com) the official GitHub desktop client. Then visit the GitHub repository and click `Open in Desktop` on the website and the rest will be done automatically by the client. 
* You can clone the repository to your computer by typing the following command in a terminal/cmd: `git clone https://github.com/ISosnovik/UVA_AML17`. But first, [install](https://git-scm.com/downloads) git. You may also find this [tutorial](https://try.github.io/) very useful
 















