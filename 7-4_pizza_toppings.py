prompt = "Enter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""

while topping != "quit":
    topping = input(prompt)

   if topping != "quit":
      print(f"I'll add {topping} to your pizza.")
