# Copyright 2023 undefined
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

def generate_markdown(pdf_folder, tex_folder, output_file):
    # Get a list of PDF and Latex files
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    tex_files = [f for f in os.listdir(tex_folder) if f.endswith(".tex")]

    # Create a Markdown table header
    markdown_content = "| 文件名 | PDF文件 | Latex文件 |\n| --- | --- | --- |"

    # Iterate through the files and add rows to the table
    for pdf_file in sorted(pdf_files):
        # Construct file names and paths
        file_name = os.path.splitext(pdf_file)[0]
        pdf_path = f"[{file_name}]({os.path.join(pdf_folder, pdf_file)})"
        tex_path = f"[{file_name}]({os.path.join(tex_folder, file_name + '.tex')})"
        
        # Add a new row to the table
        markdown_content += f"\n| {file_name} | {pdf_path} | {tex_path} |"

    # Write the Markdown content to the output file
    with open(output_file, "w") as file:
        file.write(markdown_content)



# Specify the folder paths and output file
pdf_folder = "./pdf_files"
tex_folder = "./tex_files"
output_file = "./README.md"

# Generate the Markdown file
generate_markdown(pdf_folder, tex_folder, output_file)
