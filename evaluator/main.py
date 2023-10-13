from evaluator import *
from tokenizer import *

def main() -> None:
    print("\nARITHMETIC EXPRESSION EVALUATOR\n(enter a blank string to exit)\n")

    while True:
        expression = input("\n> ").strip()

        if not expression:
            print()
            break

        try:
            tokenizer = Tokenizer(expression)
            evaluator = Evaluator()

            tokens = tokenizer.tokenize()
            result = evaluator.evaluate(tokens)
            
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid expression.")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
