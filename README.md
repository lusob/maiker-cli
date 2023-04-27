# Maiker

Maiker is an AI-powered coding project generator that uses OpenAI's GPT-3.5 to generate entire code projects from a user-provided prompt. 

## Features

- Generates entire code projects based on user-provided prompts
- Uses OpenAI's ChatGPT-3.5 model for code generation
- Outputs code to a local project directory

## Installation

1. Install the CLI globally: `pip install git+https://github.com/lusob/maiker-cli.git`.
2. Set your OpenAI API key: `export OPENAI_API_KEY="<your-open-api-key>"`.
3. Use the `maiker` command to generate a code project from a user-provided prompt, for example:
    > maiker "a snake game using just html and js"; open maiker-generated-project/index.html

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

