# Maiker

Maiker is an AI-powered coding project generator that uses OpenAI's GPT-3.5 to generate entire code projects from a user-provided prompt. 
![maiker-cli](https://user-images.githubusercontent.com/480507/236608705-0d22225b-64da-4ff3-957f-aee91901e9f6.jpeg)

This is the command line version of the [maiker](https://github.com/lusob/maiker/) vscode extension

## Features

- Generates entire code projects based on user-provided prompts
- Uses OpenAI's ChatGPT-3.5 model for code generation
- Outputs code to a local project directory

## Installation

1. Install the CLI globally: `pip install git+https://github.com/lusob/maiker-cli.git`.
2. Set your OpenAI API key: `export OPENAI_API_KEY="<your-open-api-key>"`.
3. Use the `maiker` command to generate a code project from a user-provided prompt, for example:
    
    ```
    maiker "a snake game using just html and js"; open maiker-generated-project/index.html
    ```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

