from name_function import get_formatted_name

def main():
    """Tests get_formatted_name."""
    test_first_last_name()
    test_first_middle_last_name()

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('joplin', 'janis')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """Do names like 'Wolfgang Amadeous Mozart' work?"""
    formatted_name = get_formatted_name('mozart', 'wolfgang', 'amadeous')
    assert formatted_name == 'Wolfgang Amadeous Mozart'

if __name__ == "__main__":
    main()