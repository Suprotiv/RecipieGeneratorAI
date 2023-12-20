import openai

import os

from flask import Flask, render_template_string, request

openai.api_key = os.environ['OPENAI_API_KEY']

def generate_tutorial(components):

  response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                 "role": "system",
                 "content": "You are a helpful assistant"
                }, {
                 "role":

                 "user",
                 "content":
                 f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"

                    }])


  return response['choices'][0]['message']['content']


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():


  return render_template_string('''


                   <!DOCTYPE html >


                   <html >


                   <head >


                    <title >Recipie Generator </title >


                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
                  rel="stylesheet">


                    <script >


                    async function generateTutorial() {



                     const components = document.querySelector('#components').value;



                     const output = document.querySelector('#output');



                     output.textContent = 'Cooking a recipe for you...';



                     const response = await fetch('/generate', {



                      method: 'POST',



                      body: new FormData(document.querySelector('#tutorial-form'))



                     });



                     const newOutput = await response.text();



                     output.textContent = newOutput;



                    }



                    function copyToClipboard() {

                     const output = document.querySelector('#output');

                     const textarea = document.createElement('textarea');



                     textarea.value = output.textContent;



                     document.body.appendChild(textarea);



                     textarea.select();



                     document.execCommand('copy');



                     document.body.removeChild(textarea);



                     alert('Copied to clipboard');



                    }



                    </script >



                   </head >



                   <body >



                    <div class="container">



                     <h1 class="my-4">Custom Recipe Tutorial Generator </h1 >



                     <form autocomplete="off" id="tutorial-form" onsubmit="event.preventDefault(); generateTutorial();" class="mb-3">


  <input autocomplete="false" name="hidden" type="text" style="display:none;">
                      <div class="mb-3">



                       <label for="components" class="form-label">Ingredients / Items:</label >



                       <input type="text" class="form-control" id="components" name="components" placeholder="Enter the list of Ingredients or items you have e.g. Bread, jam, potato etc. " required >



                      </div >



                      <button type="submit" class="btn btn-primary">Share with me a tutorial </button >



                     </form >



                     <div class="card">



                      <div class="card-header d-flex justify-content-between align-items-center">



                       Output:



                       <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">Copy </button >



                      </div >



                      <div class="card-body">



                       <pre id="output" class="mb-0" style="white-space: pre-wrap;"></pre >



                      </div >



                     </div >



                    </div >



                   </body >



                   </html >


               ''')
@app.route('/generate', methods=['POST'])

def generate():
  components = request.form['components']
  return generate_tutorial(components)

  # This code snippet starts the Flask application if the script is being run directly as the main program, running on the IP address '0.0.0.0' and port number 8080.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)