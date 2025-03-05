#!/usr/bin/env python3
import csv
import subprocess
import json
import sys

# ===========================
# Configuration
# ===========================
# Update the LLM name here. For example, you might use one of the following:
#
#   Smaller Models: llama3.2:1b, phi3:3.8b, gemma2:2b, deepseek-r1:1.5b
#   Larger Models:  llama3.2:latest, phi4:14b, gemma2:9b, deepseek-r1:7b
#
# For this script, we're using a single LLM. Change LLM_NAME as needed.
LLM_NAME = "phi3:3.8b"

# Modify this prompt template to change the instructions given to the LLM.
PROMPT_TEMPLATE = """Analyze the following executive townhall question/comment.
Provide:
1. Rewrite the question to make it one short sentence that can be read aloud to the CEO by the moderator during the event.
2. Provide the theme of the comment in a maximum of 3 words for categorization.

Return your answer strictly in JSON format with keys "summary" and "theme".

Question/Comment: "{comment}"
"""

# ===========================
# Helper Functions
# ===========================

def clean_response(response):
    """
    Clean up the LLM response by removing Markdown code fences (e.g., ```).
    """
    if response.startswith("```"):
        lines = response.splitlines()
        # Remove first line if it starts with ```
        if lines[0].startswith("```"):
            lines = lines[1:]
        # Remove last line if it starts with ```
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        response = "\n".join(lines).strip()
    return response

def analyze_comment(comment):
    """
    Calls the local LLM (using the LLM_NAME) via Ollama to analyze the given comment.
    Returns a dictionary with 'summary' and 'theme' keys if successful.
    """
    # Format the prompt with the provided comment.
    prompt = PROMPT_TEMPLATE.format(comment=comment)
    
    try:
        # Run the local LLM via Ollama using the constructed prompt.
        result = subprocess.run(
            ["ollama", "run", LLM_NAME, prompt],
            capture_output=True, text=True, check=True
        )
        response = result.stdout.strip()
        # Clean the response to remove Markdown code fences.
        response = clean_response(response)
        # Parse and return the JSON output.
        analysis = json.loads(response)
        return analysis
    except subprocess.CalledProcessError as e:
        print(f"Error running LLM for comment: {comment}\n{e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON for comment: {comment}\nOutput was: {response}\n{e}")
        return None

# ===========================
# Main Processing Function
# ===========================

def main():
    # Check for the required input CSV filename argument.
    if len(sys.argv) < 2:
        print("Usage: python summarize.py <input_csv>")
        sys.exit(1)
    
    # Get the input CSV filename from the command-line arguments.
    input_csv = sys.argv[1]
    output_csv = "output.csv"  # Output filename is fixed.

    # Open the input CSV for reading and output CSV for writing.
    with open(input_csv, mode='r', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header row to the output CSV.
        writer.writerow(["original_question", "summary", "theme"])
        
        # Process each row in the input CSV.
        for row in reader:
            if not row:
                continue  # Skip empty rows.
            original = row[0]  # Assumes the question/comment is in the first column.
            
            print("=== Processing Iteration ===")
            print(f"Input: {original}")
            
            analysis = analyze_comment(original)
            
            if analysis:
                summary = analysis.get("summary", "")
                theme = analysis.get("theme", "")
                print(f"Output: {analysis}")
            else:
                summary, theme = "", ""
                print("Output: No valid response received.")
            
            # Write the original question, summary, and theme to the output CSV.
            writer.writerow([original, summary, theme])
            print(f"Processed: {original}\n")
            
if __name__ == "__main__":
    main()
