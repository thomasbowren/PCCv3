import printing_functions

def main():
    unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
    completed_designs = []
    printing_functions.print_models(unprinted_models, completed_designs)
    printing_functions.show_completed_models(completed_designs)

if __name__ == "__main__":
    main()