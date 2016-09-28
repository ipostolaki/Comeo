# Comeo Contribution Guideline

### Have an idea?

**Describe it**  
Feel free to open an issue with short description of your suggestion to start a discussion.  

**Implement it**  
When opening a pull request with new code, *please* use this checklist:  

- Critical methods are covered by unit tests. Use `make tests`  
- Your code is accompanied by inline comments and docstrings where it may be necessary  
- If you are adding front-end related functionality, make sure that it is styled by the bootstrap theme  
- New code is PEP8 formatted. There is a tuned make target `make flake`, it will help you find the lines where formatting is needed.


# Comeo Codebase Principles

Comeo project and its codebase strives to achieve these ideas.

### Modularity
Different deployments may require different functionality.  
Thus for the end user there should be a way to disable/enable distinct modules with certain functionality.

### Extensibility
For the most sensitive parts there should be an API which one can use to extend the codebase. For example different deployments may use custom logic for payments processing.


### Interconnectivity
Distinctly deployed instances of Comeo should have a way to communicate with each other. For example to transmit information about users resources, which is stored in the registry.

### Usability  
Comeo is made to be used :wink:  
Thus, for both new and old features, there should be enough focus and effort to provide smooth user experience for non tech-savvy people.
