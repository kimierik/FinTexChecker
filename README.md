# FiTexChecker
cli tool grammar and spell and grammar checking for txt and tex files in the finnish language  
  

## depends on...
libvoikko

```sh
    pip3 install libvoikko
```
you also need to install the native libvoikko library from your package manager. detailed installisation instructions can be found here  https://voikko.puimula.org/  



## how to run

```sh
    python3 main.py /path/to/file
```
the program checks the file extention of the file. if it is a .tex file then it strips the file to its plaintext before checking.




