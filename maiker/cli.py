#!/usr/bin/env python3
import json
import os
import webbrowser
from typing import Dict

import click
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_project(prompt: str, previous_response: str = "", type: str = "code") -> Dict[str, str]:
    """
    Given a project prompt, generate the corresponding project using OpenAI's GPT-3.5
    """

    if type == "presentation":
        system_prompt = 'You are a reveal.js presentation generator API to generate html presentations from a description using reveal.js (importing it from https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/js/reveal.min.js and initialize reveal at the end of the html, like \"<script>Reveal.initialize();</script></html>\"). Your returns html code in a file in raw json format {"<filename>": "<html code>"} directly in the response content.'
        user_prompt = f"Create a 10 slides reveal.js presentation with beautiful background picture and text(title and bullet points) based on this prompt: \"{prompt}\". Remember you don't talk english, don't explain anything, returns just raw json without line breaks"
    else:
        files_prompt = (
            f" You have already generated these files: {previous_response}, dont return them again, just return the rest of needed files to complete the project or returns an empty response if there are no more files to return."
            if previous_response
            else ""
        )
        system_prompt = 'You are a project code generator API to generate coding projects from a description. Your returns code in separated files in raw json format {"<filename>": "<code>"} directly in the response content.'
        user_prompt = f"Create a code project based on this description: {prompt}{files_prompt}. Remember you don't talk english, don't explain anything, returns just raw json without line breaks"
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0,
    )

    generated_code = completion.choices[0].message.content
    try:
        if generated_code:
            generated_code = json.loads(generated_code)
    except json.JSONDecodeError as e:
        raise click.ClickException(
            f"Code generation failed. Please check your prompt and try again. Error: {str(e)}, generated_code: {generated_code}"
        )
    return generated_code


@click.command()
@click.argument("prompt")
@click.option(
    "--output-dir",
    "-o",
    default="./maiker-generated-project",
    help="The directory where the generated code files will be saved.",
)
@click.option('-t', '--type', required=False, type=click.Choice(['code', 'presentation']), default='code')

def main(prompt: str, output_dir: str, type: str):
    """
    Given a project prompt, generate the corresponding project using OpenAI's GPT-3.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate the code project
    click.echo(f"Generating {type} project from prompt: {prompt}")

    max_loops = 1 # Number of calls to the model, increase it for complex projects
    generated_files = []
    for _loop in range(max_loops):
        generated_code = generate_project(prompt, ",".join(generated_files), type)

        for filename, contents in generated_code.items():
            file_path = os.path.join(output_dir, filename)
            folder = os.path.dirname(filename)
            folder_path = os.path.join(output_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

            with open(file_path, "w") as f:
                f.write(contents)
                generated_files.append(filename)

        #click.echo(f"Generated code: {generated_code}")
        #click.echo(f"Generated files: {generated_files}")

    # Print success message to console
    click.echo(f"Project generation successful. Project files saved to {output_dir}.")

    if type == 'presentation':
        presentation_file = generated_files[0]
        try:
            webbrowser.open(os.path.join(output_dir, presentation_file))
        except Exception:
            print(f"Error running the web browser, you can try to open the outputfile: {output_file} manually")



if __name__ == "__main__":
    main()
