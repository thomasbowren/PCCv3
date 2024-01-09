from population import get_city_country

def main():
    test_city_country()

def test_city_country():
    """Do locales such as Tokyo Japan work?"""
    locale = get_city_country('Tokyo', 'Japan')
    assert locale == 'Tokyo, Japan'

def test_city_country_population():
    """Do locales reported along with population, such as Tokyo, Japan population 14.264.798, work?"""
    locale = get_city_country('Tokyo', 'Japan', 14246798)
    assert locale == 'Tokyo, Japan - population 14246798'
    
if __name__ == "__main__":
    main()
