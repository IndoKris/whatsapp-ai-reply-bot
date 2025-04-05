
# THIS IS A WORKING API , But showing error in the end

import google.generativeai as genai
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)



genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual API key

# Load the correct model
model = genai.GenerativeModel("models/gemini-1.5-pro-002")  # Ensure this matches an available model

# Now, generate content
response = model.generate_content("Hello,my assistant !")

# Print the response
print(response.text)

