# vscode-command-breakdown
A function app that takes a query and breaks it down to get the commands users actually wanna perform in vscode

## Usage
- Input/Query - eg 
```
Copy line 5 and paste it in line 20
```

- Response
1. Error out if query is not passed
2. An array of commands user want to really perform eg. 
```
 [
   {command:"copy", file:"/src/hello.js", line:"5"},
   {command:"paste", file:"/src/hello.js", line:"20"}
 ]
```

## Basic Requirements
- Python installed -> [check here](https://github.com/pyenv/pyenv#homebrew-on-macos)
- azure cli installed -> [check here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos)
- function tools installed -> [check here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cmacos%2Ccsharp%2Cportal%2Cbash)

## Start Locally
You can start locally by running `func start`


## How to create a function app the python way
https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser
